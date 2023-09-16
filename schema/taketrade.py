from pydantic import BaseModel

class TakeTrade(BaseModel):
    support_price : int
    resistance_price: int
    stoploss_price: int
    quantity : int
    long_position: bool

