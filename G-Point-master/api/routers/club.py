from fastapi import APIRouter

router = APIRouter()


@router.get("/club")
async def get_clubData():
    pass
@router.get("/club/list")
async def get_clubList():
    pass
@router.put("/club/update")
async def put_clubData():
    pass
@router.post("/club/register")
async def clubRegister():
    pass