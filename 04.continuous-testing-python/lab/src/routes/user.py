# lab/src/routes/user.py
from fastapi import APIRouter, HTTPException
from ..controllers import user as user_controller
from pydantic import BaseModel

router = APIRouter()

class UserIn(BaseModel):
    username: str = None
    firstname: str = None
    lastname: str = None

@router.post("/", status_code=201)
def create_user(user: UserIn):
    data = user.dict()
    result, err = user_controller.create(data)
    if err:
        raise HTTPException(status_code=400, detail={"status":"error", "message": str(err)})
    return {"status":"success"}

@router.get("/{username}")
def get_user(username: str):
    result, err = user_controller.get(username)
    if err:
        raise HTTPException(status_code=404, detail={"status":"error", "message": str(err)})
    return result