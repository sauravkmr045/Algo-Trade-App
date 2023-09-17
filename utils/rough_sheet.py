# Basic calls
# print(kite.margins())
# print(kite.orders())
# print(kite.positions())

# Get instrument or exchange
# print(kite.instruments())
# print(kite.instruments("NSE"))
# print(kite.instruments("NFO"))

# Get Live Data
#print(kite.ltp("NSE:RELIANCE"))
 
#print(kite.quote(["NSE:NIFTY BANK", "NSE:ACC", "NFO:NIFTY22SEPFUT"]))
import numpy as np
import pandas as pd
import talib

# Create sample data
data = pd.DataFrame({
    'Date': pd.date_range(start='2022-01-01', periods=100, freq='D'),
    'Open': np.random.rand(100) * 100,
    'High': np.random.rand(100) * 100,
    'Low': np.random.rand(100) * 100,
    'Close': np.random.rand(100) * 100,
    'Volume': np.random.randint(1000, 10000, size=100)
})

# Calculate moving averages using TA-Lib
data['SMA_10'] = talib.SMA(data['Close'], timeperiod=10)
data['SMA_20'] = talib.SMA(data['Close'], timeperiod=20)

# Calculate Relative Strength Index (RSI)
data['RSI'] = talib.RSI(data['Close'], timeperiod=14)

# Calculate Moving Average Convergence Divergence (MACD)
macd, signal, _ = talib.MACD(data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
data['MACD'] = macd
data['MACD_Signal'] = signal

# Display the resulting DataFrame
print(data.tail())







#print(get_ohlc_data())






# import sys

# # Store the original sys.stdout
# original_stdout = sys.stdout

# # Open a file in write mode
# with open('output.txt', 'w') as file:
#     # Redirect sys.stdout to the file
#     sys.stdout = file

#     # Your Python program code here
#     print(kite.instruments())

# # Restore sys.stdout to its original value
# sys.stdout = original_stdout