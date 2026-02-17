#!/usr/bin/env python3
"""
Import Dependency Analyzer

Analyzes import dependencies across the codebase and generates a dependency graph.
Identifies circular dependencies, external vs internal imports.

Usage:
    python tools/analyze_imports.py [--graph] [--output FILE]

Examples:
    python tools/analyze_imports.py --graph
    python tools/analyze_imports.py --graph --output dependency_graph.json
    python tools/analyze_imports.py --find-cycles
"""

import argparse
import ast
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Set, Tuple


class ImportAnalyzer(ast.NodeVisitor):
    """AST visitor to analyze imports."""
    
    def __init__(self, module_path: str):
        self.module_path = module_path
        self.imports: Set[str] = set()
        self.import_details: List[Tuple[int, str, bool]] = []  # (line, module, is_from_import)
    
    def visit_Import(self, node: ast.Import):
        for alias in node.names:
            self.imports.add(alias.name)
            self.import_details.append((node.lineno, alias.name, False))
    
    def visit_ImportFrom(self, node: ast.ImportFrom):
        if node.module:
            self.imports.add(node.module)
            self.import_details.append((node.lineno, node.module, True))


def analyze_file(file_path: Path, root_path: Path = None) -> Dict:
    """Analyze imports in a file."""
    try:
        content = file_path.read_text(encoding='utf-8')
        tree = ast.parse(content, filename=str(file_path))
    except Exception as e:
        return {
            'path': str(file_path),
            'imports': [],
            'error': str(e)
        }
    
    # Get relative path if root provided
    if root_path:
        try:
            rel_path = file_path.relative_to(root_path.parent)
        except ValueError:
            rel_path = file_path
    else:
        rel_path = file_path
    
    analyzer = ImportAnalyzer(str(rel_path))
    analyzer.visit(tree)
    
    # Classify imports
    internal_imports = []
    external_imports = []
    
    for imp in analyzer.imports:
        # Check if it's an internal import (starts with 'algorithms' or 'data_structures')
        if imp.startswith(('algorithms', 'data_structures')):
            internal_imports.append(imp)
        else:
            external_imports.append(imp)
    
    return {
        'path': str(rel_path),
        'imports': list(analyzer.imports),
        'internal_imports': internal_imports,
        'external_imports': external_imports,
        'import_details': analyzer.import_details,
    }


def build_dependency_graph(root_path: Path) -> Dict:
    """Build complete dependency graph."""
    graph = {
        'nodes': [],
        'edges': [],
        'modules': {}
    }
    
    py_files = list(root_path.rglob('*.py'))
    py_files = [f for f in py_files if '__pycache__' not in str(f)]
    
    print(f"Analyzing {len(py_files)} files...", file=sys.stderr)
    
    for py_file in py_files:
        analysis = analyze_file(py_file, root_path)
        module_name = str(py_file.relative_to(root_path.parent)).replace('/', '.').replace('.py', '')
        
        graph['modules'][module_name] = analysis
        graph['nodes'].append({
            'id': module_name,
            'path': analysis['path'],
            'internal_import_count': len(analysis.get('internal_imports', [])),
            'external_import_count': len(analysis.get('external_imports', []))
        })
        
        # Add edges for internal imports
        for imp in analysis.get('internal_imports', []):
            graph['edges'].append({
                'from': module_name,
                'to': imp
            })
    
    return graph


def find_cycles(graph: Dict) -> List[List[str]]:
    """Find circular dependencies using DFS."""
    adj_list = defaultdict(set)
    for edge in graph['edges']:
        adj_list[edge['from']].add(edge['to'])
    
    cycles = []
    visited = set()
    rec_stack = set()
    path = []
    
    def dfs(node):
        visited.add(node)
        rec_stack.add(node)
        path.append(node)
        
        for neighbor in adj_list.get(node, set()):
            if neighbor not in visited:
                dfs(neighbor)
            elif neighbor in rec_stack:
                # Found a cycle
                cycle_start = path.index(neighbor)
                cycle = path[cycle_start:] + [neighbor]
                cycles.append(cycle)
        
        path.pop()
        rec_stack.remove(node)
    
    for node in graph['nodes']:
        if node['id'] not in visited:
            dfs(node['id'])
    
    return cycles


def format_graph_markdown(graph: Dict, cycles: List[List[str]]) -> str:
    """Format dependency graph as Markdown."""
    output = [
        "# Dependency Graph Analysis",
        "",
        f"## Summary",
        "",
        f"- **Total Modules**: {len(graph['nodes'])}",
        f"- **Total Dependencies**: {len(graph['edges'])}",
        f"- **Circular Dependencies**: {len(cycles)}",
        ""
    ]
    
    # Top importers
    import_counts = defaultdict(int)
    for edge in graph['edges']:
        import_counts[edge['from']] += 1
    
    output.append("## Top Importers (by internal imports)")
    output.append("")
    output.append("| Module | Internal Imports |")
    output.append("|--------|------------------|")
    
    for module, count in sorted(import_counts.items(), key=lambda x: -x[1])[:15]:
        output.append(f"| `{module}` | {count} |")
    
    output.append("")
    
    # Top imported
    imported_counts = defaultdict(int)
    for edge in graph['edges']:
        imported_counts[edge['to']] += 1
    
    output.append("## Most Imported Modules")
    output.append("")
    output.append("| Module | Imported By |")
    output.append("|--------|-------------|")
    
    for module, count in sorted(imported_counts.items(), key=lambda x: -x[1])[:15]:
        output.append(f"| `{module}` | {count} |")
    
    output.append("")
    
    # Circular dependencies
    if cycles:
        output.append("## ⚠️  Circular Dependencies")
        output.append("")
        output.append(f"Found **{len(cycles)}** circular dependency chains:")
        output.append("")
        
        for i, cycle in enumerate(cycles[:10], 1):  # Show first 10
            output.append(f"### Cycle {i}")
            output.append("")
            output.append("```")
            output.append(" → ".join(cycle))
            output.append("```")
            output.append("")
    else:
        output.append("## ✅ No Circular Dependencies")
        output.append("")
    
    # External dependencies
    all_external = set()
    for module_info in graph['modules'].values():
        all_external.update(module_info.get('external_imports', []))
    
    output.append("## External Dependencies")
    output.append("")
    output.append(f"Total external packages: **{len(all_external)}**")
    output.append("")
    
    for dep in sorted(all_external):
        output.append(f"- `{dep}`")
    
    return '\n'.join(output)


def main():
    parser = argparse.ArgumentParser(
        description='Analyze import dependencies in the codebase',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument(
        '--graph',
        action='store_true',
        help='Generate dependency graph'
    )
    parser.add_argument(
        '--find-cycles',
        action='store_true',
        help='Find circular dependencies'
    )
    parser.add_argument(
        '--output',
        type=Path,
        help='Output file for JSON graph (default: stdout for markdown)'
    )
    parser.add_argument(
        '--path',
        type=Path,
        default=Path('algorithms'),
        help='Path to analyze (default: algorithms/)'
    )
    
    args = parser.parse_args()
    
    if not args.path.exists():
        print(f"Error: Path '{args.path}' does not exist", file=sys.stderr)
        sys.exit(1)
    
    print(f"Building dependency graph for {args.path}...", file=sys.stderr)
    graph = build_dependency_graph(args.path)
    
    print(f"Analyzing {len(graph['nodes'])} modules, {len(graph['edges'])} dependencies",
          file=sys.stderr)
    
    cycles = find_cycles(graph)
    if cycles:
        print(f"⚠️  Found {len(cycles)} circular dependencies", file=sys.stderr)
    else:
        print("✅ No circular dependencies found", file=sys.stderr)
    
    if args.output and args.graph:
        # Write JSON
        output_data = {
            **graph,
            'cycles': cycles
        }
        args.output.write_text(json.dumps(output_data, indent=2))
        print(f"Wrote graph to {args.output}", file=sys.stderr)
    else:
        # Write markdown to stdout
        output = format_graph_markdown(graph, cycles)
        print(output)


if __name__ == '__main__':
    main()

