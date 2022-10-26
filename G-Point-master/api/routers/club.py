from fastapi import APIRouter
from api.classes.user import *
from api.classes.club import *
import api.schemas.club as club_schema
import glob

router = APIRouter()


@router.get("/club/{clubId}", response_model=club_schema.Club)
async def get_clubData(clubId: str):
    clubModel = getClubModel(clubId)
    return clubModel.User(clubId=clubModel.clubId, description=clubModel.description, point=clubModel.point, type=clubModel.type)


@router.get("/club/list")
async def get_clubList():
    return glob.glob(f"data/club/*.json")


@router.put("/club/update")
async def put_clubData():
    pass


@router.post("/club/register")
async def clubRegister():
    pass
