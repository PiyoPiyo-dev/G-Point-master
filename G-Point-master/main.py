from fastapi import FastAPI
from api.routers import club, user

app = FastAPI()
app.include_router(club.router)
app.include_router(user.router)
print(app)
