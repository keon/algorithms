# Comprehensive Refactor Plan for Algorithms Repository

## Executive Summary

This document outlines a comprehensive refactoring plan to modernize the algorithms repository, focusing on:
- Clear separation between data structures and algorithms
- Improved modularity and readability
- Modern Python 3.12+ standards and best practices
- Enhanced test organization with pytest
- Better code maintainability

---

## 1. Critical Architectural Decisions (Must Resolve First)

Before proceeding with the refactoring, several architectural ambiguities in the current codebase must be resolved:

### 1.1 Union-Find/Disjoint Set Consolidation

**Issue**: There are TWO different Union-Find implementations:
1. `algorithms/unionfind/count_islands.py` - Contains `Union` class
2. `algorithms/graph/minimum_spanning_tree.py` - Contains `DisjointSet` class

**Decision Required**:
- **Consolidate** into single implementation in `data_structures/sets/union_find.py`
- Choose canonical name: `UnionFind` (preferred for clarity)
- Migrate both use cases to the unified implementation
- Keep `Union` and `DisjointSet` as deprecated aliases in v0.2.0

**Recommended Implementation**:
```python
# data_structures/sets/union_find.py
class UnionFind:
    """Union-Find (Disjoint Set) data structure with path compression and union by rank."""
    
    def __init__(self):
        self.parent = {}
        self.rank = {}
        self.count = 0
    
    def make_set(self, element):
        """Create a new set containing the single element."""
        self.parent[element] = element
        self.rank[element] = 0
        self.count += 1
    
    def find(self, element):
        """Find the root of the set containing element (with path compression)."""
        if self.parent[element] != element:
            self.parent[element] = self.find(self.parent[element])
        return self.parent[element]
    
    def union(self, element1, element2):
        """Merge the sets containing element1 and element2 (union by rank)."""
        root1, root2 = self.find(element1), self.find(element2)
        if root1 == root2:
            return
        
        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        elif self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1
        
        self.count -= 1

# Deprecated aliases for backward compatibility
Union = UnionFind
DisjointSet = UnionFind
```

### 1.2 BFS/DFS Module Organization

**Issue**: `algorithms/bfs/` and `algorithms/dfs/` contain specific algorithm implementations, but BFS/DFS are **techniques**, not categories.

**Current Files**:
- `bfs/count_islands.py` - Graph algorithm using BFS
- `bfs/maze_search.py` - Graph algorithm using BFS
- `bfs/shortest_distance_from_all_buildings.py` - Graph algorithm using BFS
- `bfs/word_ladder.py` - Graph algorithm using BFS
- `dfs/count_islands.py` - Graph algorithm using DFS
- `dfs/maze_search.py` - Graph algorithm using DFS
- `dfs/pacific_atlantic.py` - Matrix/Graph algorithm using DFS
- `dfs/sudoku_solver.py` - Backtracking algorithm using DFS
- `dfs/walls_and_gates.py` - Matrix/Graph algorithm using DFS

**Decision**:
- **Merge** BFS/DFS modules into appropriate algorithm categories
- BFS/DFS are implementation techniques, not algorithmic categories

**Proposed Mapping**:
```
OLD                                          NEW
algorithms/bfs/count_islands.py       →  algorithms/graph/count_islands_bfs.py
algorithms/bfs/maze_search.py         →  algorithms/graph/maze_search_bfs.py
algorithms/bfs/shortest_distance...   →  algorithms/graph/shortest_distance_from_all_buildings.py
algorithms/bfs/word_ladder.py         →  algorithms/graph/word_ladder.py

algorithms/dfs/count_islands.py       →  algorithms/graph/count_islands_dfs.py
algorithms/dfs/maze_search.py         →  algorithms/graph/maze_search_dfs.py
algorithms/dfs/pacific_atlantic.py    →  algorithms/graph/pacific_atlantic.py
algorithms/dfs/sudoku_solver.py       →  algorithms/backtracking/sudoku_solver.py
algorithms/dfs/walls_and_gates.py     →  algorithms/graph/walls_and_gates.py
algorithms/dfs/all_factors.py         →  algorithms/math/all_factors.py
```

**Rationale**: Group by problem domain (graph, backtracking, math), not by technique.

### 1.3 Heap Module Split

**Issue**: `algorithms/heap/` contains BOTH a data structure AND algorithms.

**Current Files**:
- `heap/binary_heap.py` - **Data Structure** → Move to `data_structures/heaps/`
- `heap/k_closest_points.py` - **Algorithm** → Keep in algorithms
- `heap/merge_sorted_k_lists.py` - **Algorithm** → Keep in algorithms
- `heap/skyline.py` - **Algorithm** → Keep in algorithms
- `heap/sliding_window_max.py` - **Algorithm** → Keep in algorithms

**Decision**:
```
data_structures/heaps/
├── __init__.py
└── binary_heap.py (moved from algorithms/heap/)

algorithms/array/  (or algorithms/misc/)
├── k_closest_points.py (uses heaps)
├── merge_sorted_k_lists.py (uses heaps)
├── skyline.py (uses heaps)
└── sliding_window_max.py (uses heaps)
```

### 1.4 Tree Structure Complexity

**Issue**: `algorithms/tree/` mixes data structures, algorithms, and has nested subdirectories with their own data structures.

**Current Complex Structure**:
```
algorithms/tree/
├── tree.py (TreeNode class)
├── bst/
│   ├── bst.py (BST class - DATA STRUCTURE)
│   ├── array_to_bst.py (algorithm)
│   ├── kth_smallest.py (algorithm)
│   └── [14 more algorithm files]
├── avl/
│   └── avl.py (AVL class - DATA STRUCTURE)
├── red_black_tree/
│   └── red_black_tree.py (RBTree class - DATA STRUCTURE)
├── trie/
│   ├── trie.py (Trie class - DATA STRUCTURE)
│   └── add_and_search.py (algorithm)
├── segment_tree/
│   └── [2 files - DATA STRUCTURES]
├── fenwick_tree/
│   └── fenwick_tree.py (DATA STRUCTURE)
└── [30+ algorithm files]
```

**Decision - Data Structures**:
```
data_structures/trees/
├── __init__.py
├── tree_node.py (from tree/tree.py - base TreeNode)
├── binary_search_tree.py (from tree/bst/bst.py)
├── avl_tree.py (from tree/avl/avl.py)
├── red_black_tree.py (from tree/red_black_tree/)
├── trie.py (from tree/trie/trie.py)
├── segment_tree.py (from tree/segment_tree/)
└── fenwick_tree.py (from tree/fenwick_tree/)
```

**Decision - Algorithms**:
```
algorithms/tree/
├── __init__.py
├── binary_search_tree/  (algorithms specific to BST)
│   ├── array_to_bst.py
│   ├── kth_smallest.py
│   ├── validate_bst.py
│   └── [other BST algorithms]
├── trie/  (algorithms using Trie)
│   └── add_and_search.py
├── traversal/  (keep as-is)
│   ├── inorder.py
│   ├── preorder.py
│   └── postorder.py
└── [general tree algorithms]
    ├── invert_tree.py
    ├── max_height.py
    └── ...
```

**Critical Fix Required**: Update imports in AVL tree:
```python
# BEFORE
from tree.tree import TreeNode

# AFTER
from data_structures.trees.tree_node import TreeNode
```

### 1.5 Module Placement Decisions

**Issue**: Several modules have unclear categorization.

| Module | Current | Proposed | Rationale |
|--------|---------|----------|-----------|
| `distribution` | `algorithms/distribution/` | `algorithms/math/statistics/` | Statistics is a branch of mathematics |
| `queues/priority_queue.py` | `algorithms/queues/` | `data_structures/heaps/priority_queue.py` | Priority queue is a data structure (heap-based) |
| `ml` | `algorithms/ml/` | `algorithms/graph/` or remove | `nearest_neighbor.py` is a graph algorithm; ML doesn't fit scope |
| `streaming` | `algorithms/streaming/` | Keep as `algorithms/streaming/` | Valid algorithmic category (not misc) |
| `unix` | `algorithms/unix/` | Remove or separate package | Not algorithms; these are utilities |

### 1.6 Linked List Structure

**Issue**: `algorithms/linkedlist/linkedlist.py` only defines node classes, not full data structures.

**Current**:
```python
class DoublyLinkedListNode(object):  # Just a node
class SinglyLinkedListNode(object):  # Just a node
```

**Decision**: Implement full linked list data structures:
```python
# data_structures/linear/linked_list.py
from dataclasses import dataclass
from typing import Optional, Generic, TypeVar

T = TypeVar('T')

@dataclass
class SinglyNode(Generic[T]):
    value: T
    next: Optional['SinglyNode[T]'] = None

@dataclass
class DoublyNode(Generic[T]):
    value: T
    next: Optional['DoublyNode[T]'] = None
    prev: Optional['DoublyNode[T]'] = None

class SinglyLinkedList(Generic[T]):
    """Complete singly linked list implementation."""
    def __init__(self):
        self.head: Optional[SinglyNode[T]] = None
        self._size = 0
    
    def append(self, value: T) -> None: ...
    def prepend(self, value: T) -> None: ...
    def delete(self, value: T) -> bool: ...
    def search(self, value: T) -> Optional[SinglyNode[T]]: ...
    def __len__(self) -> int: ...
    def __iter__(self): ...

class DoublyLinkedList(Generic[T]):
    """Complete doubly linked list implementation."""
    # Similar interface
```

### 1.7 Risk & Effort Prioritization

To keep the plan actionable, each architectural decision is scored for **Risk** (impact if wrong / discovered late) and **Effort** (estimated engineering weeks). Use this table to prioritize work if timelines change; address high-risk items first.

| # | Decision | Risk | Effort | Mitigation / Notes |
|---|----------|------|--------|--------------------|
| 1 | Union-Find consolidation | **High** (two divergent implementations used in critical algorithms) | Medium (1-1.5 weeks) | Tackle at start of Phase 2; add dedicated tests before removing legacy classes |
| 2 | BFS/DFS merger | High (touches many imports/tests) | High (2 weeks) | Prototype mapping on small subset, keep compatibility modules with smoke tests |
| 3 | Tree structure separation | Medium-High (deep import graph, custom Node classes) | High (2-3 weeks) | Execute incrementally per subtree; ensure AVL/BST imports are green before moving algorithms |
| 4 | Test import migration | Medium (breaks CI immediately if wrong) | Medium (1 week) | Build tooling + compatibility layer before running automated changes |
| 5 | Compatibility + module-level exports | Medium (risk of breaking user imports) | Low-Medium (3-4 days) | Keep real module object, expose deprecated names via `globals()`; add dedicated regression tests |
| 6 | Module placement (distribution, ml, unix) | Low-Medium | Low | Decide during Phase 5; document in CHANGELOG to avoid surprises |

**Action**: Update this table after Phase 0 when real measurements (file counts, dependency depth) are known; treat it as the source of truth for prioritizing contentious work.

---

## 2. Project Structure Reorganization

### 2.1 Separate Data Structures from Algorithms

**Current Issue**: Data structures and algorithms are mixed together without clear boundaries.

**Proposed Structure** (reflecting decisions from Section 1):
```
algorithms/
├── data_structures/          # NEW: Separate data structures package
│   ├── __init__.py
│   ├── linear/
│   │   ├── __init__.py
│   │   ├── linked_list.py   # NEW: Full implementation (not just nodes)
│   │   ├── stack.py          # From stack/stack.py
│   │   └── queue.py          # From queues/queue.py
│   ├── trees/
│   │   ├── __init__.py
│   │   ├── tree_node.py      # From tree/tree.py (base TreeNode)
│   │   ├── binary_search_tree.py  # From tree/bst/bst.py
│   │   ├── avl_tree.py       # From tree/avl/avl.py
│   │   ├── red_black_tree.py # From tree/red_black_tree/
│   │   ├── trie.py           # From tree/trie/trie.py
│   │   ├── segment_tree.py   # From tree/segment_tree/
│   │   └── fenwick_tree.py   # From tree/fenwick_tree/
│   ├── heaps/
│   │   ├── __init__.py
│   │   ├── binary_heap.py    # From heap/binary_heap.py
│   │   └── priority_queue.py # From queues/priority_queue.py
│   ├── graphs/
│   │   ├── __init__.py
│   │   └── graph.py          # From graph/graph.py (Node, DirectedEdge, DirectedGraph)
│   ├── sets/
│   │   ├── __init__.py
│   │   └── union_find.py     # CONSOLIDATED from unionfind/ and graph/minimum_spanning_tree.py
│   └── hashtables/
│       ├── __init__.py
│       ├── hash_table.py     # From map/hashtable.py
│       └── separate_chaining.py  # From map/separate_chaining_hashtable.py
│
└── algorithms/              # Keep focused on algorithms only
    ├── __init__.py
    ├── array/               # Rename from 'arrays' for consistency
    │   └── [includes k_closest_points, merge_sorted_k_lists, skyline, sliding_window_max from heap/]
    ├── sorting/             # Rename from 'sort'
    ├── searching/           # Rename from 'search'
    ├── graph/               # EXPANDED: includes BFS/DFS graph algorithms
    │   ├── count_islands_bfs.py     # From bfs/
    │   ├── count_islands_dfs.py     # From dfs/
    │   ├── maze_search_bfs.py       # From bfs/
    │   ├── maze_search_dfs.py       # From dfs/
    │   ├── [existing graph algorithms]
    │   └── nearest_neighbor.py      # From ml/ (if keeping)
    ├── tree/                # Tree algorithms
    │   ├── binary_search_tree/      # BST-specific algorithms
    │   ├── trie/                    # Trie-specific algorithms
    │   ├── traversal/               # Keep as-is
    │   └── [general tree algorithms]
    ├── string/              # Rename from 'strings'
    ├── dynamic_programming/ # Rename from 'dp' for clarity
    ├── greedy/
    ├── backtracking/        # Rename from 'backtrack'
    │   └── sudoku_solver.py         # From dfs/
    ├── bit_manipulation/    # Rename from 'bit'
    ├── math/                # Rename from 'maths'
    │   ├── statistics/              # From distribution/
    │   └── all_factors.py           # From dfs/
    ├── compression/
    ├── streaming/           # Keep as distinct category (not misc)
    └── automata/            # Keep as distinct category
```

**Key Changes from Original Plan**:
1. ✅ Union-Find consolidated (no separate disjoint_set.py)
2. ✅ BFS/DFS algorithms merged into `graph/` with technique suffixes
3. ✅ Heap algorithms moved to `array/` or appropriate categories
4. ✅ Tree structure properly separated (data structures vs algorithms)
5. ✅ Priority queue moved to `data_structures/heaps/`
6. ✅ Distribution moved to `math/statistics/`
7. ✅ Streaming and automata kept as distinct categories (not misc)
8. ✅ ML module algorithms moved to appropriate categories

### 2.2 Naming Convention Improvements

**Changes**:
- `arrays` → `array` (singular, consistent)
- `strings` → `string` (singular, consistent)
- `dp` → `dynamic_programming` (explicit, readable)
- `maths` → `math` (standard Python naming)
- `backtrack` → `backtracking` (complete word)
- `bit` → `bit_manipulation` (explicit)
- `sort` → `sorting` (consistent with gerund form)
- `search` → `searching` (consistent with gerund form)
- `linkedlist` → `linked_list` (snake_case consistency)
- `unionfind` → `union_find` (snake_case consistency)
- `bfs` → merged into `graph/` (technique, not category)
- `dfs` → merged into `graph/` (technique, not category)
- `heap` → split between `data_structures/heaps/` and `algorithms/array/`
- `map` → `hashtables` (clearer naming)
- `queues` → split between `data_structures/linear/` and `data_structures/heaps/`

**Impact**: This affects imports throughout the codebase. See Section 8 for migration strategy.

---

## 3. Code Quality Improvements

### 3.1 Python Version Strategy and Deprecation

**Current Support** (as of 0.1.4):
- `setup.py`: Python 3.4, 3.5, 3.6, 3.7
- `tox.ini`: Python 3.5, 3.6, 3.7
- `.travis.yml`: Python 3.6, 3.7

**Proposed Target**: Python 3.8+ (drop 3.4, 3.5, 3.6, 3.7 support)

**Rationale**:
- Python 3.4: EOL March 2019
- Python 3.5: EOL September 2020
- Python 3.6: EOL December 2021
- Python 3.7: EOL June 2023
- Python 3.8: Introduced in October 2019, has walrus operator, positional-only parameters
- Python 3.8 is the minimum version for many modern features we want to use

**Deprecation Timeline**:
1. **v0.2.0** (this refactor):
   - Update `pyproject.toml` to require `python>=3.8`
   - Add prominent notice in README
   - Add DeprecationWarning for Python < 3.8 in `__init__.py`
   - Document in MIGRATION.md
   
2. **Communication**:
   - PyPI package description update
   - GitHub release notes highlighting breaking change
   - Update README badges to show Python 3.8+
   - Consider maintaining a `0.1.x` branch for critical bug fixes (6-12 months)

**Migration Path for Users**:
```markdown
# In MIGRATION.md
## Python Version Support

### If you need Python 3.5-3.7:
- Stay on v0.1.x (`pip install algorithms<0.2`)
- Security and critical bug fixes will be backported for 6 months

### Upgrading to v0.2.0+:
- Requires Python 3.8 or higher
- Use `pyenv` or system package manager to upgrade Python
- Test your code with Python 3.8+ before upgrading algorithms package
```

### 3.2 Modern Python Standards

**Target Python Version**: 3.8+ (drop 3.5, 3.6, 3.7 support)

**Improvements**:

1. **Type Hints** (PEP 484, 563, 585):
   ```python
   # BEFORE
   def two_sum(array, target):
       dic = {}
       # ...
   
   # AFTER (Python 3.8+)
   from typing import Optional
   
   def two_sum(array: list[int], target: int) -> Optional[tuple[int, int]]:
       """Find two numbers that sum to target.
       
       Args:
           array: List of integers to search
           target: Target sum value
           
       Returns:
           Tuple of indices if found, None otherwise
           
       Examples:
           >>> two_sum([2, 7, 11, 15], 9)
           (0, 1)
       """
       seen: dict[int, int] = {}
       # ...
   ```

   **Note**: Use lowercase `list`, `dict`, `tuple` instead of `List`, `Dict`, `Tuple` from typing (PEP 585, Python 3.9+, but backported in `from __future__ import annotations` for 3.8)

2. **Dataclasses** for data structures:
   ```python
   # BEFORE
   class TreeNode:
       def __init__(self, val=0):
           self.val = val
           self.left = None
           self.right = None
   
   # AFTER
   from dataclasses import dataclass
   from typing import Optional
   
   @dataclass
   class TreeNode:
       val: int = 0
       left: Optional['TreeNode'] = None
       right: Optional['TreeNode'] = None
   ```

3. **f-strings** everywhere (replace `.format()` and `%`):
   ```python
   # BEFORE
   return f"({self.source} -> {self.target})"  # Already good
   
   # Make consistent across all files
   ```

4. **Pathlib** for unix path operations:
   ```python
   # In unix/ modules, use pathlib.Path instead of string operations
   from pathlib import Path
   ```

5. **Protocols and ABCs** - Use typing.Protocol for structural subtyping where appropriate

### 3.3 Wildcard Import Elimination Strategy

**Current Issue**: Almost every `__init__.py` uses `from .module import *` (35+ files)

**Impact**: Unclear what's exported, harder to maintain, potential naming conflicts

**Automated Conversion Strategy**:

1. **Create Audit Script** (`tools/audit_exports.py`):
   ```python
   """Scan all __init__.py files and catalog what needs __all__."""
   import ast
   from pathlib import Path
   
   def find_wildcard_imports(file_path):
       """Find all wildcard imports in a file."""
       # Parse AST and find ImportFrom nodes with '*'
       ...
   
   def extract_public_names(module_path):
       """Extract all public (non-_prefixed) names from a module."""
       ...
   
   def generate_explicit_init(module_dir):
       """Generate explicit __init__.py with __all__."""
       ...
   ```

2. **Conversion Process** (per module):
   ```bash
   # Step 1: Generate explicit imports
   python tools/convert_init.py algorithms/array/
   
   # Step 2: Verify tests still pass
   pytest tests/test_array.py
   
   # Step 3: Manual review and commit
   git diff algorithms/array/__init__.py
   ```

3. **Example Conversion**:
   ```python
   # BEFORE (algorithms/array/__init__.py)
   from .delete_nth import *
   from .flatten import *
   from .two_sum import *
   # ... 17 more wildcard imports
   
   # AFTER
   """Array manipulation algorithms."""
   
   from .delete_nth import delete_nth, delete_nth_naive
   from .flatten import flatten, flatten_iter
   from .two_sum import two_sum
   # ... explicit imports
   
   __all__ = [
       # Deletion
       'delete_nth',
       'delete_nth_naive',
       # Flattening
       'flatten',
       'flatten_iter',
       # Two Sum
       'two_sum',
       # ... (organized by category)
   ]
   ```

**Priority Order**:
1. Data structures modules (simpler, fewer dependencies)
2. Algorithm modules (more complex, more interdependencies)
3. Test files (update imports after modules are done)

---

## 4. Testing Infrastructure Modernization

### 4.1 Test Organization and Migration Strategy

**Current State**:
- Tests in `tests/test_array.py`, `tests/test_sort.py`, etc.
- Mix of unittest and pytest syntax
- Tests import from `algorithms.arrays`, `algorithms.sort`, etc.
- ~30+ test files with hundreds of import statements

**Proposed New Structure**:
```
tests/
├── conftest.py              # Shared fixtures
├── unit/
│   ├── data_structures/
│   │   ├── test_linked_list.py
│   │   ├── test_stack.py
│   │   ├── test_queue.py
│   │   ├── test_binary_heap.py
│   │   ├── test_binary_search_tree.py
│   │   ├── test_union_find.py
│   │   └── ...
│   └── algorithms/
│       ├── test_array.py
│       ├── test_sorting.py
│       ├── test_searching.py
│       ├── test_graph.py
│       ├── test_tree.py
│       └── ...
└── integration/
    └── test_graph_algorithms_integration.py
```

**Migration Strategy**:

1. **Phase 1: Create Import Compatibility Layer** (do this FIRST)
   ```python
   # algorithms/__init__.py
   """Algorithms package (with backward compatibility shims)."""
   from importlib import import_module as _import_module
   import warnings as _warnings
   
   _DEPRECATED_MODULES = {
       'arrays': 'algorithms.array',
       'sort': 'algorithms.sorting',
       'search': 'algorithms.searching',
       'dp': 'algorithms.dynamic_programming',
       'maths': 'algorithms.math',
       'bit': 'algorithms.bit_manipulation',
       'backtrack': 'algorithms.backtracking',
       'bfs': 'algorithms.graph',   # technique modules
       'dfs': 'algorithms.graph',
       # ... complete mapping
   }
   
   _DEPRECATED_FUNCTIONS = {
       # Allow module-level access, e.g. `from algorithms import two_sum`
       'two_sum': ('algorithms.array', 'two_sum'),
       'merge_sort': ('algorithms.sorting', 'merge_sort'),
       # Populate from Phase 0 catalog
   }
   
   def _warn(message: str) -> None:
       _warnings.warn(message, DeprecationWarning, stacklevel=2)
   
   def __getattr__(name: str):
       """Handle deprecated module and function lookups."""
       if name in _DEPRECATED_MODULES:
           target = _DEPRECATED_MODULES[name]
           _warn(
               f"Importing '{name}' from algorithms is deprecated. "
               f"Use 'from {target} import ...' instead."
           )
           return _import_module(target)
       
       if name in _DEPRECATED_FUNCTIONS:
           module_name, attr = _DEPRECATED_FUNCTIONS[name]
           _warn(
               f"Importing '{name}' from algorithms is deprecated. "
               f"Use 'from {module_name} import {attr}' instead."
           )
           module = _import_module(module_name)
           return getattr(module, attr)
       
       raise AttributeError(f"module 'algorithms' has no attribute '{name}'")
   
   # Re-export deprecated modules & functions for dir()/help()
   globals().update({
       alias: _import_module(real)
       for alias, real in _DEPRECATED_MODULES.items()
   })
   for alias, (module_name, attr) in _DEPRECATED_FUNCTIONS.items():
       globals()[alias] = getattr(_import_module(module_name), attr)
   ```

   **Module-level import guarantee**: The `_DEPRECATED_FUNCTIONS` mapping enumerates all public APIs that historically supported `from algorithms import foo`. Populate it from `MODULE_CATALOG.md` so existing tutorials that rely on module-level exports keep working (with warnings) until v0.4.0.

2. **Phase 2: Create Test Migration Script** (`tools/migrate_test_imports.py`):
   ```python
   """Automatically update test imports to new structure."""
   import re
   from pathlib import Path
   
   IMPORT_MAPPING = {
       'from algorithms.arrays import': 'from algorithms.array import',
       'from algorithms.sort import': 'from algorithms.sorting import',
       'from algorithms.dp import': 'from algorithms.dynamic_programming import',
       'from algorithms.maths import': 'from algorithms.math import',
       'from algorithms.bfs import': 'from algorithms.graph import',
       'from algorithms.dfs import': 'from algorithms.graph import',
       # ... complete mapping
   }
   
   RENAME_MAPPING = {
       'algorithms.arrays': 'algorithms.array',
       'algorithms.sort': 'algorithms.sorting',
       # ...
   }
   
   def migrate_file(filepath: Path) -> tuple[int, list[str]]:
       """Migrate imports in a single file."""
       content = filepath.read_text()
       changes = []
       change_count = 0
       
       for old, new in IMPORT_MAPPING.items():
           if old in content:
               content = content.replace(old, new)
               changes.append(f"  {old} → {new}")
               change_count += 1
       
       filepath.write_text(content)
       return change_count, changes
   
   def migrate_all_tests():
       """Migrate all test files."""
       test_dir = Path('tests')
       for test_file in test_dir.glob('test_*.py'):
           count, changes = migrate_file(test_file)
           if count > 0:
               print(f"✓ {test_file.name}: {count} imports updated")
               for change in changes:
                   print(change)
   ```

3. **Phase 3: Run Migration**:
   ```bash
   # Backup tests
   cp -r tests tests.backup
   
   # Run migration script
   python tools/migrate_test_imports.py
   
   # Run all tests to verify
   pytest tests/ -v
   
   # Manual review of changes
   git diff tests/
   
   # Fix any issues
   # ...
   
   # Commit
   git add tests/
   git commit -m "Migrate test imports to new structure"
   ```

4. **Phase 4: Split and Reorganize Test Files** (after migration works):
   ```bash
   # Split test files into unit/data_structures and unit/algorithms
   mkdir -p tests/unit/data_structures tests/unit/algorithms
   
   # Extract data structure tests from existing files
   python tools/split_tests.py
   ```

**Example Test Migration**:
```python
# BEFORE (tests/test_array.py)
from algorithms.arrays import (
    delete_nth,
    two_sum,
    three_sum,
)

# AFTER
from algorithms.array import (
    delete_nth,
    two_sum,
    three_sum,
)
```

**Testing the Migration**:
1. All existing tests must pass with new imports
2. No functionality changes during migration
3. Compatibility layer catches any missed migrations

### 4.2 Migrate to pytest

1. **Consistent Docstrings** (Google Style):
   ```python
   def merge_sort(arr: List[int]) -> List[int]:
       """Sort array using merge sort algorithm.
       
       Merge sort is a divide-and-conquer algorithm that divides the input
       array into two halves, recursively sorts them, and then merges them.
       
       Args:
           arr: Unsorted list of integers
           
       Returns:
           Sorted list in ascending order
           
       Time Complexity:
           O(n log n) in all cases
           
       Space Complexity:
           O(n) for temporary arrays
           
       Examples:
           >>> merge_sort([3, 1, 4, 1, 5, 9, 2, 6])
           [1, 1, 2, 3, 4, 5, 6, 9]
       """
   ```

2. **Remove commented code**:
   ```python
   # BEFORE (in merge_sort.py)
   # return merge(left, right, arr.copy()) # changed, no need to copy
   # return merged # do not return anything
   
   # AFTER - Remove these comments entirely
   ```

3. **Consistent naming**:
   - Variables: `snake_case`
   - Classes: `PascalCase`
   - Constants: `UPPER_SNAKE_CASE`
   - Private: `_leading_underscore`

4. **Avoid wildcard imports**:
   ```python
   # BEFORE (in __init__.py)
   from .delete_nth import *
   from .flatten import *
   
   # AFTER
   from .delete_nth import delete_nth, delete_nth_naive
   from .flatten import flatten, flatten_iter
   
   __all__ = [
       'delete_nth',
       'delete_nth_naive',
       'flatten',
       'flatten_iter',
   ]
   ```

### 2.3 Fix Common Issues

1. **Dangerous default arguments**:
   ```python
   # BEFORE (in graph.py)
   def __init__(self, load_dict={}):  # Dangerous!
   
   # AFTER
   def __init__(self, load_dict: Optional[dict] = None):
       load_dict = load_dict or {}
   ```

2. **Improve variable names**:
   ```python
   # BEFORE
   dic = {}  # Confusing
   arr = []
   
   # AFTER
   seen = {}     # More descriptive
   numbers = []
   ```

3. **Extract magic numbers**:
   ```python
   # BEFORE
   self.heap = [(0)]  # What is 0?
   
   # AFTER
   HEAP_SENTINEL = 0
   self.heap = [HEAP_SENTINEL]
   ```

---

## 3. Testing Infrastructure Modernization

### 3.1 Migrate to pytest

**Current**: Mix of unittest and pytest
**Target**: Pure pytest with modern fixtures

**Changes**:

1. **Rename test files**:
   ```
   tests/
   ├── test_array.py            # Keep
   ├── test_sorting.py          # Rename from test_sort.py
   ├── test_searching.py        # Rename from test_search.py
   ├── test_dynamic_programming.py  # Rename from test_dp.py
   └── ...
   
   tests/
   ├── unit/                    # NEW: Organize by type
   │   ├── data_structures/
   │   │   ├── test_linked_list.py
   │   │   ├── test_stack.py
   │   │   ├── test_queue.py
   │   │   ├── test_binary_heap.py
   │   │   └── ...
   │   └── algorithms/
   │       ├── test_array.py
   │       ├── test_sorting.py
   │       └── ...
   ├── integration/             # NEW: Integration tests
   │   └── test_graph_algorithms.py
   └── conftest.py              # NEW: Shared fixtures
   ```

2. **Convert unittest to pytest style**:
   ```python
   # BEFORE (unittest style)
   import unittest
   
   class TestTwoSum(unittest.TestCase):
       def test_two_sum(self):
           self.assertTupleEqual((0, 2), two_sum([2, 11, 7, 9], target=9))
           self.assertIsNone(two_sum([-3, 5, 2, 3, 8, -9], target=6))
   
   if __name__ == "__main__":
       unittest.main()
   
   # AFTER (pytest style)
   import pytest
   from algorithms.array import two_sum
   
   
   def test_two_sum_found():
       """Test two_sum when target is found."""
       result = two_sum([2, 11, 7, 9], target=9)
       assert result == (0, 2)
   
   
   def test_two_sum_not_found():
       """Test two_sum when target is not found."""
       result = two_sum([-3, 5, 2, 3, 8, -9], target=6)
       assert result is None
   
   
   @pytest.mark.parametrize("array,target,expected", [
       ([2, 7, 11, 15], 9, (0, 1)),
       ([3, 2, 4], 6, (1, 2)),
       ([3, 3], 6, (0, 1)),
   ])
   def test_two_sum_parametrized(array, target, expected):
       """Test two_sum with multiple inputs."""
       assert two_sum(array, target) == expected
   ```

3. **Add fixtures for common data structures**:
   ```python
   # conftest.py
   import pytest
   
   @pytest.fixture
   def sample_tree():
       """Create a sample binary tree for testing."""
       from algorithms.data_structures.trees import TreeNode
       root = TreeNode(1)
       root.left = TreeNode(2)
       root.right = TreeNode(3)
       return root
   
   @pytest.fixture
   def sample_graph():
       """Create a sample graph for testing."""
       from algorithms.data_structures.graphs import Graph
       graph = Graph()
       graph.add_edge('A', 'B')
       graph.add_edge('B', 'C')
       return graph
   ```

4. **Use pytest marks for organization**:
   ```python
   @pytest.mark.sorting
   @pytest.mark.slow
   def test_merge_sort_large_array():
       """Test merge sort with large array."""
       # ...
   
   @pytest.mark.data_structure
   def test_binary_heap_operations():
       """Test binary heap basic operations."""
       # ...
   ```

### 3.2 Improve Test Coverage

1. **Add property-based testing with hypothesis**:
   ```python
   from hypothesis import given, strategies as st
   
   @given(st.lists(st.integers()))
   def test_sort_is_idempotent(arr):
       """Sorting twice gives same result as sorting once."""
       sorted_once = merge_sort(arr.copy())
       sorted_twice = merge_sort(sorted_once.copy())
       assert sorted_once == sorted_twice
   
   @given(st.lists(st.integers()))
   def test_sort_preserves_length(arr):
       """Sorting preserves array length."""
       assert len(merge_sort(arr)) == len(arr)
   ```

2. **Add edge case tests**:
   ```python
   def test_two_sum_empty_array():
       """Test with empty array."""
       assert two_sum([], 5) is None
   
   def test_two_sum_single_element():
       """Test with single element."""
       assert two_sum([1], 1) is None
   ```

3. **Add performance benchmarks** (optional):
   ```python
   @pytest.mark.benchmark
   def test_merge_sort_performance(benchmark):
       """Benchmark merge sort performance."""
       data = list(range(10000, 0, -1))
       result = benchmark(merge_sort, data)
       assert result == list(range(1, 10001))
   ```

### 3.3 Update Testing Configuration

Create `pyproject.toml` (modern Python standard):

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "algorithms"
version = "0.2.0"
description = "Pythonic Data Structures and Algorithms"
readme = "README.md"
requires-python = ">=3.8"
license = {text = "MIT"}
authors = [
    {name = "Algorithms Team & Contributors", email = "kwk236@gmail.com"}
]
classifiers = [
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "License :: OSI Approved :: MIT License",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "pytest-cov>=4.0",
    "pytest-benchmark>=4.0",
    "hypothesis>=6.0",
    "black>=23.0",
    "ruff>=0.1.0",
    "mypy>=1.0",
]

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = [
    "-v",
    "--strict-markers",
    "--cov=algorithms",
    "--cov=data_structures",
    "--cov-report=html",
    "--cov-report=term-missing",
]
markers = [
    "slow: marks tests as slow",
    "benchmark: performance benchmark tests",
    "data_structure: data structure tests",
    "algorithm: algorithm tests",
    "sorting: sorting algorithm tests",
    "searching: searching algorithm tests",
]

[tool.coverage.run]
source = ["algorithms", "data_structures"]
omit = ["*/tests/*", "*/__init__.py"]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "raise AssertionError",
    "raise NotImplementedError",
    "if __name__ == .__main__.:",
    "if TYPE_CHECKING:",
]

[tool.black]
line-length = 88
target-version = ['py38', 'py39', 'py310', 'py311', 'py312']
include = '\.pyi?$'

[tool.ruff]
line-length = 88
select = [
    "E",   # pycodestyle errors
    "W",   # pycodestyle warnings
    "F",   # pyflakes
    "I",   # isort
    "C90", # mccabe complexity
    "N",   # pep8-naming
    "UP",  # pyupgrade
    "B",   # flake8-bugbear
    "SIM", # flake8-simplify
]
ignore = [
    "E501", # line too long (handled by black)
]

[tool.mypy]
python_version = "3.8"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = false  # Gradually enable
check_untyped_defs = true
```

---

## 4. Package Organization

### 4.1 Improve __init__.py Files

Make imports explicit and organized:

```python
# algorithms/array/__init__.py
"""Array manipulation algorithms."""

from .two_sum import two_sum
from .three_sum import three_sum
from .n_sum import n_sum
from .rotate import rotate
from .move_zeros import move_zeros

__all__ = [
    'two_sum',
    'three_sum',
    'n_sum',
    'rotate',
    'move_zeros',
]
```

### 4.2 Add py.typed for Type Checking

Create `algorithms/py.typed` and `data_structures/py.typed` (empty files) to indicate type hint support.

---

## 5. Documentation Improvements

### 5.1 Enhanced README

Update README.md with:
- Clear distinction between data structures and algorithms
- Modern installation instructions
- Usage examples for both data structures and algorithms
- Contribution guidelines
- Algorithm complexity tables

### 5.2 API Documentation

Add comprehensive module docstrings:

```python
"""
Array Algorithms
================

This module provides common array manipulation algorithms including:
- Two Sum and N-Sum variants
- Array rotation and manipulation
- Interval operations
- Sliding window algorithms

All functions are optimized for time and space complexity.
"""
```

### 5.3 Update Sphinx Documentation

Reorganize docs to reflect new structure:
- Separate sections for data structures and algorithms
- Add complexity analysis tables
- Include visual diagrams (where applicable)

---

## 6. Build and Development Tools

### 6.1 Replace setup.py with pyproject.toml

**Rationale**: PEP 517/518 compliance, modern standard

See section 3.3 for full configuration.

### 6.2 Add Modern Linting and Formatting

**Tools**:
- `black`: Code formatting
- `ruff`: Fast linting (replaces flake8, isort, etc.)
- `mypy`: Type checking

**Configuration** (in pyproject.toml above)

### 6.3 GitHub Actions CI/CD (Replaces Travis CI)

**Issue**: Current `.travis.yml` uses Travis CI, which is deprecated for open source

**Replacement**: GitHub Actions

Create `.github/workflows/test.yml`:

```yaml
name: Tests

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    
    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -e ".[dev]"
    
    - name: Lint with ruff
      run: ruff check .
    
    - name: Format check with black
      run: black --check .
    
    - name: Type check with mypy
      run: mypy algorithms data_structures --config-file pyproject.toml
      continue-on-error: true  # Initially allow failures

  test:
    runs-on: ${{ matrix.os }}
    strategy:
      fail-fast: false
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
        python-version: ['3.8', '3.9', '3.10', '3.11', '3.12']
    
    steps:
    - uses: actions/checkout@v4
    
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v5
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -e ".[dev]"
    
    - name: Test with pytest
      run: |
        pytest tests/ \
          --cov=algorithms \
          --cov=data_structures \
          --cov-report=xml \
          --cov-report=term-missing \
          -v
    
    - name: Upload coverage to Codecov
      if: matrix.os == 'ubuntu-latest' && matrix.python-version == '3.11'
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml
        fail_ci_if_error: false

  docs:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    
    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -e ".[dev]"
        pip install sphinx sphinx-rtd-theme
    
    - name: Build documentation
      run: |
        cd docs
        make html
```

**Migration Steps**:
1. Create `.github/workflows/` directory
2. Add `test.yml` workflow
3. Test locally with `act` (GitHub Actions local runner)
4. Push to feature branch and verify workflows run
5. Update README badges:
   ```markdown
   <!-- OLD -->
   [![Build Status](https://travis-ci.org/keon/algorithms.svg?branch=master)](https://travis-ci.org/keon/algorithms)
   
   <!-- NEW -->
   [![Tests](https://github.com/keon/algorithms/workflows/Tests/badge.svg)](https://github.com/keon/algorithms/actions)
   [![codecov](https://codecov.io/gh/keon/algorithms/branch/main/graph/badge.svg)](https://codecov.io/gh/keon/algorithms)
   ```
6. Remove `.travis.yml` after GitHub Actions is working

### 6.4 Pre-commit Hooks

Create `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.12.0
    hooks:
      - id: black
        language_version: python3.8

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.9
    hooks:
      - id: ruff
        args: [--fix, --exit-non-zero-on-fix]

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.8.0
    hooks:
      - id: mypy
        additional_dependencies: [types-all]

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
```

---

## 7. Implementation Roadmap

### Phase 0: Discovery & Cataloging (Weeks 1-2) **[NEW - CRITICAL]**

**Goal**: Audit the codebase to prevent issues during refactoring

- [ ] **Catalog all data structures vs algorithms**
  ```bash
  python tools/catalog_modules.py > MODULE_CATALOG.md
  ```
  - Identify which files are data structures
  - Identify which files are algorithms
  - Identify files that are neither (utilities, helpers)
  
- [ ] **Find all dangerous default arguments**
  ```bash
  python tools/find_dangerous_defaults.py
  ```
  - Scan for `def __init__(self, param={})` patterns
  - Scan for `def __init__(self, param=[])` patterns
  - Generate fix list

- [ ] **Map all import dependencies**
  ```bash
  python tools/analyze_imports.py --graph
  ```
  - Create dependency graph
  - Identify circular dependencies
  - Identify external vs internal imports
  - Map which tests use which modules

- [ ] **Audit AbstractBase Classes**
  ```bash
  grep -r "ABCMeta\|ABC" algorithms/ --include="*.py"
  ```
  - List all abstract classes
  - Check for consistency in approach
  - Plan migration to `ABC` (new style)

- [ ] **Find all wildcard imports**
  ```bash
  python tools/find_wildcard_imports.py
  ```
  - List all `from X import *`
  - Extract what's actually used
  - Generate __all__ lists

- [ ] **Identify Union-Find implementations**
  - Document differences between `Union` and `DisjointSet`
  - Choose canonical implementation
  - List all files that use Union-Find

- [ ] **Create Phase 0 Report**
  ```
  PHASE_0_REPORT.md:
  - Total files to migrate: X
  - Data structures: Y
  - Algorithms: Z
  - Dangerous defaults found: N
  - Wildcard imports: M
  - Dependencies mapped: ✓
  - Circular dependencies: [list]
  - Risk assessment: [high/medium/low]
  ```

**Deliverables**:
- `MODULE_CATALOG.md` - Complete module categorization
- `DANGEROUS_DEFAULTS.md` - List of fixes needed
- `DEPENDENCY_GRAPH.pdf` - Visual dependency map
- `WILDCARD_AUDIT.md` - All wildcard imports and proposed __all__
- `PHASE_0_REPORT.md` - Summary for decision making

**Tools to Create**:
- `tools/catalog_modules.py` - Module categorization script
- `tools/find_dangerous_defaults.py` - AST-based scanner
- `tools/analyze_imports.py` - Dependency analyzer
- `tools/find_wildcard_imports.py` - Wildcard scanner
- `tools/generate_all_lists.py` - Auto-generate __all__ lists

All scripts live inside this repository under `tools/` (no external packaging). Each script should meet the following spec **before** Phase 0 ends:

| Script | Inputs | Outputs | Example Invocation |
|--------|--------|---------|--------------------|
| `tools/catalog_modules.py` | Optional `--format json\|md` | `MODULE_CATALOG.md` (and `.json`) listing path, classification (`data_structure` / `algorithm` / `utility`), LOC, dependencies | `python tools/catalog_modules.py --format md > MODULE_CATALOG.md` |
| `tools/find_dangerous_defaults.py` | Path glob (default `algorithms/`) | `DANGEROUS_DEFAULTS.md` with file, line, signature, suggested fix | `python tools/find_dangerous_defaults.py algorithms/ data_structures/` |
| `tools/analyze_imports.py` | `--graph` flag, optional `--output graph.json` | `DEPENDENCY_GRAPH.json` + rendered `DEPENDENCY_GRAPH.pdf` via `graphviz` | `python tools/analyze_imports.py --graph --output dependency_graph.json` |
| `tools/find_wildcard_imports.py` | None | `WILDCARD_AUDIT.md` summarizing each wildcard import and referenced symbols | `python tools/find_wildcard_imports.py` |
| `tools/generate_all_lists.py` | Module path | Draft `__init__.py` content with explicit imports + `__all__` for review | `python tools/generate_all_lists.py algorithms/array/ > /tmp/array_init.py` |

> **Acceptance Criteria**: Each tool includes usage docs (`--help`), sample output checked into `docs/internal/phase0/`, and is covered by at least smoke tests (run via `python -m pytest tools/tests`).

**Decision Points After Phase 0**:
1. Confirm/adjust Phase 1-6 timeline based on findings
2. Identify any showstoppers or high-risk areas
3. Prioritize which modules to refactor first (low-risk to high-risk)
4. Adjust resource allocation if needed

### Phase 1: Foundation (Weeks 3-4)
- [ ] Set up pyproject.toml
- [ ] Configure pytest, black, ruff, mypy
- [ ] Set up GitHub Actions
- [ ] Add pre-commit hooks
- [ ] Create new directory structure (don't move files yet)

### Phase 2: Data Structures Migration (Weeks 5-7)

**Goal**: Create the data_structures package and migrate all data structures

- [ ] **Create data_structures package structure**
  ```bash
  mkdir -p data_structures/{linear,trees,heaps,graphs,sets,hashtables}
  ```

- [ ] **Consolidate Union-Find** (Priority 1 - has duplicates)
  - [ ] Create `data_structures/sets/union_find.py` with unified implementation
  - [ ] Add `Union` and `DisjointSet` as deprecated aliases
  - [ ] Update `algorithms/unionfind/count_islands.py` to use new Union-Find
  - [ ] Update `algorithms/graph/minimum_spanning_tree.py` to use new Union-Find
  - [ ] Test both use cases
  - [ ] Add deprecation warnings to old locations

- [ ] **Migrate linear structures**
  - [ ] Create complete `linked_list.py` (not just nodes)
  - [ ] Move `stack.py` from stack/
  - [ ] Move `queue.py` from queues/
  - [ ] Update all imports in algorithms that use these
  - [ ] Update tests

- [ ] **Migrate tree structures** (Complex - follow Section 1.4 plan)
  - [ ] Create `tree_node.py` (base TreeNode from tree/tree.py)
  - [ ] Move `binary_search_tree.py` (from tree/bst/bst.py)
    - [ ] Fix Node class conflict (bst.py has own Node)
  - [ ] Move `avl_tree.py` (from tree/avl/avl.py)
    - [ ] Fix import: `from tree.tree import TreeNode` → `from data_structures.trees import TreeNode`
  - [ ] Move `red_black_tree.py`
  - [ ] Move `trie.py`
  - [ ] Move `segment_tree.py`
  - [ ] Move `fenwick_tree.py`
  - [ ] Add type hints to all tree classes
- [ ] Write comprehensive tests for each

- [ ] **Migrate heap structures**
  - [ ] Move `binary_heap.py` from heap/
  - [ ] Move `priority_queue.py` from queues/
  - [ ] Update heap algorithms to import from data_structures
  - [ ] Add type hints
  - [ ] Test

- [ ] **Migrate graph structures**
  - [ ] Move `graph.py` (Node, DirectedEdge, DirectedGraph)
  - [ ] Fix dangerous default: `__init__(self, load_dict={})`
  - [ ] Add type hints
  - [ ] Update all graph algorithms to use new import
  - [ ] Test

- [ ] **Migrate hashtables**
  - [ ] Move `hashtable.py` from map/
  - [ ] Move `separate_chaining_hashtable.py` from map/
  - [ ] Keep map algorithms (is_anagram, etc.) in algorithms/
  - [ ] Test

- [ ] **Add py.typed markers**
  ```bash
  touch data_structures/py.typed
  ```

**Validation**:
- [ ] All data structure tests pass
- [ ] No circular imports
- [ ] Type checking passes (mypy)
- [ ] Documentation generated correctly

### Phase 3: Core Algorithms Refactoring (Weeks 8-10)

**Goal**: Refactor and modernize core algorithm modules

- [ ] **Refactor array algorithms**
  - [ ] Rename `algorithms/arrays/` → `algorithms/array/`
  - [ ] Add type hints to all functions
  - [ ] Convert wildcard imports to explicit
  - [ ] Move heap-based algorithms from `heap/`:
    - [ ] `k_closest_points.py`
    - [ ] `merge_sorted_k_lists.py`
    - [ ] `skyline.py`
    - [ ] `sliding_window_max.py`
  - [ ] Update tests
  - [ ] Add complexity documentation

- [ ] **Refactor sorting algorithms**
  - [ ] Rename `algorithms/sort/` → `algorithms/sorting/`
  - [ ] Add type hints
  - [ ] Remove commented code
  - [ ] Update docstrings with complexity
  - [ ] Migrate tests to `tests/unit/algorithms/test_sorting.py`

- [ ] **Refactor searching algorithms**
  - [ ] Rename `algorithms/search/` → `algorithms/searching/`
  - [ ] Add type hints
  - [ ] Update tests

- [ ] **Refactor string algorithms**
  - [ ] Rename `algorithms/strings/` → `algorithms/string/`
  - [ ] Add type hints
  - [ ] Update tests

- [ ] **Refactor dynamic programming**
  - [ ] Rename `algorithms/dp/` → `algorithms/dynamic_programming/`
  - [ ] Add type hints
  - [ ] Enhanced docstrings with DP patterns
  - [ ] Update tests

- [ ] **Create test migration scripts** (see Section 4.1)
  - [ ] `tools/migrate_test_imports.py`
  - [ ] Run migration on all test files
  - [ ] Verify all tests pass

### Phase 4: Graph & Tree Algorithms (Weeks 11-13)

**Goal**: Reorganize graph and tree algorithms, merge BFS/DFS

- [ ] **Merge BFS algorithms into graph/** (see Section 1.2)
  - [ ] Rename `bfs/count_islands.py` → `graph/count_islands_bfs.py`
  - [ ] Rename `bfs/maze_search.py` → `graph/maze_search_bfs.py`
  - [ ] Move `bfs/shortest_distance_from_all_buildings.py` → `graph/`
  - [ ] Move `bfs/word_ladder.py` → `graph/`
  - [ ] Keep `algorithms/bfs/__init__.py` for compatibility (with deprecation)
  - [ ] Update all imports

- [ ] **Merge DFS algorithms appropriately** (see Section 1.2)
  - [ ] Rename `dfs/count_islands.py` → `graph/count_islands_dfs.py`
  - [ ] Rename `dfs/maze_search.py` → `graph/maze_search_dfs.py`
  - [ ] Move `dfs/pacific_atlantic.py` → `graph/`
  - [ ] Move `dfs/walls_and_gates.py` → `graph/`
  - [ ] Move `dfs/sudoku_solver.py` → `backtracking/`
  - [ ] Move `dfs/all_factors.py` → `math/`
  - [ ] Keep `algorithms/dfs/__init__.py` for compatibility
  - [ ] Update all imports

- [ ] **Refactor graph algorithms**
  - [ ] Update to use `data_structures.graphs.Graph`
  - [ ] Add type hints
  - [ ] Consolidate dijkstra/bellman_ford/etc.
  - [ ] Enhanced documentation
  - [ ] Update tests

- [ ] **Reorganize tree algorithms** (see Section 1.4)
  - [ ] Create `algorithms/tree/binary_search_tree/` subdirectory
  - [ ] Move BST algorithms from `tree/bst/` (except bst.py which moved to data_structures)
  - [ ] Create `algorithms/tree/trie/` for trie algorithms
  - [ ] Keep `algorithms/tree/traversal/` as-is
  - [ ] Move general tree algorithms to `algorithms/tree/`
  - [ ] Update all imports to use `data_structures.trees` for tree structures
  - [ ] Add type hints
  - [ ] Update tests

- [ ] **Comprehensive testing**
  - [ ] All graph algorithm tests pass
  - [ ] All tree algorithm tests pass
  - [ ] BFS/DFS compatibility layer works
  - [ ] No import errors

### Phase 5: Specialized Modules & Final Cleanup (Weeks 14-15)

**Goal**: Handle remaining modules and finalize refactoring

- [ ] **Refactor backtracking algorithms**
  - [ ] Rename `algorithms/backtrack/` → `algorithms/backtracking/`
  - [ ] Include `sudoku_solver.py` from dfs/
  - [ ] Add type hints
  - [ ] Update tests

- [ ] **Refactor greedy algorithms**
  - [ ] Add type hints
  - [ ] Enhanced documentation
  - [ ] Update tests

- [ ] **Refactor bit manipulation**
  - [ ] Rename `algorithms/bit/` → `algorithms/bit_manipulation/`
  - [ ] Add type hints
  - [ ] Update tests

- [ ] **Refactor math algorithms** (see Section 1.5)
  - [ ] Rename `algorithms/maths/` → `algorithms/math/`
  - [ ] Move `distribution/histogram.py` → `math/statistics/`
  - [ ] Move `dfs/all_factors.py` → `math/`
  - [ ] Add type hints
  - [ ] Update tests

- [ ] **Handle compression algorithms**
  - [ ] Keep as `algorithms/compression/`
  - [ ] Add type hints
  - [ ] Update tests

- [ ] **Handle streaming algorithms** (NOT misc - valid category)
  - [ ] Keep as `algorithms/streaming/`
  - [ ] Add comprehensive documentation explaining streaming algorithm concepts
  - [ ] Add type hints
  - [ ] Update tests

- [ ] **Handle automata** (NOT misc - valid category)
  - [ ] Keep as `algorithms/automata/`
  - [ ] Add type hints
  - [ ] Update tests

- [ ] **Handle ML module** (see Section 1.5)
  - [ ] Decision: Move `ml/nearest_neighbor.py` → `graph/nearest_neighbor.py`
  - [ ] Remove `ml/` module (out of scope for algorithms library)
  - [ ] Update tests

- [ ] **Handle unix module** (see Section 1.5)
  - [ ] Decision: Remove or create separate `algorithms-utils` package
  - [ ] These are utilities, not algorithms
  - [ ] Document decision in CHANGELOG

- [ ] **Wildcard import elimination** (see Section 3.3)
  - [ ] Run `tools/convert_init.py` on all modules
  - [ ] Manual review of generated __all__ lists
  - [ ] Test each module after conversion

- [ ] **Fix all dangerous defaults**
  - [ ] Apply fixes from `DANGEROUS_DEFAULTS.md` (from Phase 0)
  - [ ] Test each fix

- [ ] **Update all Abstract Base Classes**
  - [ ] Convert `ABCMeta` to `ABC` (new style)
  - [ ] Ensure consistency across all abstract classes
  - [ ] Test

### Phase 6: Documentation, Testing & Release (Weeks 16-17)

**Goal**: Finalize documentation, ensure quality, and release

- [ ] **Complete documentation review**
  - [ ] Update README.md with new structure
  - [ ] Document data_structures vs algorithms separation
  - [ ] Update installation instructions
  - [ ] Add migration guide (MIGRATION.md)
  - [ ] Update CONTRIBUTING.md
  - [ ] Create CHANGELOG.md for v0.2.0

- [ ] **Update Sphinx documentation**
  - [ ] Reorganize API docs to reflect new structure
  - [ ] Add data_structures documentation section
  - [ ] Add algorithms documentation section
  - [ ] Include complexity analysis tables
  - [ ] Add visual diagrams where applicable
  - [ ] Generate and review HTML docs

- [ ] **Ensure backward compatibility**
  - [ ] Test all compatibility layers
  - [ ] Run `tests/test_backward_compatibility.py`
  - [ ] Verify deprecation warnings work correctly
  - [ ] Test automated migration tool

- [ ] **Performance benchmarking**
  - [ ] Ensure no performance regressions
  - [ ] Run benchmark suite on key algorithms
  - [ ] Document any performance changes

- [ ] **Security audit**
  - [ ] Run `bandit` for security issues
  - [ ] Check for injection vulnerabilities
  - [ ] Review use of `eval()`, `exec()`, `pickle`
  - [ ] Check for hardcoded secrets

- [ ] **Final validation**
  - [ ] All tests pass on Python 3.8-3.12
  - [ ] All tests pass on Linux, macOS, Windows
  - [ ] Test coverage >90%
  - [ ] Type checking passes (mypy)
  - [ ] Linting passes (ruff, black)
  - [ ] Documentation builds successfully
  - [ ] Installation works via pip

- [ ] **Prepare release**
  - [ ] Update version to 0.2.0 in pyproject.toml
  - [ ] Create release notes
  - [ ] Tag release in git
  - [ ] Build distribution packages
  - [ ] Test package installation from test.pypi.org
  - [ ] Publish to PyPI
  - [ ] Create GitHub release
  - [ ] Announcement blog post/tweet
  - [ ] Update project badges in README

- [ ] **Post-release monitoring**
  - [ ] Monitor GitHub issues for migration problems
  - [ ] Update FAQ with common questions
  - [ ] Provide support for early adopters
  - [ ] Plan v0.2.1 with bug fixes if needed

---

## 10. Updated Timeline Summary

**Total Duration**: 17 weeks (~4 months)

| Phase | Duration | Weeks | Key Deliverables |
|-------|----------|-------|------------------|
| **Phase 0** | 2 weeks | 1-2 | Discovery, cataloging, tooling |
| **Phase 1** | 2 weeks | 3-4 | Foundation, build system, CI/CD |
| **Phase 2** | 3 weeks | 5-7 | Data structures migration |
| **Phase 3** | 3 weeks | 8-10 | Core algorithms refactoring |
| **Phase 4** | 3 weeks | 11-13 | Graph/Tree algorithms, BFS/DFS merge |
| **Phase 5** | 2 weeks | 14-15 | Specialized modules, cleanup |
| **Phase 6** | 2 weeks | 16-17 | Documentation, testing, release |

**Updated from original**: Added Phase 0 (discovery), increased Phase 2-4 duration to account for complexity

**Recommended Team Size**: 2-3 developers
**Priority**: High (technical debt reduction, improved maintainability)

**Critical Path**:
1. Phase 0 must complete before any migration (risk mitigation)
2. Phase 1 tools must work before Phase 2 (build system dependency)
3. Phase 2 must complete before Phase 3-4 (data structures used by algorithms)
4. Phase 3-4 can partially overlap (different modules)
5. Phase 5 depends on Phase 2-4 completion
6. Phase 6 requires all previous phases complete

### Phase Dependencies & Contingencies

- **Phase 0 exit criteria**: No work may start on Phase 2 until the Phase 0 report explicitly states (a) number of circular dependencies and (b) mitigation plan. If blockers surface (e.g., import cycles that require design changes), pause the schedule and create RFCs before moving forward.
- **Buffer**: Reserve 1 spare week after Phase 2 and Phase 4 for remediation. If unused, pull Phase 5 forward; if Phase 0 uncovers large surprises, consume these buffers first instead of cutting scope.
- **Feature flags**: For risky moves (BFS/DFS merger, Union-Find consolidation), land behind compatibility shims so partial progress can ship without breaking `main`.
- **Go/No-go checkpoints**: At the end of Phases 2, 4, and 6 hold review meetings to validate readiness for the next stage; if acceptance criteria aren’t met, either extend the phase or deliberately defer work to v0.3.0.

---

## 8. Backward Compatibility Strategy

### 8.1 Enhanced Deprecation Approach

**Challenge**: The original `__getattr__` approach has limitations:
- Only works for module-level imports
- Doesn't support `from algorithms.arrays import *`
- Performance overhead on every import

**Enhanced Multi-Layer Strategy**:

#### Layer 1: Module-Level Re-exports (Primary Method)

```python
# algorithms/__init__.py
"""
Algorithms package.

This version provides backward compatibility with 0.1.x imports
while migrating to the new structure.
"""
import warnings

# Explicit re-exports for backward compatibility
# These allow "from algorithms import arrays" to work
from algorithms import array as arrays  # OLD name → NEW module
from algorithms import sorting as sort
from algorithms import searching as search
from algorithms import dynamic_programming as dp
from algorithms import math as maths
from algorithms import backtracking as backtrack
from algorithms import bit_manipulation as bit
from algorithms import string as strings

# For data structures that moved
from data_structures.linear import linked_list as linkedlist
from data_structures.heaps import binary_heap as heap_module
from data_structures.sets import union_find as unionfind
from data_structures.hashtables import hash_table as map_module

# Issue deprecation warning on first import
_warned = False
if not _warned:
    warnings.warn(
        "Importing from the old module structure is deprecated. "
        "Please update your imports:\n"
        "  OLD: from algorithms.arrays import two_sum\n"
        "  NEW: from algorithms.array import two_sum\n"
        "See MIGRATION.md for details.",
        DeprecationWarning,
        stacklevel=2
    )
    _warned = True

__all__ = [
    # Old names (deprecated)
    'arrays', 'sort', 'search', 'dp', 'maths', 'backtrack', 'bit', 'strings',
    'linkedlist', 'heap_module', 'unionfind', 'map_module',
    # New names
    'array', 'sorting', 'searching', 'dynamic_programming', 'math',
    'backtracking', 'bit_manipulation', 'string',
]
```

#### Layer 2: Individual Module Compatibility

For complex cases like BFS/DFS merger:

```python
# algorithms/bfs/__init__.py (kept for compatibility)
"""
BFS algorithms - DEPRECATED.

This module is deprecated. BFS algorithms have been moved to algorithms.graph.
"""
import warnings

warnings.warn(
    "algorithms.bfs is deprecated. Import from algorithms.graph instead:\n"
    "  OLD: from algorithms.bfs import count_islands\n"
    "  NEW: from algorithms.graph import count_islands_bfs",
    DeprecationWarning,
    stacklevel=2
)

# Re-export with old names
from algorithms.graph import (
    count_islands_bfs as count_islands,
    maze_search_bfs as maze_search,
    shortest_distance_from_all_buildings,
    word_ladder,
)

__all__ = [
    'count_islands',
    'maze_search',
    'shortest_distance_from_all_buildings',
    'word_ladder',
]
```

#### Layer 3: Dynamic __getattr__ (Fallback)

```python
# algorithms/__init__.py (additional fallback)

def __getattr__(name):
    """Provide fallback for missed imports."""
    # More complex mappings that can't be handled by re-exports
    special_mappings = {
        'Node': ('data_structures.graphs', 'Node'),
        'TreeNode': ('data_structures.trees', 'TreeNode'),
        'BinaryHeap': ('data_structures.heaps', 'BinaryHeap'),
    }
    
    if name in special_mappings:
        module_path, attr_name = special_mappings[name]
        warnings.warn(
            f"Importing {name} from 'algorithms' is deprecated. "
            f"Use 'from {module_path} import {attr_name}' instead.",
            DeprecationWarning,
            stacklevel=2
        )
        module = __import__(module_path, fromlist=[attr_name])
        return getattr(module, attr_name)
    
    raise AttributeError(f"module 'algorithms' has no attribute '{name}'")
```

### 8.2 Migration Testing Strategy

**Create Compatibility Test Suite** (`tests/test_backward_compatibility.py`):

```python
"""Test that old import paths still work (with warnings)."""
import pytest
import warnings

class TestBackwardCompatibility:
    """Ensure old imports work but issue deprecation warnings."""
    
    def test_arrays_import(self):
        """Test that 'algorithms.arrays' still works."""
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
from algorithms.arrays import two_sum
            assert len(w) == 1
            assert issubclass(w[0].category, DeprecationWarning)
            assert callable(two_sum)
    
    def test_sort_import(self):
        """Test that 'algorithms.sort' still works."""
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
from algorithms.sort import merge_sort
            assert len(w) == 1
            assert issubclass(w[0].category, DeprecationWarning)
            assert callable(merge_sort)
    
    def test_bfs_import(self):
        """Test that 'algorithms.bfs' still works."""
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            from algorithms.bfs import count_islands
            assert len(w) == 1
            assert issubclass(w[0].category, DeprecationWarning)
            assert callable(count_islands)
    
    # ... more tests for each deprecated import path
```

### 8.3 Migration Timeline

| Version | Timeline | Action | Old Imports |
|---------|----------|--------|-------------|
| **0.2.0** | Release | New structure + compatibility layer | ✅ Work with DeprecationWarning |
| **0.2.x** | 6-12 months | Bug fixes, encourage migration | ✅ Work with DeprecationWarning |
| **0.3.0** | +12 months | Stronger warnings | ⚠️ Work with FutureWarning + louder logs |
| **0.4.0** | +24 months | Remove compatibility layer | ❌ Raise ImportError |

### 8.4 Migration Guide Template

Create comprehensive `MIGRATION.md`:

```markdown
# Migration Guide: v0.1.x to v0.2.0

## Quick Start

### Automated Migration Tool

A repository-local helper lives at `tools/migrate_imports.py`. Run it directly (no separate PyPI package):

\`\`\`bash
# From the repo root
python tools/migrate_imports.py --path path/to/your/code/
\`\`\`

The tool:
- Updates imports using the mapping in Section 1
- Writes `.bak` backups alongside edited files
- Produces a summary report (`migration_report.json`)

> Tip: commit your work before running the tool so you can review and revert via git if needed.

## Import Path Changes

### Module Renames

| Old Import | New Import | Notes |
|------------|------------|-------|
| `from algorithms.arrays import ...` | `from algorithms.array import ...` | Singular |
| `from algorithms.sort import ...` | `from algorithms.sorting import ...` | Gerund form |
| `from algorithms.dp import ...` | `from algorithms.dynamic_programming import ...` | Explicit |
| `from algorithms.maths import ...` | `from algorithms.math import ...` | Standard naming |

### Data Structure Moves

| Old Import | New Import |
|------------|------------|
| `from algorithms.heap import BinaryHeap` | `from data_structures.heaps import BinaryHeap` |
| `from algorithms.tree.tree import TreeNode` | `from data_structures.trees import TreeNode` |
| `from algorithms.graph.graph import Node` | `from data_structures.graphs import Node` |

### BFS/DFS Merger

| Old Import | New Import |
|------------|------------|
| `from algorithms.bfs import count_islands` | `from algorithms.graph import count_islands_bfs` |
| `from algorithms.dfs import count_islands` | `from algorithms.graph import count_islands_dfs` |

## Python Version

- **Minimum**: Python 3.8+
- **Recommendation**: Python 3.11+ for best performance

If you need Python 3.5-3.7:
\`\`\`bash
pip install "algorithms<0.2"
\`\`\`

## Testing Your Migration

1. Run your test suite with warnings enabled:
   \`\`\`bash
   python -W all -m pytest
   \`\`\`

2. Check for DeprecationWarnings
3. Update imports as suggested
4. Re-run tests

## Timeline

- **v0.2.0-0.2.x**: Old imports work with warnings (12 months)
- **v0.3.0**: Stronger warnings (12 months)
- **v0.4.0**: Old imports stop working

## Need Help?

- GitHub Issues: https://github.com/keon/algorithms/issues
- Migration FAQ: https://github.com/keon/algorithms/wiki/Migration-FAQ
```

---

## 9. Quality Metrics and Goals

### 9.1 Code Coverage
- **Target**: 90%+ test coverage
- **Current**: Unknown (need to measure)
- **Action**: Add coverage reporting to CI

### 9.2 Type Coverage
- **Target**: 100% of public APIs type-hinted
- **Action**: Use mypy with strict mode gradually

### 9.3 Performance
- **Target**: No performance regression vs v0.1.x
- **Action**: Add benchmark suite

### 9.4 Documentation
- **Target**: All public functions documented with examples
- **Current**: Inconsistent
- **Action**: Automated doc coverage check

---

## 10. Specific File Refactoring Examples

### 10.1 Example: Two Sum

**Before** (`algorithms/arrays/two_sum.py`):
```python
"""
Given an array of integers, return indices of the two numbers
such that they add up to a specific target.
"""

def two_sum(array, target):
    dic = {}
    for i, num in enumerate(array):
        if num in dic:
            return dic[num], i
        else:
            dic[target - num] = i
    return None
```

**After** (`algorithms/array/two_sum.py`):
```python
"""Two Sum problem solver.

Given an array of integers, finds two numbers that add up to a specific target.
"""

from typing import List, Optional, Tuple


def two_sum(array: List[int], target: int) -> Optional[Tuple[int, int]]:
    """Find indices of two numbers that sum to target.
    
    Args:
        array: List of integers to search
        target: Target sum to find
        
    Returns:
        Tuple of (index1, index2) if found, None otherwise.
        Guarantees index1 < index2.
        
    Time Complexity:
        O(n) where n is the length of array
        
    Space Complexity:
        O(n) for the hash map
        
    Examples:
        >>> two_sum([2, 7, 11, 15], 9)
        (0, 1)
        >>> two_sum([3, 2, 4], 6)
        (1, 2)
        >>> two_sum([3, 3], 6)
        (0, 1)
        >>> two_sum([1, 2, 3], 10)
        None
    """
    seen: dict[int, int] = {}
    
    for i, num in enumerate(array):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i
    
    return None
```

### 10.2 Example: Binary Heap

**Before** (`algorithms/heap/binary_heap.py`): See earlier reading

**After** (`data_structures/heaps/binary_heap.py`):
```python
"""Binary heap implementation.

A binary heap is a complete binary tree where each node is smaller (min heap)
or larger (max heap) than its children.
"""

from abc import ABC, abstractmethod
from typing import Generic, List, Optional, TypeVar

T = TypeVar('T')


class AbstractHeap(ABC, Generic[T]):
    """Abstract base class for heap implementations."""
    
    @abstractmethod
    def insert(self, value: T) -> None:
        """Insert a value into the heap."""
        
    @abstractmethod
    def extract_min(self) -> T:
        """Remove and return the minimum element."""
        
    @abstractmethod
    def peek(self) -> T:
        """Return the minimum element without removing it."""
        
    @abstractmethod
    def __len__(self) -> int:
        """Return the number of elements in the heap."""
        
    def is_empty(self) -> bool:
        """Check if heap is empty."""
        return len(self) == 0


class MinHeap(AbstractHeap[T]):
    """Min heap implementation using an array.
    
    The heap is stored as a list where for any element at index i:
    - Parent is at index (i - 1) // 2
    - Left child is at index 2 * i + 1
    - Right child is at index 2 * i + 2
    
    Examples:
        >>> heap = MinHeap()
        >>> heap.insert(5)
        >>> heap.insert(3)
        >>> heap.insert(7)
        >>> heap.peek()
        3
        >>> heap.extract_min()
        3
        >>> heap.peek()
        5
    """
    
    def __init__(self) -> None:
        """Initialize an empty min heap."""
        self._heap: List[T] = []
    
    def __len__(self) -> int:
        """Return the number of elements in the heap."""
        return len(self._heap)
    
    def __repr__(self) -> str:
        """Return string representation of the heap."""
        return f"MinHeap({self._heap})"
    
    def insert(self, value: T) -> None:
        """Insert a value into the heap.
        
        Time Complexity: O(log n)
        """
        self._heap.append(value)
        self._bubble_up(len(self._heap) - 1)
    
    def extract_min(self) -> T:
        """Remove and return the minimum element.
        
        Time Complexity: O(log n)
        
        Raises:
            IndexError: If heap is empty
        """
        if self.is_empty():
            raise IndexError("extract_min from empty heap")
        
        min_value = self._heap[0]
        last_value = self._heap.pop()
        
        if not self.is_empty():
            self._heap[0] = last_value
            self._bubble_down(0)
        
        return min_value
    
    def peek(self) -> T:
        """Return the minimum element without removing it.
        
        Time Complexity: O(1)
        
        Raises:
            IndexError: If heap is empty
        """
        if self.is_empty():
            raise IndexError("peek from empty heap")
        return self._heap[0]
    
    def _bubble_up(self, index: int) -> None:
        """Restore heap property by moving element up."""
        while index > 0:
            parent_index = (index - 1) // 2
            if self._heap[index] < self._heap[parent_index]:
                self._swap(index, parent_index)
                index = parent_index
            else:
                break
    
    def _bubble_down(self, index: int) -> None:
        """Restore heap property by moving element down."""
        while True:
            min_index = index
            left = 2 * index + 1
            right = 2 * index + 2
            
            if left < len(self._heap) and self._heap[left] < self._heap[min_index]:
                min_index = left
            
            if right < len(self._heap) and self._heap[right] < self._heap[min_index]:
                min_index = right
            
            if min_index != index:
                self._swap(index, min_index)
                index = min_index
            else:
                break
    
    def _swap(self, i: int, j: int) -> None:
        """Swap two elements in the heap."""
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]
```

---

## 11. Success Criteria

The refactoring will be considered successful when:

1. ✅ All tests pass with >90% coverage
2. ✅ All public APIs have type hints
3. ✅ All modules have comprehensive docstrings
4. ✅ CI/CD pipeline passes on Python 3.8-3.12
5. ✅ No performance regressions (benchmark suite)
6. ✅ Documentation is complete and published
7. ✅ Migration guide is clear and tested
8. ✅ Code quality metrics (ruff, black, mypy) all pass
9. ✅ Package successfully published to PyPI
10. ✅ Community feedback is positive

---

## 12. Risks and Mitigation

### Risk 1: Breaking Changes
**Mitigation**: Maintain backward compatibility with deprecation warnings for at least 2 major versions.

### Risk 2: Community Adoption
**Mitigation**: Clear migration guide, maintain old documentation, responsive to issues.

### Risk 3: Time Investment
**Mitigation**: Incremental rollout, prioritize high-impact changes, community contributions welcome.

### Risk 4: Performance Regression
**Mitigation**: Benchmark suite, performance testing in CI, careful review of algorithm changes.

---

## Appendix A: Style Guide

### Python Style
- Follow PEP 8, PEP 257 (docstrings)
- Use Black for formatting (line length: 88)
- Use Google-style docstrings
- Type hints for all public APIs

### Naming Conventions
- Functions/Variables: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`
- Private members: `_leading_underscore`
- Modules: lowercase, no underscores if possible

### Documentation
- Module docstring at top of every file
- Class docstring with examples
- Function docstring with Args, Returns, Raises, Examples
- Include complexity analysis where relevant

---

## Appendix B: Resources

### Tools
- **Formatting**: [Black](https://black.readthedocs.io/)
- **Linting**: [Ruff](https://docs.astral.sh/ruff/)
- **Type Checking**: [MyPy](https://mypy.readthedocs.io/)
- **Testing**: [Pytest](https://docs.pytest.org/)
- **Property Testing**: [Hypothesis](https://hypothesis.readthedocs.io/)

### References
- [PEP 8](https://peps.python.org/pep-0008/) - Style Guide for Python Code
- [PEP 257](https://peps.python.org/pep-0257/) - Docstring Conventions
- [PEP 484](https://peps.python.org/pep-0484/) - Type Hints
- [PEP 517](https://peps.python.org/pep-0517/) - Build System
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)

---

## Conclusion

This enhanced refactoring plan transforms the algorithms repository into a modern, maintainable, and professional Python package. The focus on:

1. **Separation of concerns** (data structures vs algorithms)
2. **Modern Python standards** (type hints, dataclasses, pyproject.toml)
3. **Code quality** (linting, formatting, testing)
4. **Documentation** (comprehensive docstrings, examples)
5. **Developer experience** (clear structure, good tooling)

...will make the codebase more accessible to contributors and more useful to users.

The incremental implementation approach ensures that the project remains functional throughout the refactoring process, and backward compatibility measures protect existing users.

**Estimated Timeline**: 17 weeks (~4 months) for complete implementation
**Recommended Team Size**: 2-3 developers
**Priority**: High (technical debt reduction, improved maintainability)

---

## Appendix: Key Changes from Original Plan

This section documents significant changes made after reviewing the actual codebase:

### Major Architectural Decisions Added:

1. **Section 1: Critical Architectural Decisions (NEW)**
   - Added Union-Find consolidation strategy (2 implementations found)
   - Defined BFS/DFS module merger strategy (technique vs category issue)
   - Clarified heap module split (data structure vs algorithms)
   - Detailed tree structure complexity resolution
   - Module placement decisions for ambiguous modules

2. **Phase 0: Discovery & Cataloging (NEW)**
   - Added 2-week discovery phase before any refactoring
   - Created tooling requirements for safe migration
   - Risk mitigation through comprehensive auditing

### Enhanced Strategies:

3. **Python Version Deprecation (Section 3.1)**
   - Added formal deprecation timeline
   - Communication strategy for breaking change
   - Migration path for users on older Python versions

4. **Wildcard Import Elimination (Section 3.3)**
   - Automated conversion strategy (35+ `__init__.py` files affected)
   - Tooling to generate __all__ lists
   - Priority order for conversion

5. **Test Migration Strategy (Section 4.1)**
   - Multi-phase migration approach
   - Import compatibility layer (prevents test breakage)
   - Automated migration scripts

6. **Enhanced Backward Compatibility (Section 8)**
   - Multi-layer approach (re-exports + __getattr__ + individual modules)
   - Migration testing suite
   - Extended timeline (24 months before removal)
   - Automated migration tool for users

7. **CI/CD Modernization (Section 6.3)**
   - Travis CI → GitHub Actions migration
   - Multi-OS testing (Linux, macOS, Windows)
   - Separate lint, test, and docs jobs

### Timeline Adjustments:

- **Original**: 13 weeks (6 phases)
- **Updated**: 17 weeks (7 phases, with Phase 0)
- **Rationale**: Added discovery phase, increased time for complex migrations

### Specific Module Changes:

| Module | Original Plan | Updated Plan | Reason |
|--------|---------------|--------------|--------|
| `bfs/`, `dfs/` | Move to `graph/` | Merge into `graph/` with technique suffixes + keep compatibility modules | BFS/DFS are techniques, not categories |
| `heap/` | Move to data_structures | Split: data structure → data_structures, algorithms → array/ | Contains both |
| `unionfind/` | Move to data_structures | Consolidate 2 implementations first | Found duplicate in graph/ |
| `distribution/` | Unclear | Move to `math/statistics/` | Statistics is math |
| `streaming/` | Move to `misc/` | Keep as distinct category | Valid algorithmic category |
| `automata/` | Move to `misc/` | Keep as distinct category | Valid algorithmic category |
| `ml/` | Move to `misc/` | Remove or move to graph/ | Out of scope / nearest_neighbor is graph |
| `unix/` | Move to `misc/` | Remove or separate package | Not algorithms |

### Risk Mitigation Added:

- Discovery phase prevents surprises during implementation
- Import compatibility layer prevents test breakage
- Automated tooling reduces human error
- Backward compatibility extends to 24 months
- Multi-layer deprecation strategy
- Comprehensive testing at each phase

### Quality Improvements:

- All abstract base classes standardized (ABCMeta → ABC)
- All dangerous defaults catalogued and fixed
- All wildcard imports converted to explicit
- Type hints using Python 3.8+ features
- GitHub Actions replacing deprecated Travis CI

**Result**: A more thorough, safer, and more maintainable refactoring plan that addresses real-world complexity discovered in the codebase.





