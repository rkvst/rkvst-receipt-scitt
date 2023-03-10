"""
Test decoding of RKVST receipts
"""

from importlib.resources import read_text  # 3.9 + we should use 'files' instead

from unittest import TestCase

from rkvst_receipt_scitt.receiptdecoder import decode_cosesign1_payload

PAYLOAD_KEYS = "application_parameters named_proofs".split()
APPLICATION_PARAMETERS = "who_declared who_accepted essentials attribute_kindnames attribute_values when".split()


class TestReceiptDecoder(TestCase):
    """
    Receipt decode tests
    """

    def test_payload_extraction(self):
        """
        Test we can get at the payload and that it is valid json
        """
        b64 = read_text("unittests.data", "khipu_receipt_happy_default.b64")
        payload = decode_cosesign1_payload(b64)
        for k in PAYLOAD_KEYS:
            self.assertIn(k, payload)
        for k in APPLICATION_PARAMETERS:
            self.assertIn(k, payload["application_parameters"])
