from fastapi import APIRouter, HTTPException, Depends
from app.auth.schemas import UserCreate, UserLogin
from app.auth.utils import register_user, authenticate_user
from app.auth.models import User
from app.database import get_session

router = APIRouter()

@router.post("/register")
async def register(user: UserCreate, session=Depends(get_session)):
    await register_user(user, session)
    return {"message": "User registered successfully"}

@router.post("/login")
async def login(user: UserLogin, session=Depends(get_session)):
    user_data = await authenticate_user(user, session)
    if not user_data:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful", "user": user_data}

@router.post("/logout")
async def logout():
    return {"message": "Logged out successfully"}
