#!/usr/bin/env bash
#
# Create virtualenv the rkvst_receipt_scittv1 command.
#
# 'task wheel' to generate installable wheel package generated locally.
#
rm -rf scitt-receipt-venv/
python3 -m venv scitt-receipt-venv
source scitt-receipt-venv/bin/activate
python3 -m pip install -q --force-reinstall dist/rkvst_receipt_scitt-*.whl
deactivate
