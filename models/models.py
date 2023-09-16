from sqlalchemy import Boolean, Column, Integer ,String,Float
from config.db import Base


class Banknifty(Base):

    __tablename__ = 'banknifty'
    
    id = Column(Integer, primary_key=True, index=True)
    open_price = Column(Float)
    high_price= Column(Float)
    close_price = Column(Float)
    low_price = Column(Float)
    date_time = Column(String(100))
    volume = Column(Float, default = 0)
    

class Nifty(Base):

    __tablename__ = 'nifty'
    
    id = Column(Integer, primary_key=True, index=True)
    open_price = Column(Float)
    high_price= Column(Float)
    close_price = Column(Float)
    low_price = Column(Float)
    date_time = Column(String(100))
    volume = Column(Float, default = 0)
    


class Finnfity(Base):

    __tablename__ = 'finnifty'
    
    id = Column(Integer, primary_key=True, index=True)
    open_price = Column(Float)
    high_price= Column(Float)
    close_price = Column(Float)
    low_price = Column(Float)
    date_time = Column(String(100))
    volume = Column(Float, default = 0)
    


class MidcapNifty(Base):

    __tablename__ = 'midcapnifty'
    
    id = Column(Integer, primary_key=True, index=True)
    open_price = Column(Float)
    high_price= Column(Float)
    close_price = Column(Float)
    low_price = Column(Float)
    date_time = Column(String(100))
    volume = Column(Float, default = 0)
    

class Sensex(Base):

    __tablename__ = 'sensex'
    
    id = Column(Integer, primary_key=True, index=True)
    open_price = Column(Float)
    high_price= Column(Float)
    close_price = Column(Float)
    low_price = Column(Float)
    date_time = Column(String(100))
    volume = Column(Float, default = 0)
