#!/usr/bin/env python3
"""
Wildcard Import Scanner

Finds all wildcard imports (`from module import *`) and catalogs what symbols
they actually reference, helping convert to explicit imports.

Usage:
    python tools/find_wildcard_imports.py [--path PATH]

Examples:
    python tools/find_wildcard_imports.py
    python tools/find_wildcard_imports.py --path algorithms/
    python tools/find_wildcard_imports.py > WILDCARD_AUDIT.md
"""

import argparse
import ast
import sys
from pathlib import Path
from typing import Dict, List, NamedTuple, Set


class WildcardImport(NamedTuple):
    """Information about a wildcard import."""
    file: str
    line: int
    module: str
    referenced_symbols: Set[str]


class WildcardFinder(ast.NodeVisitor):
    """AST visitor to find wildcard imports and their usage."""
    
    def __init__(self, filename: str, module_content: str):
        self.filename = filename
        self.module_content = module_content
        self.wildcard_imports: List[WildcardImport] = []
        self.wildcard_modules: Dict[int, str] = {}  # line -> module
        self.all_names: Set[str] = set()
    
    def visit_ImportFrom(self, node: ast.ImportFrom):
        """Find wildcard imports."""
        if node.names[0].name == '*':
            self.wildcard_modules[node.lineno] = node.module or ''
        self.generic_visit(node)
    
    def visit_Name(self, node: ast.Name):
        """Track all name references."""
        self.all_names.add(node.id)
        self.generic_visit(node)
    
    def finalize(self):
        """Match wildcard imports with referenced symbols."""
        for line, module in self.wildcard_modules.items():
            # Try to determine which symbols come from this import
            # This is a heuristic - we can't be 100% sure without runtime info
            symbols = self._guess_symbols_from_module(module)
            
            self.wildcard_imports.append(WildcardImport(
                file=self.filename,
                line=line,
                module=module,
                referenced_symbols=symbols
            ))
    
    def _guess_symbols_from_module(self, module: str) -> Set[str]:
        """
        Heuristically guess which symbols might come from a wildcard import.
        This is not perfect but helps identify likely candidates.
        """
        # Extract module name for pattern matching
        module_parts = module.split('.')
        base_module = module_parts[-1] if module_parts else ''
        
        likely_symbols = set()
        
        # Pattern: if module is 'two_sum', likely exports 'two_sum' function
        if base_module:
            # Convert module name variations
            variations = [
                base_module,
                base_module.replace('_', ''),
                ''.join(word.capitalize() for word in base_module.split('_')),
            ]
            for name in self.all_names:
                name_lower = name.lower()
                if any(var.lower() in name_lower for var in variations):
                    likely_symbols.add(name)
        
        # If we can't guess, just return all names (conservative)
        if not likely_symbols and len(self.all_names) < 50:
            return self.all_names.copy()
        
        return likely_symbols or {'<unknown>'}


def scan_file(file_path: Path, root_path: Path = None) -> List[WildcardImport]:
    """Scan a Python file for wildcard imports."""
    try:
        content = file_path.read_text(encoding='utf-8')
        tree = ast.parse(content, filename=str(file_path))
    except Exception as e:
        print(f"Error parsing {file_path}: {e}", file=sys.stderr)
        return []
    
    # Get relative path if root provided
    if root_path:
        try:
            rel_path = file_path.relative_to(root_path)
        except ValueError:
            rel_path = file_path
    else:
        rel_path = file_path
    
    finder = WildcardFinder(str(rel_path), content)
    finder.visit(tree)
    finder.finalize()
    return finder.wildcard_imports


def scan_directory(root_path: Path) -> List[WildcardImport]:
    """Scan directory for wildcard imports."""
    all_wildcards = []
    
    for py_file in root_path.rglob('*.py'):
        if '__pycache__' not in str(py_file):
            all_wildcards.extend(scan_file(py_file, root_path))
    
    return sorted(all_wildcards, key=lambda w: (w.file, w.line))


def generate_explicit_import(wildcard: WildcardImport) -> str:
    """Generate explicit import statement."""
    if not wildcard.referenced_symbols or wildcard.referenced_symbols == {'<unknown>'}:
        return f"# TODO: Determine actual symbols\nfrom {wildcard.module} import ..."
    
    symbols = sorted(wildcard.referenced_symbols)
    if len(symbols) <= 3:
        return f"from {wildcard.module} import {', '.join(symbols)}"
    else:
        # Multi-line for readability
        lines = [f"from {wildcard.module} import ("]
        for symbol in symbols[:-1]:
            lines.append(f"    {symbol},")
        lines.append(f"    {symbols[-1]}")
        lines.append(")")
        return '\n'.join(lines)


def format_markdown(wildcards: List[WildcardImport]) -> str:
    """Format wildcard imports as Markdown."""
    output = [
        "# Wildcard Import Audit",
        "",
        f"Found **{len(wildcards)}** wildcard imports.",
        "",
        "Wildcard imports (`from module import *`) should be converted to explicit imports.",
        "",
        "## Findings",
        ""
    ]
    
    current_file = None
    for wc in wildcards:
        if wc.file != current_file:
            current_file = wc.file
            output.append(f"### `{wc.file}`\n")
        
        output.append(f"#### Line {wc.line}: `from {wc.module} import *`")
        output.append("")
        
        if wc.referenced_symbols and wc.referenced_symbols != {'<unknown>'}:
            output.append(f"**Referenced symbols** ({len(wc.referenced_symbols)}):")
            symbols_list = ', '.join(f"`{s}`" for s in sorted(wc.referenced_symbols))
            output.append(f"{symbols_list}")
        else:
            output.append("**Referenced symbols**: Could not determine")
        
        output.append("")
        output.append("**Suggested explicit import:**")
        output.append("```python")
        output.append(generate_explicit_import(wc))
        output.append("```")
        output.append("")
    
    # Summary by file type
    output.append("## Summary by Directory")
    output.append("")
    
    by_dir = {}
    for wc in wildcards:
        dir_name = str(Path(wc.file).parent)
        by_dir[dir_name] = by_dir.get(dir_name, 0) + 1
    
    output.append("| Directory | Count |")
    output.append("|-----------|-------|")
    for dir_name, count in sorted(by_dir.items(), key=lambda x: -x[1]):
        output.append(f"| `{dir_name}` | {count} |")
    
    return '\n'.join(output)


def main():
    parser = argparse.ArgumentParser(
        description='Find and analyze wildcard imports in Python code',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument(
        '--path',
        type=Path,
        default=Path('algorithms'),
        help='Path to scan (default: algorithms/)'
    )
    
    args = parser.parse_args()
    
    if not args.path.exists():
        print(f"Error: Path '{args.path}' does not exist", file=sys.stderr)
        sys.exit(1)
    
    print(f"Scanning {args.path}...", file=sys.stderr)
    wildcards = scan_directory(args.path)
    print(f"Found {len(wildcards)} wildcard imports", file=sys.stderr)
    
    output = format_markdown(wildcards)
    print(output)


if __name__ == '__main__':
    main()

