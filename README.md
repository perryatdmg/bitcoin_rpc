




# bitcoin_rpc
> Basic setup required for a Python project under Visual Studio Code that can make RPC calls to a Bitcoin node.<br/>
## Tools Required
To setup the tools required this project visit the following links:
- [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)<br/>
- [Python testing in Visual Studio Code](https://code.visualstudio.com/docs/python/testing)<br/>

This project is just a starting template for Python based projects that wish to make Bitcoin RPC calls.</br>
Python3 is recommended for use with this project: [Python 3 Installation & Setup Guide](https://realpython.com/installing-python/)

![pytest](https://github.com/perryatdmg/basic_python/blob/main/etc/img/Basic_Python.png)

## bitcoin_rpc as a template
> **bitcoin_rpc** is available as template for Python projects on github. 
## bitcoin_rpc setup
> **bitcoin_rpc** is meant to be used inside it's own environment

    sudo apt install python3.8-venv
    python3 -m venv .venv
    source .venv/bin/activate

## **NOTE** 
> To make sure that Visual Studio Code is using the same environment space as determined by 'source .venv/bin/activate' simply close the ide instance and restart it again inside a terminal:

    git clone https://github.com/perryatdmg/bitcoin_rpc.git your_project
    cd your_project
    python3 -m venv .venv
    source .venv/bin/activate
    code . 

## bitcoin_rpc with pytest
> **bitcoin_rpc** can be used with the three most popular Python unit test case frameworks but this one is using pytest by default. Therefore, (once you have your environment setup) you should add pytest to your environment. Also for the purposes of this particular project the matplotlib and numpy are also used:

    pip install -U pytest matplotlib numpy 

## bitcoin-requests 2.0.0
This Github repository makes extensive use of the pipy.org library known as **bitcoin-requests**, (version 2.0.0)
[bitcoin-requests](https://pypi.org/project/bitcoin-requests/)

	from bitcoin_requests import BitcoinRPC
	rpc = BitcoinRPC('http://127.0.0.1:18443', 'user', 'pass')
	blocks = rpc.generate(101)
	tx = rpc.sendtoaddress(address, 20)

In the above code segment, a standard URL is required along with a username and password to gain access to a Bitcoin node by way of RPC, (or **remote-procedure calls**). 

**GIVEN** that socket programming, (especially using URLs) can be complicated
**WHEN** we start of with a simple implementation of Bitcoin RPC for a given project
**THEN** we can verify our steps towards more complicated applications

## The Plan
We will develop bitcoin_rpc in the following manner:

 1. Testing it on an instance of **bitcoind** running on the same Linux box
 2. Testing it on an instance of **bitcoind** running on the two different Linux boxes, (same machine)
 3. Testing it on an instance of **bitcoind** running on the two different Linux boxes, (different  machines)
 4.  Testing it on an instance of **bitcoind** running on the two different Linux boxes across the Internet

## Bitcoin
In order to use the bitcoin_rpc package you will need a Bitcoin Node running to make RPC calls against. The parameters for running a Bitcoin Node in testmode are as follows:

The following parameters have to be set:
#### **NETWORK-RELATED**  **SETTINGS**
	   **testnet=**['1'|'0']
              Enable or disable run on the test network instead of the real *bitcoin* network.

       **proxy=**'127.0.0.1:9050'
              Connect via a socks4 proxy.

       **addnode=**'10.0.0.2:8333'
              Use as many *addnode=* settings as you like to connect to specific peers.

       **connect=**'10.0.0.1:8333'
              Use as many *connect=* settings as you like to connect ONLY to specific peers.

       **noirc=**['1'|'0']
              Use  or  Do  not  use  Internet Relay Chat (irc.lfnet.org #bitcoin channel) to find
              other peers.

       maxconnections='value'
              Maximum number of inbound+outbound connections.

#### **JSON-RPC**  **OPTIONS**

	   **server=**['1'|'0']
	              Tells *bitcoin* to accept or not accept JSON-RPC commands.

       **rpcuser=**'username'
              You must set *rpcuser* to secure the JSON-RPC api.

       **rpcpassword=**'password'
              You must set *rpcpassword* to secure the JSON-RPC api.

       **rpctimeout=**'30'
              How many seconds *bitcoin* will wait for a complete RPC  HTTP  request,  after  the
              HTTP connection is established.

       **rpcallowip=**'192.168.1.*'
              By  default,  only  RPC  connections  from  localhost  are allowed. Specify as many
              *rpcallowip=* settings as you like to allow connections from other hosts  (and  you
              may use * as a wildcard character).

       **rpcport=**'8332'
              Listen for RPC connections on this TCP port.

       **rpcconnect=**'127.0.0.1'
              You  can use *bitcoin* or *[bitcoind](http://manpages.ubuntu.com/manpages/precise/en/man1/bitcoind.1.html)(1)* to send commands to *bitcoin*/*[bitcoind](http://manpages.ubuntu.com/manpages/precise/en/man1/bitcoind.1.html)(1)*
              running on another host using this option.

       **rpcssl=**'1'
              Use Secure Sockets Layer (also known as TLS or HTTPS) to communicate with *bitcoin*
              '-server' or *[bitcoind](http://manpages.ubuntu.com/manpages/precise/en/man1/bitcoind.1.html)(1)*. Example of OpenSSL settings used when *rpcssl*='1':

       **rpcsslciphers=**'TLSv1+HIGH:!SSLv2:!aNULL:!eNULL:!AH:!3DES:@STRENGTH'

       **rpcsslcertificatechainfile=**'server.cert'

       **rpcsslprivatekeyfile=**'server.pem'

       **MISCELLANEOUS** **OPTIONS**

       **gen=**['0'|'1']
              Enable or disable attempt to generate bitcoins.

       **4way=**['0'|'1']
              Enable or disable use SSE instructions to try to generate bitcoins faster.

       **keypool=**'100'
              Pre-generate  this  many  public/private key pairs, so wallet backups will be valid
              for both prior transactions and several dozen future transactions.

       **paytxfee=**'0.00'
              Pay an optional transaction fee every time you  send  bitcoins.  Transactions  with
              fees  are more likely than free transactions to be included in generated blocks, so
              may be validated sooner.

       **allowreceivebyip=**'1'
              Allow direct connections for the 'pay via IP address' feature.

       **USER** **INTERFACE** **OPTIONS**

       **min=**['0'|'1']
              Enable or disable start bitcoind minimized.

       **minimizetotray=**['0'|'1']
              Enable or disable minimize to the system tray.
              
## Why use an IDE?
> The following are examples of (pytest) debugging Python inside Visual Studio Code:


Here we have your typical Python source code, (as methods) to be unit tested:
![pytest](https://github.com/perryatdmg/basic_python/blob/main/etc/img/000.png)</br>
### Here we have at least one unit test per method:
![pytest](https://github.com/perryatdmg/basic_python/blob/main/etc/img/007.png)</br>
### In this case a unit test has indicated that a Python method is not returning as expected value, (which is the purpose of writing test cases). In response the Visual Studio Code IDE with the Python extension interacting with the Pytest framework shows us which test case has an issue:
![pytest](https://github.com/perryatdmg/basic_python/blob/main/etc/img/001.png)</br>
### The benefits of using an IDE such as Visual Studio Code are that, (the trained eye) can quickly see which unit tests are reporting a pass, (in green) and which unit tests are indicating an issue, (in red):
![pytest](https://github.com/perryatdmg/basic_python/blob/main/etc/img/002.png)</br>
### Additionally, the editor portion shows the unit test case, (that requires attention) with an additional "red line":
![pytest](https://github.com/perryatdmg/basic_python/blob/main/etc/img/003.png)</br>
### In the console/terminal portion of the screen, the actual report from the pytest framework is supplied to the software developer, (in blue):
![pytest](https://github.com/perryatdmg/basic_python/blob/main/etc/img/004.png)</br>
### Here is a menu of operations that can be conducted easily using the Pytest extension for Visual Studio Code. Notice that the test case causing the issue was mistaken in the value expected from our Python code, (aka. a value of 4 when it should be 2).
![pytest](https://github.com/perryatdmg/basic_python/blob/main/etc/img/007.png)</br>
### Once the correction has been made, the IDE updates almost immediately, (no manual running or recompiling or the Python code necessary), the editor showing no errors:
![pytest](https://github.com/perryatdmg/basic_python/blob/main/etc/img/008.png)</br>
### With the IDE we can set breakpoints and catch the code at the precise line of source requiring our attention:
![pytest](https://github.com/perryatdmg/basic_python/blob/main/etc/img/010.png)</br>
### Resulting in a fully operational test case suite, (or all green):
![pytest](https://github.com/perryatdmg/basic_python/blob/main/etc/img/012.png)</br>
### Further, the console report is now reporting no errors:
![pytest](https://github.com/perryatdmg/basic_python/blob/main/etc/img/009.png)</br>

