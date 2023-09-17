from fastapi import APIRouter, Depends , HTTPException
from models.models import Nifty,Banknifty
from schema.schema import *
from utils.kite_trade import *
from sqlalchemy.orm import Session
from config.db import SessionLocal
from utils.common_util import *
from typing import List

trading = APIRouter()


@trading.get("/ltp")
async def get_ltp(symbol:str):
    """
        This API returns the Latest Traded Price (LTP) for the given <br/>
     <b> symbol = "NSE:NIFTY BANK" <br/> symbol = "NSE:NIFTY 50" </b>
    """
    ltp = ltp_calculator(symbol)
    return f" the latest price for {symbol} is  : {ltp}"



@trading.get("/long_position")
async def long_position(stoploss:int, support:int, resistance:int,quantity:int,strike_price: int ,symbol:str):
    '''
        <b>stoploss < ltp < support < resistance </b>

        This api will place long position and will track for taget and stoploss
        <br/>while taking trade <br> <b> LTP <= SUPPORT </b> 
        <br/>
        <b>STOPLOSS < SUPPORT </b>
        <br/> 
        
        while taking exit <br/> <br/><b> LTP >= RESISTNACE </b> <br/>
         for stoploss hit  <br/> <br/> <b> LTP <= STOPLOSS </b> 


       <b> symbol = "NSE:NIFTY BANK" symbol = "NSE:NIFTY 50" </b>

    '''

    while True:
        ltp = ltp_calculator(symbol)
        time.sleep(0.9)

        
        if ltp <= support:
            #Place Buy Order
            try:
            
                buy_order = kite.place_order(variety=kite.VARIETY_REGULAR,
                                        exchange=kite.EXCHANGE_NFO,
                                        tradingsymbol=tradingsymbol_maker(symbol,strike_price)+"CE",
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
                                        tag="Saurav Kumar")
            except Exception as e:
                return f"An occoured due to {e}"
            break
    # for placing Sell order 
  
    while True:
        ltp = ltp_calculator()
        
        if ltp >= resistance or ltp < stoploss:
            #Place SELL Order
            try:
                sell_order = kite.place_order(variety=kite.VARIETY_REGULAR,
                                        exchange=kite.EXCHANGE_NFO,
                                        tradingsymbol=tradingsymbol_maker(symbol,strike_price)+"CE",
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
                                        tag="Saurav Kumar")

                print(sell_order)
            except Exception as e:
                return f"An occoured due to {e}"
            break
                
        return "Trade complete success fully"
    



@trading.get("/short_position")
async def short_position(resistance:int ,support:int,stoploss:int,quantity:int,strike_price:int ,symbol:str):
    '''
        <b> resistance <support <ltp < stoploss </b>
        This api will place short position and will track for taget and stoploss
       

        <b>
        while take trade
            STOPLOSS > SUPPORT,
            LTP >= SUPPORT


        while exit trade
        LTP <= RESISTANCE or  STOPLOSS > LTP


        </b>


       <b> symbol = "NSE:NIFTY BANK" symbol = "NSE:NIFTY 50" </b>

    '''


    if stoploss > support:      
        while True:
            ltp = ltp_calculator()
            time.sleep(0.9)

            
            if ltp >= support:
                #Place Buy Order
                try:
                    buy_order = kite.place_order(variety=kite.VARIETY_REGULAR,
                                            exchange=kite.EXCHANGE_NFO,
                                            tradingsymbol=tradingsymbol_maker(symbol,strike_price)+"PE",
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
                except Exception as e:
                    return f"An occoured due to {e}"   
                
                break 


# For the order
    
    while True:
        ltp = ltp_calculator()
        
        if ltp <= resistance or ltp < stoploss :
            #Place SELL Order
            try: 
                sell_order = kite.place_order(variety=kite.VARIETY_REGULAR,
                                        exchange=kite.EXCHANGE_NFO,
                                        tradingsymbol=tradingsymbol_maker(symbol,strike_price)+"PE",
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
            except Exception as e:
                return f"An occoured due to {e}"
            
            break
        return " Trade completed succesfully"





@trading.get('/data_upload')
async def dataupload(symbol:str):

    '''
        This API will add the data in database every second for the given loop
        symbol = "NSE:NIFTY BANK"
        symbol = "NSE:NIFTY 50"
        BSE:SENSEX
    '''

    while True:
        data  = get_ohlc_data(symbol=symbol)
        
        try:
            with SessionLocal() as session:
                if symbol == "NSE:NIFTY BANK":
                    data = Banknifty(open_price=data.get("open_price"),
                                                high_price=data.get("high_price"),
                                                low_price=data.get("low_price"),
                                                close_price=data.get("close_price"),
                                                date_time=data.get("date_time"))
                    
                elif symbol == "NSE:NIFTY 50":

                    data = Nifty(open_price=data.get("open_price"),
                                                high_price=data.get("high_price"),
                                                low_price=data.get("low_price"),
                                                close_price=data.get("close_price"),
                                                date_time=data.get("date_time"))
                
            
            
                session.add(data)
            
                session.commit()

        except Exception as e:
            print("An Error occoured",e)
            break
            
    return "data added successfully"

import talib

@trading.get('/get_banknifty_data/}')
async def get_banknifty_data():

    '''
        This API will fetch the data from database every second for the given loop
        symbol = "NSE:NIFTY BANK"
        symbol = "NSE:NIFTY 50"
        BSE:SENSEX
    '''
    
    with SessionLocal() as session:
        items = session.query(Banknifty).all()
        items = list(items)
        close_price = [i.close_price for i in items]
        return close_price




@trading.get('/get_nifty_data/}')
async def get_nifty_data():

    '''
        This API will fetch the data from database every second for the given loop
        symbol = "NSE:NIFTY BANK"
        symbol = "NSE:NIFTY 50"
        BSE:SENSEX
    '''
    
    with SessionLocal() as session:
        items = session.query(Nifty).all()
        return items