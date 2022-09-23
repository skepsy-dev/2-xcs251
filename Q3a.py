from sys import exit
from bitcoin.core.script import *
from bitcoin.wallet import CBitcoinSecret

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from Q1 import send_from_P2PKH_transaction


cust1_private_key = CBitcoinSecret(
    'cNexQ6jqmR68QMxaMUeApmH4HLubn6tTbPeeDCY2fPu43NYatorA')
cust1_public_key = cust1_private_key.pub
cust2_private_key = CBitcoinSecret(
    'cUyLGv7YEqHhaZxVUXu7w6PFba7coDTGaWsrG4KBhrPyuBWDcujd')
cust2_public_key = cust2_private_key.pub
cust3_private_key = CBitcoinSecret(
    'cRZxzWjz8UYQwn78qg89ueafjXVr6nA4Zbh5Lm32qdQ1qS4th8hn')
cust3_public_key = cust3_private_key.pub


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 3

# You can assume the role of the bank for the purposes of this problem
# and use my_public_key and my_private_key in lieu of bank_public_key and
# bank_private_key.

Q3a_txout_scriptPubKey = [
        # fill this in!
        my_public_key, OP_CHECKSIGVERIFY, OP_1, cust1_public_key, cust2_public_key, 
        cust3_public_key, OP_3, OP_CHECKMULTISIG
]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = .002 # amount of BTC in the output you're sending minus fee
    txid_to_spend = (
        'a30656d04427d3f0a0394f6ed973a39c900a989956410fa86cc962347e9c6fd7')
    utxo_index = 3 # index of the output you are spending, indices start at 0
    ######################################################################

    response = send_from_P2PKH_transaction(amount_to_send, txid_to_spend, 
        utxo_index, Q3a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)
