from kite_trade import *
import pandas as pd

enctoken = "va0JEHdpLnAJtcSundBrdLap8Ejb3nQyOzHEGOtU9uf+oxTvhrHJ1ZVaefiFNbZjqoUBo/BayJblc7jSWAq5junb8ox2S/WcGXkH0oxkaiPOLibezB/veg=="
kite = KiteApp(enctoken=enctoken)

'''
Need to enter support value always lesser than resistance
'''

import time
import pandas as pd
print(kite.quote("NSE:NIFTY BANK"))
strike_price = input("please enter the strike price : ")
support = int(input("enter the support price : "))
resistance = int(input("enter the resisitance price : "))
option_buying = input("do you want to buy the CE Yes or No ").lower()
quantity = int(input("enter the quantity : "))
stoploss = int(input("Enter the stoploss price: "))


def ltp_calculator(symbol="NSE:NIFTY BANK"):
    #symbol = "NSE:NIFTY BANK"
    #symbol = "NSE:NIFTY 50"
    data =kite.ltp([ "NSE:NIFTY BANK"])
    time.sleep(1)
    ltp = bank_nifty_latest_price = data.get(symbol).get('last_price')
    print("latest price of ", symbol,"  : ",ltp, "support : " ,support, "resisitance : ", resistance, 'stoploss : ' ,stoploss)
    return ltp


def tradingsymbol_maker():
    if option_buying == 'yes':
        tradingsymbol = "BANKNIFTY23920"+strike_price + "CE"
    else:
        tradingsymbol = "BANKNIFTY23920"+strike_price + "PE"
    return tradingsymbol

tradingsymbol = tradingsymbol_maker()


#============================For Long Position===================================
if option_buying == "yes" and support > stoploss:
    while True:
        ltp = ltp_calculator()

        
        if ltp <= support:
            #Place Buy Order
            
            buy_order = kite.place_order(variety=kite.VARIETY_REGULAR,
                                    exchange=kite.EXCHANGE_NFO,
                                    tradingsymbol=tradingsymbol,
                                    transaction_type=kite.TRANSACTION_TYPE_BUY,
                                    quantity=quantity,
                                    product=kite.PRODUCT_MIS,
                                    order_type=kite.ORDER_TYPE_MARKET,
                                    price=None,
                                    validity=None,
                                    disclosed_quantity=None,
                                    trigger_price=None,
                                    squareoff=None,
                                    stoploss=None,
                                    trailing_stoploss=None,
                                    tag="Suman Kumar")
            
            print(buy_order)
            break 
    # for placing Sell order 
  
    while True:
        ltp = ltp_calculator()
        
        if ltp >= resistance or ltp < stoploss:
            #Place SELL Order
            
            sell_order = kite.place_order(variety=kite.VARIETY_REGULAR,
                                    exchange=kite.EXCHANGE_NFO,
                                    tradingsymbol=tradingsymbol,
                                    transaction_type=kite.TRANSACTION_TYPE_SELL,
                                    quantity=quantity,
                                    product=kite.PRODUCT_MIS,
                                    order_type=kite.ORDER_TYPE_MARKET,
                                    price=None,
                                    validity=None,
                                    disclosed_quantity=None,
                                    trigger_price=None,
                                    squareoff=None,
                                    stoploss=None,
                                    trailing_stoploss=None,
                                    tag="Suman Kumar")

            print(sell_order)
            break

        #=====================Short Selling=====================================

# for placing buy order  
if option_buying == "no" and stoploss > resistance:      
    while True:
        ltp = ltp_calculator()

        
        if ltp >= resistance:
            #Place Buy Order
            
            buy_order = kite.place_order(variety=kite.VARIETY_REGULAR,
                                    exchange=kite.EXCHANGE_NFO,
                                    tradingsymbol=tradingsymbol,
                                    transaction_type=kite.TRANSACTION_TYPE_BUY,
                                    quantity=quantity,
                                    product=kite.PRODUCT_MIS,
                                    order_type=kite.ORDER_TYPE_MARKET,
                                    price=None,
                                    validity=None,
                                    disclosed_quantity=None,
                                    trigger_price=None,
                                    squareoff=None,
                                    stoploss=None,
                                    trailing_stoploss=None,
                                    tag="Suman Kumar")
            
            print(buy_order)
            break 


# For the order
    
    while True:
        ltp = ltp_calculator()
        
        if ltp <= support or ltp >stoploss :
            #Place SELL Order
            
            sell_order = kite.place_order(variety=kite.VARIETY_REGULAR,
                                    exchange=kite.EXCHANGE_NFO,
                                    tradingsymbol=tradingsymbol,
                                    transaction_type=kite.TRANSACTION_TYPE_SELL,
                                    quantity=quantity,
                                    product=kite.PRODUCT_MIS,
                                    order_type=kite.ORDER_TYPE_MARKET,
                                    price=None,
                                    validity=None,
                                    disclosed_quantity=None,
                                    trigger_price=None,
                                    squareoff=None,
                                    stoploss=None,
                                    trailing_stoploss=None,
                                    tag="Suman Kumar")

            print(sell_order)
            break