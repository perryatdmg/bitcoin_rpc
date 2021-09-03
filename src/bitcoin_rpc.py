from bitcoin_requests import BitcoinRPC

def bitcoindrpc():
    rpc = BitcoinRPC('http://75.157.6.175:4000', 'user', 'pass')
    blocks = rpc.generate(101)
    # tx = rpc.sendtoaddress(address, 20) 
    return 1
    

