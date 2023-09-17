from sqlalchemy import Boolean, Column, Integer ,String,Float
from config.db import Base


class Banknifty(Base):

    __tablename__ = 'Banknifty'
    
    id = Column(Integer, primary_key=True, index=True)
    open_price = Column(Float)
    high_price= Column(Float)
    low_price = Column(Float)
    close_price = Column(Float)
    date_time = Column(String(100))
    volume = Column(Float, default = 0)
    

class Nifty(Base):

    __tablename__ = 'Nifty'
    
    id = Column(Integer, primary_key=True, index=True)
    open_price = Column(Float)
    high_price= Column(Float)
    low_price = Column(Float)
    close_price = Column(Float)
    date_time = Column(String(100))
    volume = Column(Float, default = 0)
    

