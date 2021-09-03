import matplotlib.pyplot as plt
import numpy as np

def data(a,b,c):
    x = np.linspace(a,b,c) 
    print(x)# Create a list of evenly-spaced numbers over the range
    return x

def plot():
    y = data(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
    plt.plot(y, np.sin(y))       # Plot the sine of each x point
    plt.show()                   # Display the plot
    print(y)
    return y

