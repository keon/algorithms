#!/usr/bin/env python3
"""
__all__ List Generator

Generates explicit __all__ lists for __init__.py files based on what's currently
exported via wildcard imports.

Usage:
    python tools/generate_all_lists.py MODULE_PATH

Examples:
    python tools/generate_all_lists.py algorithms/array/
    python tools/generate_all_lists.py algorithms/array/ > /tmp/array_init.py
"""

import argparse
import ast
import sys
from pathlib import Path
from typing import Dict, List, Set


def extract_public_names(file_path: Path) -> Set[str]:
    """Extract all public (non-underscore-prefixed) names from a module."""
    try:
        content = file_path.read_text(encoding='utf-8')
        tree = ast.parse(content, filename=str(file_path))
    except Exception:
        return set()
    
    public_names = set()
    
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and not node.name.startswith('_'):
            public_names.add(node.name)
        elif isinstance(node, ast.FunctionDef) and not node.name.startswith('_'):
            public_names.add(node.name)
        elif isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and not target.id.startswith('_'):
                    # Only include if it's a constant (uppercase)
                    if target.id.isupper():
                        public_names.add(target.id)
    
    return public_names


def analyze_current_init(init_path: Path) -> Dict[str, Set[str]]:
    """Analyze current __init__.py to see what it imports."""
    if not init_path.exists():
        return {}
    
    try:
        content = init_path.read_text(encoding='utf-8')
        tree = ast.parse(content, filename=str(init_path))
    except Exception:
        return {}
    
    imports = {}
    
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom):
            if node.module and node.names:
                if node.names[0].name == '*':
                    # Wildcard import - need to check the source module
                    imports[node.module] = set()  # Will fill in later
                else:
                    imports[node.module] = {alias.name for alias in node.names}
    
    return imports


def generate_init_content(module_dir: Path) -> str:
    """Generate new __init__.py content with explicit imports and __all__."""
    init_path = module_dir / '__init__.py'
    module_name = module_dir.name
    
    # Get current imports if __init__ exists
    current_imports = analyze_current_init(init_path)
    
    # Scan all .py files in the directory
    module_exports = {}
    for py_file in sorted(module_dir.glob('*.py')):
        if py_file.name == '__init__.py':
            continue
        
        module_stem = py_file.stem
        exports = extract_public_names(py_file)
        
        if exports:
            module_exports[module_stem] = exports
    
    # Build output
    lines = [
        f'"""{module_name.replace("_", " ").title()} module."""',
        '',
    ]
    
    # Generate imports
    all_exported = []
    
    for module_stem, exports in sorted(module_exports.items()):
        if not exports:
            continue
        
        sorted_exports = sorted(exports)
        all_exported.extend(sorted_exports)
        
        if len(sorted_exports) == 1:
            lines.append(f'from .{module_stem} import {sorted_exports[0]}')
        elif len(sorted_exports) <= 3:
            lines.append(f'from .{module_stem} import {", ".join(sorted_exports)}')
        else:
            # Multi-line for readability
            lines.append(f'from .{module_stem} import (')
            for export in sorted_exports[:-1]:
                lines.append(f'    {export},')
            lines.append(f'    {sorted_exports[-1]}')
            lines.append(')')
    
    lines.append('')
    
    # Generate __all__
    lines.append('__all__ = [')
    for name in sorted(all_exported):
        lines.append(f"    '{name}',")
    lines.append(']')
    lines.append('')
    
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(
        description='Generate __all__ lists for __init__.py files',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument(
        'module_path',
        type=Path,
        help='Path to module directory'
    )
    parser.add_argument(
        '--write',
        action='store_true',
        help='Write directly to __init__.py (default: print to stdout)'
    )
    parser.add_argument(
        '--backup',
        action='store_true',
        help='Create backup of existing __init__.py'
    )
    
    args = parser.parse_args()
    
    if not args.module_path.exists():
        print(f"Error: Path '{args.module_path}' does not exist", file=sys.stderr)
        sys.exit(1)
    
    if not args.module_path.is_dir():
        print(f"Error: Path '{args.module_path}' is not a directory", file=sys.stderr)
        sys.exit(1)
    
    print(f"Analyzing {args.module_path}...", file=sys.stderr)
    content = generate_init_content(args.module_path)
    
    if args.write:
        init_path = args.module_path / '__init__.py'
        
        if args.backup and init_path.exists():
            backup_path = init_path.with_suffix('.py.bak')
            backup_path.write_text(init_path.read_text())
            print(f"Created backup: {backup_path}", file=sys.stderr)
        
        init_path.write_text(content)
        print(f"Wrote {init_path}", file=sys.stderr)
    else:
        print(content)


if __name__ == '__main__':
    main()


