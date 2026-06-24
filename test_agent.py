#!/usr/bin/env python
"""Quick test of the AIDA agent repository analyzer"""

import sys
sys.path.insert(0, '.')
from my_agent.agentv2 import analyze_repository_contents

print("Testing AIDA Agent - Repository Analysis\n")
print("=" * 60)

# Test the analysis function
result = analyze_repository_contents('.')

# Report statistics
py_count = result.count("=== ARCHIVO FUENTE PYTHON:")
nb_count = result.count("=== JUPYTER NOTEBOOK:")
error_count = result.count("=== ERROR AL LEER")

print(f"✓ Analysis completed successfully")
print(f"  - Python files found: {py_count}")
print(f"  - Jupyter notebooks found: {nb_count}")
print(f"  - Read errors: {error_count}")
print(f"  - Total output size: {len(result):,} characters")
print("\n" + "=" * 60)
print("ANALYSIS PREVIEW (First 1500 characters):")
print("=" * 60)
print(result[:1500])
print("\n... (content truncated) ...\n")
