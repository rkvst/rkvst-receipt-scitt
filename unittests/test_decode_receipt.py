"""
Test decoding of RKVST receipts
"""

import json
from importlib.resources import read_text  # 3.9 + we should use 'files' instead
from unittest import TestCase

from rkvst_receipt_scitt.receiptdecoder import (
    receipt_trie_alg_contents,
    receipt_verify_envelope
)

from .wellknown import key 

PAYLOAD_KEYS = "application_parameters named_proofs".split()
APPLICATION_PARAMETERS = "app_id app_content_ref element_manifest monotonic_version".split()
KHIPU_MANIFEST_ELEMENTS = "who_declared who_accepted essentials attribute_kindnames attribute_values when".split()


class TestReceiptDecoder(TestCase):
    """
    Receipt decode tests
    """

    def test_payload_extraction(self):
        """
        Test we can get at the payload and that it is valid json
        """
        b64 = read_text("unittests.data", "khipu_receipt_happy_default.b64")
        contents = json.loads(receipt_trie_alg_contents(b64)[1])
        for k in PAYLOAD_KEYS:
            self.assertIn(k, contents)
        for k in APPLICATION_PARAMETERS:
            self.assertIn(k, contents["application_parameters"])
        for k in KHIPU_MANIFEST_ELEMENTS:
            self.assertIn(k, contents["application_parameters"]["element_manifest"])

    def test_verify_envelope(self):
        """
        Test we can get at the payload and that it is valid json
        """
        b64 = read_text("unittests.data", "khipu_receipt_happy_default.b64")
        [phdr, sig, contents] = receipt_trie_alg_contents(b64)
        k = key()
        receipt_verify_envelope(k, phdr, sig, contents)

