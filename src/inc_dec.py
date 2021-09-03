def increment(x):
    return x + 1

def decrement(x):
    return x - 1

from bitcoin_requests import BitcoinRPC

def bitcoindrpc():
    rpc = BitcoinRPC('http://75.157.6.175:18443', '', '')
    blocks = rpc.generate(101)
    # tx = rpc.sendtoaddress(address, 20) 
    return 1
    

