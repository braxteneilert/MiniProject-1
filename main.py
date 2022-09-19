# INF601 - Advanced Programming in Python
# Braxten Eilert
# Mini Project 1

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

# Get last 10 days adj close data.
data = yf.download("LNG", start="2022-09-01", end="2022-09-16")


# Create a list.
lngPrices = []

for price in data['Adj Close']:
    lngPrices.append(price)

print(lngPrices)

# Create a numpy array.
#lngarray = np.array(lngPrices)

# Show and create matplotlib chart from array

#plt.plot(lngarray)
#plt.show()
