#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validate every data/*.json against its JSON Schema in data/_schema/.

Each data file names its schema in "$schema" (e.g. "./_schema/events.schema.json");
a file without that key uses data/_schema/<name>.schema.json. The schemas are plain
draft 2020-12, so editors (VS Code) validate the same files while you type.

No dependencies: this is a small validator for the keyword subset the schemas use —
type, required, properties, additionalProperties, items, enum, const, pattern,
minimum, maximum, minLength, minItems, anyOf, allOf, oneOf, $ref (local "#/…").
A schema that uses any other keyword is an error, so a new keyword can never be
silently ignored — add it here first.

Usage (repo root or anywhere):
  python3 tools/validate_data.py            # validate all data/*.json; exit 1 on any error
  python3 tools/validate_data.py events     # only data/events.json (several names allowed)

Run it after editing any data/*.json (alongside tools/sync_data.py).
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, 'data')
SCHEMA_DIR = os.path.join(DATA, '_schema')

ANNOTATIONS = {'$schema', '$id', '$comment', 'title', 'description', '$defs'}
KEYWORDS = ANNOTATIONS | {
    'type', 'required', 'properties', 'additionalProperties', 'items', 'enum', 'const',
    'pattern', 'minimum', 'maximum', 'minLength', 'minItems', 'anyOf', 'allOf', 'oneOf', '$ref',
}
TYPES = {
    'object': lambda v: isinstance(v, dict),
    'array': lambda v: isinstance(v, list),
    'string': lambda v: isinstance(v, str),
    'boolean': lambda v: isinstance(v, bool),
    'null': lambda v: v is None,
    'integer': lambda v: isinstance(v, int) and not isinstance(v, bool),
    'number': lambda v: isinstance(v, (int, float)) and not isinstance(v, bool),
}


class SchemaError(Exception):
    pass


def check_keywords(node, where):
    """Reject unsupported keywords anywhere in the schema tree."""
    if not isinstance(node, dict):
        raise SchemaError(f'{where}: schema must be an object, got {type(node).__name__}')
    unknown = set(node) - KEYWORDS
    if unknown:
        raise SchemaError(f'{where}: unsupported keyword(s) {sorted(unknown)} — teach tools/validate_data.py first')
    for t in ([node['type']] if isinstance(node.get('type'), str) else node.get('type', [])):
        if t not in TYPES:
            raise SchemaError(f'{where}: unknown type {t!r}')
    for key in ('properties', '$defs'):
        for name, sub in node.get(key, {}).items():
            check_keywords(sub, f'{where}/{key}/{name}')
    for key in ('items', 'additionalProperties'):
        if isinstance(node.get(key), dict):
            check_keywords(node[key], f'{where}/{key}')
    for key in ('anyOf', 'allOf', 'oneOf'):
        for i, sub in enumerate(node.get(key, [])):
            check_keywords(sub, f'{where}/{key}/{i}')


def resolve(root, ref):
    if not ref.startswith('#/'):
        raise SchemaError(f'only local refs are supported, got {ref!r}')
    node = root
    for part in ref[2:].split('/'):
        node = node[part.replace('~1', '/').replace('~0', '~')]
    return node


def validate(value, schema, root, path, errors):
    if '$ref' in schema:
        validate(value, resolve(root, schema['$ref']), root, path, errors)

    if 'type' in schema:
        types = [schema['type']] if isinstance(schema['type'], str) else schema['type']
        if not any(TYPES[t](value) for t in types):
            errors.append(f'{path}: expected {" or ".join(types)}, got {json.dumps(value, ensure_ascii=False)[:60]}')
            return
    if 'enum' in schema and value not in schema['enum']:
        errors.append(f'{path}: {value!r} is not one of {schema["enum"]}')
    if 'const' in schema and value != schema['const']:
        errors.append(f'{path}: expected {schema["const"]!r}')

    for sub in schema.get('allOf', []):
        validate(value, sub, root, path, errors)
    for key in ('anyOf', 'oneOf'):
        if key in schema:
            matches = 0
            for sub in schema[key]:
                sub_errors = []
                validate(value, sub, root, path, sub_errors)
                matches += not sub_errors
            if matches == 0 or (key == 'oneOf' and matches > 1):
                errors.append(f'{path}: matches {matches} of the {key} options, got {json.dumps(value, ensure_ascii=False)[:60]}')

    if isinstance(value, dict):
        for name in schema.get('required', []):
            if name not in value:
                errors.append(f'{path}: missing required "{name}"')
        props = schema.get('properties', {})
        extra = schema.get('additionalProperties', True)
        for name, item in value.items():
            if name in props:
                validate(item, props[name], root, f'{path}.{name}', errors)
            elif extra is False:
                errors.append(f'{path}: unexpected property "{name}"')
            elif isinstance(extra, dict):
                validate(item, extra, root, f'{path}.{name}', errors)
    elif isinstance(value, list):
        if len(value) < schema.get('minItems', 0):
            errors.append(f'{path}: expected at least {schema["minItems"]} items')
        if 'items' in schema:
            for i, item in enumerate(value):
                validate(item, schema['items'], root, f'{path}[{i}]', errors)
    elif isinstance(value, str):
        if 'pattern' in schema and not re.search(schema['pattern'], value):
            errors.append(f'{path}: {value!r} does not match {schema["pattern"]}')
        if len(value) < schema.get('minLength', 0):
            errors.append(f'{path}: shorter than {schema["minLength"]}')
    elif TYPES['number'](value):
        if 'minimum' in schema and value < schema['minimum']:
            errors.append(f'{path}: {value} < minimum {schema["minimum"]}')
        if 'maximum' in schema and value > schema['maximum']:
            errors.append(f'{path}: {value} > maximum {schema["maximum"]}')


def schema_path_for(data_path, data):
    ref = data.get('$schema') if isinstance(data, dict) else None
    if ref:
        return os.path.normpath(os.path.join(os.path.dirname(data_path), ref))
    name = os.path.splitext(os.path.basename(data_path))[0]
    return os.path.join(SCHEMA_DIR, f'{name}.schema.json')


def main(argv):
    names = sorted(f for f in os.listdir(DATA) if f.endswith('.json'))
    if argv:
        wanted = {a if a.endswith('.json') else f'{a}.json' for a in argv}
        missing = wanted - set(names)
        if missing:
            print(f'no such data file: {", ".join(sorted(missing))}')
            return 2
        names = [n for n in names if n in wanted]

    failed = 0
    for name in names:
        data_path = os.path.join(DATA, name)
        try:
            with open(data_path, encoding='utf-8') as f:
                data = json.load(f)
            schema_path = schema_path_for(data_path, data)
            if not os.path.isfile(schema_path):
                raise SchemaError(f'schema not found: {os.path.relpath(schema_path, ROOT)}')
            with open(schema_path, encoding='utf-8') as f:
                schema = json.load(f)
            check_keywords(schema, os.path.relpath(schema_path, ROOT))
            errors = []
            validate(data, schema, schema, '$', errors)
        except (ValueError, SchemaError, KeyError) as e:
            errors = [f'{type(e).__name__}: {e}']
        if errors:
            failed += 1
            print(f'FAIL data/{name} ({len(errors)} error{"s" * (len(errors) != 1)})')
            for err in errors[:50]:
                print(f'  {err}')
            if len(errors) > 50:
                print(f'  … {len(errors) - 50} more')
        else:
            print(f'ok   data/{name}')

    print(f'\n{len(names) - failed}/{len(names)} data files valid')
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
