from sqlite3 import Timestamp
from fastapi import APIRouter
from typing import List
import api.schemas.user as user_schema
from api.classes.user import *
from api.classes.club import *

router = APIRouter()


@router.get("/user/{userId}", response_model=user_schema.User)
async def get_userData(userId:str):
    userModel = getUserModel(userId)#user_schema.History(clubId="10",point=100, timeStamp="0:0:0")
    return user_schema.User(userId=userModel.userId, point=userModel.point, prize=userModel.prize, history=userModel.history)
@router.put("/user/{userId}/update")
async def put_userData(userId:str):
    pass
@router.put("/user/{userId}/visit")
async def visit(userId:str, visit_data:user_schema.Visit):
    userModel = getUserModel(userId)
    clubModel = getClubModel(visit_data.clubId)
    if clubModel.type==0:
        return userModel.visit(clubModel.clubId, clubModel.point)
    elif clubModel.type==1:
        if visit_data.point:
            return userModel.visit(clubModel.clubId, visit_data.point)
        else:
            pass
    elif clubModel.type==2:
        if visit_data.point and visit_data.point in clubModel.point:
            return userModel.visit(clubModel.clubId, visit_data.point)
        else:
            pass

@router.post("/user/register")
async def userRegister():
    pass