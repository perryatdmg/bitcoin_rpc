



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

