import time
from utils.kite_trade import KiteApp
from env import enctoken

# enctoken = "xHM+jxac3jC5T4yOcWCr2OSKHTHmAITCFi2/pZCRlAy3KUY2k7cifqRQ/ahS6L3WXI+m4Ii9m2vvayjJIUePvLiaJd7Ew3mqtmqS+D7AELIbsQwrTyccaw=="

kite = KiteApp(enctoken=enctoken)


def get_ohlc_data(symbol="NSE:NIFTY BANK"):
    data = kite.quote(symbol)
    
    time.sleep(1)
    
    bank_nifty_ohlc_data = {"open_price": data.get(symbol).get("ohlc").get("open"),
                 "high_price": data.get(symbol).get("ohlc").get("high"),
                 "low_price": data.get(symbol).get("ohlc").get("low"),
                 "close_price": data.get(symbol).get("ohlc").get("close"),
                 "date_time": data.get(symbol).get("timestamp")
                 }
    
 

    return bank_nifty_ohlc_data  


def ltp_calculator(symbol="NSE:NIFTY BANK"):
    
    data =kite.ltp([ symbol])
    
    ltp  = data.get(symbol).get('last_price')
    print("latest price of ", symbol,"  : ",ltp,)
    return ltp


def tradingsymbol_maker(symbol="NSE:NIFTY BANK" ,strike_price=0):
    if symbol == "NSE:NIFTY BANK":
    
        tradingsymbol = "BANKNIFTY" +"23920" +str(strike_price) 
    elif symbol == "NSE:NIFTY":
        tradingsymbol = "NIFTY" +"23920" +str(strike_price)

    
    return tradingsymbol



    

