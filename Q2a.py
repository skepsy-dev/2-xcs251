from sys import exit
from bitcoin.core.script import *

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from Q1 import send_from_P2PKH_transaction


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 2
Q2a_txout_scriptPubKey = [
        # fill this in! x==1450 y==534 
    OP_2DUP, OP_ADD, 1984, OP_EQUALVERIFY, OP_SUB, 916, OP_EQUALVERIFY 
]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.0003  # amount of BTC in the output you're sending minus fee
    txid_to_spend = (
        'f2441dba1d8215f2bde270aac9e5dc4363092620d57f76ecbd22c18e94d4ce86')
    utxo_index = 0 # index of the output you are spending, indices start at 0
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        Q2a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)
