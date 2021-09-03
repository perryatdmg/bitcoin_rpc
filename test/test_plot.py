# import sys
# sys.path.insert(0, '../src')
from src import standardplot    # The code to test

def test_data():
    assert standardplot.data(0, 20, 100).size()>0

def test_plot():
    assert standardplot.plot().size()>0
  

# test_data()
