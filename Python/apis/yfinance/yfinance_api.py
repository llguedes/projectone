import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data, wb

import matplotlib
matplotlib.rcParams['figure.figsize'] = (15,7)

import yfinance as yf
#yf.pdr_override()

ibov = data.DataReader()
#ibov.head()
#ibov.tail()

ibov["Close"].plot()

