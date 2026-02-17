# Phase 0 Tools

Discovery and cataloging tools for the algorithms repository refactoring.

## Tools

### 1. catalog_modules.py

Categorizes all Python modules as data structures, algorithms, utilities, or tests.

**Usage:**
```bash
python tools/catalog_modules.py --format md > MODULE_CATALOG.md
python tools/catalog_modules.py --format json --output catalog.json
```

**Output:** `MODULE_CATALOG.md` with classification and statistics

---

### 2. find_dangerous_defaults.py

Finds dangerous mutable default arguments (`def func(param={})` or `param=[]`).

**Usage:**
```bash
python tools/find_dangerous_defaults.py algorithms/
python tools/find_dangerous_defaults.py algorithms/ data_structures/ > DANGEROUS_DEFAULTS.md
```

**Output:** `DANGEROUS_DEFAULTS.md` with locations and suggested fixes

---

### 3. find_wildcard_imports.py

Finds all wildcard imports (`from module import *`) and suggests explicit imports.

**Usage:**
```bash
python tools/find_wildcard_imports.py
python tools/find_wildcard_imports.py --path algorithms/ > WILDCARD_AUDIT.md
```

**Output:** `WILDCARD_AUDIT.md` with explicit import suggestions

---

### 4. analyze_imports.py

Analyzes import dependencies and finds circular dependencies.

**Usage:**
```bash
python tools/analyze_imports.py --graph > DEPENDENCY_ANALYSIS.md
python tools/analyze_imports.py --graph --output dependency_graph.json
python tools/analyze_imports.py --find-cycles
```

**Output:** 
- `DEPENDENCY_ANALYSIS.md` - Human-readable analysis
- `dependency_graph.json` - Machine-readable graph data

---

### 5. generate_all_lists.py

Generates explicit `__all__` lists for `__init__.py` files.

**Usage:**
```bash
python tools/generate_all_lists.py algorithms/array/ > /tmp/array_init.py
python tools/generate_all_lists.py algorithms/array/ --write --backup
```

**Output:** New `__init__.py` content with explicit imports and `__all__`

---

### 6. migrate_imports.py

Migrates user code from old import structure to new structure.

**Usage:**
```bash
python tools/migrate_imports.py --path /path/to/user/code --dry-run
python tools/migrate_imports.py --path /path/to/user/code
```

**Output:** Updated imports in all Python files

---

## Running All Phase 0 Tools

To generate all Phase 0 reports:

```bash
# Create output directory
mkdir -p docs/internal/phase0

# 1. Module catalog
python tools/catalog_modules.py --format md > docs/internal/phase0/MODULE_CATALOG.md
python tools/catalog_modules.py --format json --output docs/internal/phase0/catalog.json

# 2. Dangerous defaults
python tools/find_dangerous_defaults.py algorithms/ > docs/internal/phase0/DANGEROUS_DEFAULTS.md

# 3. Wildcard imports
python tools/find_wildcard_imports.py > docs/internal/phase0/WILDCARD_AUDIT.md

# 4. Import analysis
python tools/analyze_imports.py --graph > docs/internal/phase0/DEPENDENCY_ANALYSIS.md
python tools/analyze_imports.py --graph --output docs/internal/phase0/dependency_graph.json

# 5. Generate Phase 0 summary report
echo "Phase 0 Discovery Complete!" > docs/internal/phase0/PHASE_0_REPORT.md
echo "" >> docs/internal/phase0/PHASE_0_REPORT.md
echo "See individual reports for details." >> docs/internal/phase0/PHASE_0_REPORT.md
```

Or use the convenience script:

```bash
bash tools/run_phase0.sh
```

## Testing

Basic smoke tests are in `tools/tests/`:

```bash
python -m pytest tools/tests/ -v
```

## Requirements

All tools use only Python standard library (ast, argparse, pathlib, json).
No external dependencies required.


