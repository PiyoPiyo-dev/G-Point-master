from sqlite3 import Timestamp
from fastapi import APIRouter
from typing import List
import api.schemas.user as user_schema
from api.classes.user import *

router = APIRouter()


@router.get("/user/{userId}", response_model=user_schema.User)
async def get_userData(userId:str):
    userModel = getUserModel(userId)#user_schema.History(clubId="10",point=100, timeStamp="0:0:0")
    return user_schema.User(userId=userModel.userId, point=userModel.point, prize=userModel.prize, history=userModel.history)
@router.put("/user/{userId}/update")
async def put_userData(userId:str):
    pass
@router.put("/user/visit")
async def visit():
    pass
@router.post("/user/register")
async def userRegister():
    pass