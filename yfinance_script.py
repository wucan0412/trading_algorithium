# -*- coding: utf-8 -*-
"""
Getting data Using yfinance library

@author: Mayank Rasu (http://rasuquant.com/wp/)
"""

import yfinance as yf

# get ohlcv data for any ticker by period.
#data1 = yf.download("MSFT", period='1mo', interval="5m")

 #get ohlcv data for any ticker by start date and end date
#data2 = yf.download("MSFT", start="2020-01-01", end="2020-05-22",interval="1h")

# get intraday data for any ticker by period.
#data3 = yf.download("MSFT", period='1mo', interval="5m")

msft = yf.Ticker("msft")
#print(msft.major_holders)
a=msft.cashflow
print(a)
