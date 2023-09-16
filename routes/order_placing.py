from fastapi import APIRouter
from models.models import *
from schema.taketrade import *

trading = APIRouter()


@trading.get("/ltp")
async def get_ltp():
    
    return "ltp"