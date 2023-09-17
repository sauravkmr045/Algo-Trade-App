from pydantic import BaseModel

# class TakeTrade(BaseModel):
#     support_price : int
#     resistance_price: int
#     stoploss_price: int
#     quantity : int
#     long_position: bool

class GetData(BaseModel):
    open_price: int
    high_price: int
    low_price:int
    close_price:int
   