# INF601 - Advanced Programming in Python
# Braxten Eilert
# Mini Project 1

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

#1
# Get last 10 days adj close data.
data = yf.download("TLT", start="2022-09-01", end="2022-09-16")

# Create a list.
tltPrices = []

for price in data['Adj Close']:
    tltPrices.append(price)

print(tltPrices)

#2
#Get last 10 days adj close data.
data = yf.download("LNG", start="2022-09-01", end="2022-09-16")

# Create a list.
lngPrices = []

for price in data['Adj Close']:
    lngPrices.append(price)

print(lngPrices)

#3
#Get last 10 days adj close data.
data = yf.download("KWEB", start="2022-09-01", end="2022-09-16")

# Create a list.
kwebPrices = []

for price in data['Adj Close']:
    kwebPrices.append(price)

print(kwebPrices)

#4
#Get last 10 days adj close data.
data = yf.download("AAPl", start="2022-09-01", end="2022-09-16")

# Create a list.
aaplPrices = []

for price in data['Adj Close']:
    aaplPrices.append(price)

print(aaplPrices)

#5
#Get last 10 days adj close data.
data = yf.download("XOM", start="2022-09-01", end="2022-09-16")

# Create a list.
xomPrices = []

for price in data['Adj Close']:
    xomPrices.append(price)

print(xomPrices)


# Create a numpy array.
lngarray = np.array([lngPrices])
xomarray = np.array([xomPrices])
tltarray = np.array([tltPrices])
aaplarray = np.array([aaplPrices])
kwebarray = np.array([kwebPrices])
# Show and create matplotlib chart from array
plt.plot(lngarray, xomarray, tltarray, aaplarray, kwebarray)
plt.show()
