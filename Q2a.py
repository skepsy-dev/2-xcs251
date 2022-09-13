from sys import exit
from bitcoin.core.script import *

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from Q1 import send_from_P2PKH_transaction


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 2
Q2a_txout_scriptPubKey = [
        # fill this in! 1450 OP_ADD 534 == OP_SUB
    OP_DUP, OP_HASH160, my_address,
    OP_EQUALVERIFY, OP_CHECKSIG
]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = .002 # amount of BTC in the output you're sending minus fee
    txid_to_spend = (
        'a30656d04427d3f0a0394f6ed973a39c900a989956410fa86cc962347e9c6fd7')
    utxo_index = 1 # index of the output you are spending, indices start at 0
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        Q2a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)
