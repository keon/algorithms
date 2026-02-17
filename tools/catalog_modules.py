#!/usr/bin/env python3
"""
Module Cataloging Script

Scans the codebase and classifies each Python file as:
- data_structure: Defines a reusable data structure class
- algorithm: Implements an algorithm or algorithmic function
- utility: Helper/utility code (tests, config, etc.)

Usage:
    python tools/catalog_modules.py [--format json|md] [--output FILE]

Examples:
    python tools/catalog_modules.py --format md > MODULE_CATALOG.md
    python tools/catalog_modules.py --format json --output catalog.json
"""

import argparse
import ast
import json
import sys
from pathlib import Path
from typing import Dict, List, Literal, TypedDict


class ModuleInfo(TypedDict):
    """Information about a Python module."""
    path: str
    classification: Literal["data_structure", "algorithm", "utility", "test"]
    loc: int
    classes: List[str]
    functions: List[str]
    imports: List[str]
    confidence: float  # 0-1, how confident we are in classification


class ModuleAnalyzer(ast.NodeVisitor):
    """AST visitor to analyze module contents."""
    
    def __init__(self):
        self.classes = []
        self.functions = []
        self.imports = []
        self.has_init = False
        self.has_magic_methods = 0
        self.has_abstract = False
        
    def visit_ClassDef(self, node: ast.ClassDef):
        self.classes.append(node.name)
        
        # Check for data structure indicators
        for item in node.body:
            if isinstance(item, ast.FunctionDef):
                if item.name == '__init__':
                    self.has_init = True
                if item.name.startswith('__') and item.name.endswith('__'):
                    self.has_magic_methods += 1
        
        # Check for abstract base classes
        for base in node.bases:
            if isinstance(base, ast.Name) and base.id in ('ABC', 'ABCMeta'):
                self.has_abstract = True
        
        self.generic_visit(node)
    
    def visit_FunctionDef(self, node: ast.FunctionDef):
        # Only count module-level functions
        if not isinstance(node, ast.AsyncFunctionDef):
            self.functions.append(node.name)
        self.generic_visit(node)
    
    def visit_Import(self, node: ast.Import):
        for alias in node.names:
            self.imports.append(alias.name)
    
    def visit_ImportFrom(self, node: ast.ImportFrom):
        if node.module:
            self.imports.append(node.module)


def count_loc(file_path: Path) -> int:
    """Count lines of code (excluding blank lines and comments)."""
    try:
        content = file_path.read_text(encoding='utf-8')
        lines = content.split('\n')
        loc = 0
        in_docstring = False
        
        for line in lines:
            stripped = line.strip()
            # Toggle docstring state
            if '"""' in stripped or "'''" in stripped:
                in_docstring = not in_docstring
                continue
            # Skip blank lines, comments, and docstrings
            if not stripped or stripped.startswith('#') or in_docstring:
                continue
            loc += 1
        
        return loc
    except Exception:
        return 0


def analyze_module(file_path: Path, root_path: Path) -> ModuleInfo:
    """Analyze a Python module and classify it."""
    try:
        content = file_path.read_text(encoding='utf-8')
        tree = ast.parse(content, filename=str(file_path))
    except Exception as e:
        return {
            'path': str(file_path),
            'classification': 'utility',
            'loc': 0,
            'classes': [],
            'functions': [],
            'imports': [],
            'confidence': 0.0,
        }
    
    analyzer = ModuleAnalyzer()
    analyzer.visit(tree)
    
    # Classify based on heuristics
    classification, confidence = classify_module(
        file_path, analyzer, len(content.split('\n'))
    )
    
    # Try to get relative path
    try:
        rel_path = file_path.relative_to(root_path.parent)
    except ValueError:
        rel_path = file_path
    
    return {
        'path': str(rel_path),
        'classification': classification,
        'loc': count_loc(file_path),
        'classes': analyzer.classes,
        'functions': analyzer.functions,
        'imports': analyzer.imports,
        'confidence': confidence,
    }


def classify_module(
    file_path: Path,
    analyzer: ModuleAnalyzer,
    total_lines: int
) -> tuple[Literal["data_structure", "algorithm", "utility", "test"], float]:
    """
    Classify a module based on its contents.
    
    Returns (classification, confidence_score)
    """
    path_str = str(file_path)
    
    # Test files
    if 'test' in path_str or file_path.name.startswith('test_'):
        return ('test', 1.0)
    
    # Utility files
    if file_path.name in ('__init__.py', 'setup.py', 'conftest.py'):
        return ('utility', 1.0)
    
    # Data structure indicators
    ds_score = 0.0
    if analyzer.classes:
        ds_score += 0.4
    if analyzer.has_init:
        ds_score += 0.2
    if analyzer.has_magic_methods >= 3:
        ds_score += 0.2
    if analyzer.has_abstract:
        ds_score += 0.1
    
    # Check for data structure keywords in path
    ds_keywords = ['stack', 'queue', 'heap', 'tree', 'graph', 'linkedlist', 
                   'hashtable', 'trie', 'union', 'disjoint']
    if any(kw in path_str.lower() for kw in ds_keywords):
        ds_score += 0.1
    
    # Algorithm indicators
    algo_score = 0.0
    if analyzer.functions:
        algo_score += 0.3
    if len(analyzer.functions) > len(analyzer.classes):
        algo_score += 0.2
    
    # Check for algorithm keywords in path
    algo_keywords = ['sort', 'search', 'dp', 'dynamic', 'greedy', 'backtrack',
                     'bfs', 'dfs', 'dijkstra', 'bellman']
    if any(kw in path_str.lower() for kw in algo_keywords):
        algo_score += 0.2
    
    # Classify based on scores
    if ds_score > algo_score and ds_score > 0.5:
        return ('data_structure', min(ds_score, 1.0))
    elif algo_score >= 0.3:
        return ('algorithm', min(algo_score, 1.0))
    else:
        return ('utility', 0.5)


def scan_directory(root_path: Path) -> List[ModuleInfo]:
    """Scan directory for Python modules and analyze them."""
    modules = []
    
    for py_file in root_path.rglob('*.py'):
        # Skip __pycache__ and .venv
        if '__pycache__' in str(py_file) or '.venv' in str(py_file):
            continue
        
        module_info = analyze_module(py_file, root_path)
        modules.append(module_info)
    
    return sorted(modules, key=lambda m: m['path'])


def format_markdown(modules: List[ModuleInfo]) -> str:
    """Format module catalog as Markdown."""
    output = ["# Module Catalog", "", "## Summary", ""]
    
    # Count by classification
    counts = {}
    for mod in modules:
        counts[mod['classification']] = counts.get(mod['classification'], 0) + 1
    
    total_loc = sum(m['loc'] for m in modules)
    
    output.append(f"- **Total Modules**: {len(modules)}")
    output.append(f"- **Total LOC**: {total_loc:,}")
    for classification, count in sorted(counts.items()):
        output.append(f"- **{classification.replace('_', ' ').title()}**: {count}")
    
    output.append("\n## Modules by Classification\n")
    
    for classification in ['data_structure', 'algorithm', 'utility', 'test']:
        classified_mods = [m for m in modules if m['classification'] == classification]
        if not classified_mods:
            continue
        
        output.append(f"### {classification.replace('_', ' ').title()} ({len(classified_mods)})\n")
        output.append("| Path | LOC | Classes | Functions | Confidence |")
        output.append("|------|-----|---------|-----------|------------|")
        
        for mod in classified_mods:
            classes_str = ', '.join(mod['classes'][:3])
            if len(mod['classes']) > 3:
                classes_str += f', ... ({len(mod['classes'])} total)'
            functions_str = str(len(mod['functions']))
            confidence_str = f"{mod['confidence']:.1%}"
            
            output.append(
                f"| `{mod['path']}` | {mod['loc']} | {classes_str or '-'} | "
                f"{functions_str} | {confidence_str} |"
            )
        
        output.append("")
    
    return '\n'.join(output)


def format_json(modules: List[ModuleInfo]) -> str:
    """Format module catalog as JSON."""
    return json.dumps({
        'summary': {
            'total_modules': len(modules),
            'total_loc': sum(m['loc'] for m in modules),
            'by_classification': {
                classification: len([m for m in modules if m['classification'] == classification])
                for classification in ['data_structure', 'algorithm', 'utility', 'test']
            }
        },
        'modules': modules
    }, indent=2)


def main():
    parser = argparse.ArgumentParser(
        description='Catalog and classify Python modules in the codebase',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument(
        '--format',
        choices=['md', 'json'],
        default='md',
        help='Output format (default: md)'
    )
    parser.add_argument(
        '--output',
        type=Path,
        help='Output file (default: stdout)'
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
    modules = scan_directory(args.path)
    print(f"Found {len(modules)} modules", file=sys.stderr)
    
    if args.format == 'json':
        output = format_json(modules)
    else:
        output = format_markdown(modules)
    
    if args.output:
        args.output.write_text(output)
        print(f"Wrote catalog to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == '__main__':
    main()

