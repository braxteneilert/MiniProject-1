#INF601 - Advanced Programming in Python
#Braxten Eilert
#Mini Project 1

import yfinance as yf

data = yf.download("LNG", start="2022-09-01", end="2022-09-16")
print(data['Adj Close'])

lngPrices = []

for price in data['Adj Close']:
    lngPrices.append(price)

print(lngPrices)