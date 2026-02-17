#!/usr/bin/env python3
"""
Dangerous Default Argument Scanner

Finds dangerous default arguments like `def func(param={})` or `def func(param=[])`.
These are dangerous because the default is created once at function definition time
and shared across all invocations.

Usage:
    python tools/find_dangerous_defaults.py [PATHS...]

Examples:
    python tools/find_dangerous_defaults.py algorithms/
    python tools/find_dangerous_defaults.py algorithms/ data_structures/
    python tools/find_dangerous_defaults.py > DANGEROUS_DEFAULTS.md
"""

import argparse
import ast
import sys
from pathlib import Path
from typing import List, NamedTuple


class DangerousDefault(NamedTuple):
    """Information about a dangerous default argument."""
    file: str
    line: int
    function: str
    parameter: str
    default_type: str  # 'dict', 'list', 'set'
    signature: str
    suggested_fix: str


class DangerousDefaultFinder(ast.NodeVisitor):
    """AST visitor to find dangerous default arguments."""
    
    def __init__(self, filename: str):
        self.filename = filename
        self.dangerous_defaults: List[DangerousDefault] = []
        self.current_class = None
    
    def visit_ClassDef(self, node: ast.ClassDef):
        old_class = self.current_class
        self.current_class = node.name
        self.generic_visit(node)
        self.current_class = old_class
    
    def visit_FunctionDef(self, node: ast.FunctionDef):
        self._check_function(node)
        self.generic_visit(node)
    
    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef):
        self._check_function(node)
        self.generic_visit(node)
    
    def _check_function(self, node):
        """Check function for dangerous defaults."""
        for arg, default in zip(
            reversed(node.args.args),
            reversed(node.args.defaults)
        ):
            default_type = self._get_dangerous_type(default)
            if default_type:
                func_name = node.name
                if self.current_class:
                    func_name = f"{self.current_class}.{func_name}"
                
                # Generate signature
                signature = self._generate_signature(node, arg, default)
                
                # Generate fix
                suggested_fix = self._generate_fix(node, arg, default_type)
                
                self.dangerous_defaults.append(DangerousDefault(
                    file=self.filename,
                    line=node.lineno,
                    function=func_name,
                    parameter=arg.arg,
                    default_type=default_type,
                    signature=signature,
                    suggested_fix=suggested_fix
                ))
    
    def _get_dangerous_type(self, node) -> str | None:
        """Check if default is a dangerous mutable type."""
        if isinstance(node, ast.Dict):
            return 'dict'
        elif isinstance(node, ast.List):
            return 'list'
        elif isinstance(node, ast.Set):
            return 'set'
        return None
    
    def _generate_signature(self, func_node, arg, default) -> str:
        """Generate function signature excerpt."""
        args = []
        for a in func_node.args.args:
            if a == arg:
                args.append(f"{a.arg}={ast.unparse(default)}")
            else:
                args.append(a.arg)
        
        return f"def {func_node.name}({', '.join(args)})"
    
    def _generate_fix(self, func_node, arg, default_type) -> str:
        """Generate suggested fix."""
        param_name = arg.arg
        
        if default_type == 'dict':
            return (
                f"def {func_node.name}(..., {param_name}: Optional[dict] = None):\n"
                f"    {param_name} = {param_name} or {{}}"
            )
        elif default_type == 'list':
            return (
                f"def {func_node.name}(..., {param_name}: Optional[list] = None):\n"
                f"    {param_name} = {param_name} or []"
            )
        elif default_type == 'set':
            return (
                f"def {func_node.name}(..., {param_name}: Optional[set] = None):\n"
                f"    {param_name} = {param_name} or set()"
            )
        return ""


def scan_file(file_path: Path, root_path: Path = None) -> List[DangerousDefault]:
    """Scan a Python file for dangerous defaults."""
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
    
    finder = DangerousDefaultFinder(str(rel_path))
    finder.visit(tree)
    return finder.dangerous_defaults


def scan_paths(paths: List[Path]) -> List[DangerousDefault]:
    """Scan multiple paths for dangerous defaults."""
    all_dangerous = []
    
    for path in paths:
        if path.is_file() and path.suffix == '.py':
            all_dangerous.extend(scan_file(path, path.parent))
        elif path.is_dir():
            for py_file in path.rglob('*.py'):
                if '__pycache__' not in str(py_file):
                    all_dangerous.extend(scan_file(py_file, path))
    
    return sorted(all_dangerous, key=lambda d: (d.file, d.line))


def format_markdown(dangerous_defaults: List[DangerousDefault]) -> str:
    """Format dangerous defaults as Markdown."""
    output = [
        "# Dangerous Default Arguments",
        "",
        f"Found **{len(dangerous_defaults)}** dangerous default arguments.",
        "",
        "These use mutable defaults (dict, list, set) that are shared across function calls.",
        "",
        "## Issues Found",
        ""
    ]
    
    current_file = None
    for dd in dangerous_defaults:
        if dd.file != current_file:
            current_file = dd.file
            output.append(f"### `{dd.file}`\n")
        
        output.append(f"#### Line {dd.line}: `{dd.function}` parameter `{dd.parameter}`")
        output.append("")
        output.append("**Current:**")
        output.append(f"```python")
        output.append(dd.signature)
        output.append("```")
        output.append("")
        output.append("**Suggested Fix:**")
        output.append(f"```python")
        output.append(dd.suggested_fix)
        output.append("```")
        output.append("")
    
    return '\n'.join(output)


def main():
    parser = argparse.ArgumentParser(
        description='Find dangerous mutable default arguments in Python code',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument(
        'paths',
        nargs='*',
        type=Path,
        default=[Path('algorithms')],
        help='Paths to scan (default: algorithms/)'
    )
    
    args = parser.parse_args()
    
    # Validate paths
    for path in args.paths:
        if not path.exists():
            print(f"Error: Path '{path}' does not exist", file=sys.stderr)
            sys.exit(1)
    
    print(f"Scanning {len(args.paths)} path(s)...", file=sys.stderr)
    dangerous_defaults = scan_paths(args.paths)
    print(f"Found {len(dangerous_defaults)} dangerous defaults", file=sys.stderr)
    
    output = format_markdown(dangerous_defaults)
    print(output)


if __name__ == '__main__':
    main()

