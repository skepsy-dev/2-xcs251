from bitcoin.core.script import *

######################################################################
# These functions will be used by Alice and Bob to send their respective
# coins to a utxo that is redeemable either of two cases:
# 1) Recipient provides x such that hash(x) = hash of secret
#    and recipient signs the transaction.
# 2) Sender and recipient both sign transaction
#
# TODO: Fill these in to create scripts that are redeemable by both
#       of the above conditions.
# See this page for opcode documentation: https://en.bitcoin.it/wiki/Script

# This is the ScriptPubKey for the swap transaction
def coinExchangeScript(public_key_sender, public_key_recipient, hash_of_secret):
    return [
        # fill this in!
        OP_IF,
            OP_2, public_key_recipient, hash_of_secret, OP_2, OP_EQUALVERIFY, OP_CHECKMULTISIG,
        OP_ELSE,
        alice_locktime, bob_locktime, OP_CHECKLOCKTIMEVERIFY, OP_DROP,
        OP_ENDIF,
            OP_2, public_key_recipient, public_key_sender, OP_2, OP_EQUALVERIFY, OP_CHECKMULTISIG
    ]

# This is the ScriptSig that the receiver will use to redeem coins
def coinExchangeScriptSig1(sig_recipient, secret):
    return [
        # fill this in!
        0, sig_recipient, OP_HASH160, secret, coinExchangeScript
    ]

# This is the ScriptSig for sending coins back to the sender if unredeemed
def coinExchangeScriptSig2(sig_sender, sig_recipient):
    return [
        # fill this in!
        0, sig_recipient, sig_sender, coinExchangeScript
    ]
######################################################################

######################################################################
#
# Configured for your addresses
#
# TODO: Fill in all of these fields
#

alice_txid_to_spend     = "d9618342ddb1f2210837aba8c7c99b30481eedc354aad9e7b3f4edd5bbaffece"
alice_utxo_index        = 0
alice_amount_to_send    = 0.00002

bob_txid_to_spend       = "6f6837f0c385584539e89c7dc72d3f8d6fa67b44e77d6e40c2ab4b5eff251afe"
bob_utxo_index          = 0
bob_amount_to_send      = 0.0002

# Get current block height (for locktime) in 'height' parameter for each blockchain (will be used in swap.py):
#  curl https://api.blockcypher.com/v1/btc/test3
btc_test3_chain_height = 2347736

#  curl https://api.blockcypher.com/v1/bcy/test
bcy_test_chain_height = 471165

# Parameter for how long Alice/Bob should have to wait before they can take back their coins
# alice_locktime MUST be > bob_locktime
alice_locktime = 5
bob_locktime = 3

tx_fee = 0.0001

# While testing your code, you can edit these variables to see if your
# transaction can be broadcasted succesfully.
broadcast_transactions = False
alice_redeems = False

######################################################################
