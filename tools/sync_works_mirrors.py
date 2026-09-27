#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DEPRECATED NAME — kept so older instructions/sessions keep working.

All generated data copies are now produced by tools/sync_data.py (artist pages load
data/generated/*.js instead of carrying inline copies). This wrapper just runs it,
passing any arguments through (e.g. --check).

    python3 tools/sync_data.py            # preferred
"""
import os, runpy, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.argv[0] = os.path.join(HERE, "sync_data.py")
runpy.run_path(sys.argv[0], run_name="__main__")
