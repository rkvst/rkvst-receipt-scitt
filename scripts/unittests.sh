#!/bin/sh
#
# run unittests
#
python3 --version

rm -f coverage.xml
rm -rf htmlcov
COVERAGE="coverage"
${COVERAGE} --version
${COVERAGE} run --branch --source rkvst_receipt_scitt -m unittest -v 
${COVERAGE} html
${COVERAGE} xml
${COVERAGE} report

