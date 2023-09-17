from fastapi import FastAPI
from routes.order_placing import trading
from config.db import Base,engine

app = FastAPI()


app.include_router(trading)




Base.metadata.create_all(bind=engine)