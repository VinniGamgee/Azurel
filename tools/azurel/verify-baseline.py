#!/usr/bin/env python3
"""Fail CI if the known-good Torzu graphics source has changed."""
import subprocess
BASELINE_TREES = {'src/video_core': 'c152318f3edde919ee5c920ab01beeff233ebb3c', 'src/shader_recompiler': '2226c370bcb7a9d31bb79cd41e84ff03fb199079'}
for path, expected in BASELINE_TREES.items():
    actual = subprocess.check_output(["git", "rev-parse", f"HEAD:{path}"], text=True).strip()
    if actual != expected:
        raise SystemExit(f"Torzu baseline mismatch: {path}: {actual} != {expected}")
    print(f"Unchanged Torzu source: {path} ({actual})")
