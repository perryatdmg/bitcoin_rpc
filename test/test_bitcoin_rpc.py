# import sys
# sys.path.insert(0, '../src')
from src import bitcoin_rpc    # The code to test
 
# Testing BitcoinRPC
def test_bitcoindrpc():
    assert bitcoin_rpc.bitcoindrpc()>0
