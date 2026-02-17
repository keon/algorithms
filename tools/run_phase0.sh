#!/bin/bash
# Run all Phase 0 discovery tools and generate reports

set -e

echo "========================================="
echo "Phase 0: Discovery & Cataloging"
echo "========================================="
echo ""

# Create output directory
mkdir -p docs/internal/phase0

echo "1️⃣  Cataloging modules..."
python tools/catalog_modules.py --format md > docs/internal/phase0/MODULE_CATALOG.md
python tools/catalog_modules.py --format json --output docs/internal/phase0/catalog.json
echo "   ✅ MODULE_CATALOG.md created"

echo ""
echo "2️⃣  Finding dangerous defaults..."
python tools/find_dangerous_defaults.py algorithms/ > docs/internal/phase0/DANGEROUS_DEFAULTS.md
echo "   ✅ DANGEROUS_DEFAULTS.md created"

echo ""
echo "3️⃣  Auditing wildcard imports..."
python tools/find_wildcard_imports.py > docs/internal/phase0/WILDCARD_AUDIT.md
echo "   ✅ WILDCARD_AUDIT.md created"

echo ""
echo "4️⃣  Analyzing import dependencies..."
python tools/analyze_imports.py --graph > docs/internal/phase0/DEPENDENCY_ANALYSIS.md
python tools/analyze_imports.py --graph --output docs/internal/phase0/dependency_graph.json
echo "   ✅ DEPENDENCY_ANALYSIS.md created"
echo "   ✅ dependency_graph.json created"

echo ""
echo "========================================="
echo "Phase 0 Complete!"
echo "========================================="
echo ""
echo "Reports generated in: docs/internal/phase0/"
echo ""
echo "Next steps:"
echo "  1. Review MODULE_CATALOG.md for classification accuracy"
echo "  2. Check DANGEROUS_DEFAULTS.md for issues to fix"
echo "  3. Review WILDCARD_AUDIT.md for import conversions"
echo "  4. Examine DEPENDENCY_ANALYSIS.md for circular dependencies"
echo "  5. Create PHASE_0_REPORT.md summarizing findings"
echo ""


