#INF601 - Advanced Programming in Python
#Braxten Eilert
#Mini Project 1

#Install and import yfinance, numpy, matplotlib

#Example
#Pip install yfinance
#import yfinance as yf

#plot 5 tickers last 10 day adj close price

#bring data from yf
#'data = yf.download("LNG", start="2022-09-01", end="2022-09-16")'

#append the price
#for price in data['Adj Close']:
#    lngPrices.append(price)

#create a list
#lngPrices = []

#convert list to numpy array
#lngarray = np.array([lngPrices])

#plot array in matplotlib (plt was not defined for me even with numpy and matplotlib installed?)
#plt.plot(lngarray)