#!/usr/bin/env python3
"""
Import Migration Tool

Automatically updates imports from old structure to new structure.
This helps users migrate their code to algorithms v0.2.0+.

Usage:
    python tools/migrate_imports.py --path PATH [--dry-run]

Examples:
    python tools/migrate_imports.py --path my_project/
    python tools/migrate_imports.py --path my_project/ --dry-run
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple


# Import path mappings
IMPORT_MAPPINGS = {
    'from algorithms.arrays import': 'from algorithms.array import',
    'from algorithms.sort import': 'from algorithms.sorting import',
    'from algorithms.search import': 'from algorithms.searching import',
    'from algorithms.dp import': 'from algorithms.dynamic_programming import',
    'from algorithms.maths import': 'from algorithms.math import',
    'from algorithms.backtrack import': 'from algorithms.backtracking import',
    'from algorithms.bit import': 'from algorithms.bit_manipulation import',
    'from algorithms.strings import': 'from algorithms.string import',
    
    # BFS/DFS merges - these need special handling
    'from algorithms.bfs import count_islands': 'from algorithms.graph import count_islands_bfs as count_islands',
    'from algorithms.bfs import maze_search': 'from algorithms.graph import maze_search_bfs as maze_search',
    'from algorithms.bfs import': 'from algorithms.graph import',
    
    'from algorithms.dfs import count_islands': 'from algorithms.graph import count_islands_dfs as count_islands',
    'from algorithms.dfs import maze_search': 'from algorithms.graph import maze_search_dfs as maze_search',
    'from algorithms.dfs import': 'from algorithms.graph import',
    
    # Data structure moves
    'from algorithms.heap import BinaryHeap': 'from data_structures.heaps import BinaryHeap',
    'from algorithms.tree.tree import TreeNode': 'from data_structures.trees import TreeNode',
    'from algorithms.tree.bst.bst import': 'from data_structures.trees import',
    'from algorithms.graph.graph import': 'from data_structures.graphs import',
    'from algorithms.linkedlist.linkedlist import': 'from data_structures.linear import',
    'from algorithms.stack.stack import': 'from data_structures.linear import',
    'from algorithms.queues.queue import': 'from data_structures.linear import',
    'from algorithms.queues.priority_queue import': 'from data_structures.heaps import',
    'from algorithms.map.hashtable import': 'from data_structures.hashtables import',
    'from algorithms.unionfind': 'from data_structures.sets import union_find',
}

# Module name mappings (for import statements without from)
MODULE_MAPPINGS = {
    'algorithms.arrays': 'algorithms.array',
    'algorithms.sort': 'algorithms.sorting',
    'algorithms.search': 'algorithms.searching',
    'algorithms.dp': 'algorithms.dynamic_programming',
    'algorithms.maths': 'algorithms.math',
    'algorithms.backtrack': 'algorithms.backtracking',
    'algorithms.bit': 'algorithms.bit_manipulation',
    'algorithms.strings': 'algorithms.string',
}


def migrate_file(file_path: Path, dry_run: bool = False) -> Tuple[int, List[str]]:
    """
    Migrate imports in a single file.
    
    Returns:
        (change_count, list_of_changes)
    """
    try:
        content = file_path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"Error reading {file_path}: {e}", file=sys.stderr)
        return 0, []
    
    original_content = content
    changes = []
    
    # Apply import mappings
    for old_import, new_import in IMPORT_MAPPINGS.items():
        if old_import in content:
            content = content.replace(old_import, new_import)
            changes.append(f"  {old_import} → {new_import}")
    
    # Apply module name mappings
    for old_module, new_module in MODULE_MAPPINGS.items():
        # Match module names in import statements
        pattern = r'\bimport\s+' + re.escape(old_module) + r'\b'
        if re.search(pattern, content):
            content = re.sub(pattern, f'import {new_module}', content)
            changes.append(f"  import {old_module} → import {new_module}")
    
    # Write back if changed and not dry-run
    if content != original_content:
        if not dry_run:
            file_path.write_text(content)
        return len(changes), changes
    
    return 0, []


def migrate_directory(root_path: Path, dry_run: bool = False) -> Dict[str, Tuple[int, List[str]]]:
    """Migrate all Python files in a directory."""
    results = {}
    
    py_files = list(root_path.rglob('*.py'))
    py_files = [f for f in py_files if '__pycache__' not in str(f) and '.venv' not in str(f)]
    
    print(f"Scanning {len(py_files)} Python files...", file=sys.stderr)
    
    for py_file in py_files:
        change_count, changes = migrate_file(py_file, dry_run)
        if change_count > 0:
            results[str(py_file.relative_to(root_path))] = (change_count, changes)
    
    return results


def main():
    parser = argparse.ArgumentParser(
        description='Migrate imports to algorithms v0.2.0+ structure',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument(
        '--path',
        type=Path,
        required=True,
        help='Path to your code directory'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview changes without modifying files'
    )
    
    args = parser.parse_args()
    
    if not args.path.exists():
        print(f"Error: Path '{args.path}' does not exist", file=sys.stderr)
        sys.exit(1)
    
    mode = "DRY RUN" if args.dry_run else "MIGRATING"
    print(f"\n{mode}: Analyzing {args.path}\n", file=sys.stderr)
    
    results = migrate_directory(args.path, args.dry_run)
    
    if not results:
        print("✅ No changes needed - your imports are already up to date!", file=sys.stderr)
        return
    
    print(f"\n{'Would migrate' if args.dry_run else 'Migrated'} {len(results)} files:\n")
    
    total_changes = 0
    for file_path, (count, changes) in sorted(results.items()):
        print(f"📝 {file_path} ({count} changes)")
        for change in changes:
            print(change)
        print()
        total_changes += count
    
    print(f"Total: {total_changes} import statements {'would be' if args.dry_run else ''} updated\n")
    
    if args.dry_run:
        print("Run without --dry-run to apply these changes.")
    else:
        print("✅ Migration complete!")
        print("\nNext steps:")
        print("1. Run your tests to ensure everything works")
        print("2. Review the changes with: git diff")
        print("3. Commit the changes")


if __name__ == '__main__':
    main()


