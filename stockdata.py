import yfinance as yf
import pandas as pd
import numpy as np

def getOHLCV(ticker, interval='1d', period='1y', start=None, end=None):
    """
        :Parameters:
            period : str
                Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
                Either Use period parameter or use start and end
            interval : str
                Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
                Intraday data cannot extend last 60 days
            start: str
                Download start date string (YYYY-MM-DD) or _datetime.
                Default is 1900-01-01
            end: str
                Download end date string (YYYY-MM-DD) or _datetime.
                Default is now		
    """
    df = yf.Ticker(ticker).history(period=period, interval=interval, start=start, end=end)
    df.index = df.index.to_period('D')
    return df