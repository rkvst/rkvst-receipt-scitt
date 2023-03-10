"""
Support decoding of the receipt response from the RKVST /v1/notary/receipts end point

[SCITT-RECEIPTS]: https://datatracker.ietf.org/doc/draft-birkholz-scitt-receipts/

"""
# TODO: check format of docstrings is compatible with sphynx. need ci support adding to check this

import base64
import cbor2.decoder
from pycose.messages.sign1message import Sign1Message
import json

def decode_cosesign1(receiptb64: str) -> Sign1Message:
    """
    decode a pycose Sign1Message from the base64 cose encoded object
    :param receipt: base64 encoded CBOR Cose Sign1 receipt value obtained from the receipts api
    """
    receiptbytes = base64.standard_b64decode(receiptb64)
    # return Sign1Message.decode(receiptbytes)
    cose_obj = cbor2.decoder.loads(receiptbytes)
    return Sign1Message.from_cose_obj(cose_obj, allow_unknown_attributes=True)

def decode_cosesign1_payload(receiptb64: str) -> dict:
    """
    :param receipt: base64 encoded CBOR Cose Sign1 receipt value obtained from the receipts api
    """
    msg = decode_cosesign1(receiptb64)

    # NOTICE: WE DO NOT VERIFY THE SIGNATURE

    # RKVST does not currently sign the message with any meaningful key. It is
    # implausible that the merkle proofs in combination with captured block
    # headers could be spoofed.

    # We MAY in future sign claims with a meaningful key to grant authority in
    # perpetuity to redeem the claim for a receipt. But once the receipt is in
    # your hands its testimony is completely independent of the RKVST platform.

    return json.loads(msg.payload)