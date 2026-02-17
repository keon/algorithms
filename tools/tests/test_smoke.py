"""
Smoke tests for Phase 0 tools.

These tests verify that each tool can run without crashing.
"""

import subprocess
import sys
from pathlib import Path

TOOLS_DIR = Path(__file__).parent.parent
ROOT_DIR = TOOLS_DIR.parent


def test_catalog_modules_help():
    """Test catalog_modules.py --help runs."""
    result = subprocess.run(
        [sys.executable, TOOLS_DIR / 'catalog_modules.py', '--help'],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert 'catalog' in result.stdout.lower()


def test_find_dangerous_defaults_help():
    """Test find_dangerous_defaults.py --help runs."""
    result = subprocess.run(
        [sys.executable, TOOLS_DIR / 'find_dangerous_defaults.py', '--help'],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert 'dangerous' in result.stdout.lower()


def test_find_wildcard_imports_help():
    """Test find_wildcard_imports.py --help runs."""
    result = subprocess.run(
        [sys.executable, TOOLS_DIR / 'find_wildcard_imports.py', '--help'],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert 'wildcard' in result.stdout.lower()


def test_analyze_imports_help():
    """Test analyze_imports.py --help runs."""
    result = subprocess.run(
        [sys.executable, TOOLS_DIR / 'analyze_imports.py', '--help'],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert 'import' in result.stdout.lower()


def test_generate_all_lists_help():
    """Test generate_all_lists.py --help runs."""
    result = subprocess.run(
        [sys.executable, TOOLS_DIR / 'generate_all_lists.py', '--help'],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert '__all__' in result.stdout.lower() or 'all' in result.stdout.lower()


def test_migrate_imports_help():
    """Test migrate_imports.py --help runs."""
    result = subprocess.run(
        [sys.executable, TOOLS_DIR / 'migrate_imports.py', '--help'],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert 'migrate' in result.stdout.lower()


if __name__ == '__main__':
    # Run tests manually if pytest not available
    import traceback
    
    tests = [
        test_catalog_modules_help,
        test_find_dangerous_defaults_help,
        test_find_wildcard_imports_help,
        test_analyze_imports_help,
        test_generate_all_lists_help,
        test_migrate_imports_help,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            print(f"✅ {test.__name__}")
            passed += 1
        except AssertionError as e:
            print(f"❌ {test.__name__}: {e}")
            traceback.print_exc()
            failed += 1
        except Exception as e:
            print(f"💥 {test.__name__}: {e}")
            traceback.print_exc()
            failed += 1
    
    print(f"\nResults: {passed} passed, {failed} failed")
    sys.exit(0 if failed == 0 else 1)


