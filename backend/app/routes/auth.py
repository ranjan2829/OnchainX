from fastapi import APIRouter, Depends, HTTPException, status, Header
from sqlalchemy.orm import Session
from typing import Dict, Any

from ..database import get_db
from ..schemas import UserCreate, UserLogin, Token, UserResponse
from ..services.auth_service import auth_service

router = APIRouter(prefix="/auth", tags=["authentication"])


@router.post("/signup", response_model=Token)
async def signup(user_data: UserCreate, db: Session = Depends(get_db)):
    try:
        result = await auth_service.signup(user_data, db)
        return Token(**result)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Signup failed: {str(e)}"
        )


@router.post("/signin", response_model=Token)
async def signin(user_data: UserLogin, db: Session = Depends(get_db)):
    try:
        result = await auth_service.signin(user_data, db)
        return Token(**result)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Signin failed: {str(e)}"
        )


@router.post("/logout")
async def logout():
    try:
        result = await auth_service.logout("")
        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Logout failed: {str(e)}"
        )


def get_token_from_header(authorization: str = Header(None)) -> str:
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing or invalid authorization header"
        )
    return authorization.split(" ")[1]


def get_current_user_id(token: str = Depends(get_token_from_header)) -> int:
    try:
        token_data = auth_service.verify_token(token)
        return int(token_data.user_id)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )


@router.get("/me", response_model=UserResponse)
async def get_current_user(
    current_user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db)
):
    user = auth_service.get_user_by_id(current_user_id, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user