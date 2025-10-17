from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime


class UserBase(BaseModel):
    email: EmailStr
    username: Optional[str] = None
    full_name: Optional[str] = None


class UserCreate(UserBase):
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class WalletConnect(BaseModel):
    address: str
    signature: str
    message: str


class UserResponse(UserBase):
    id: int
    supabase_id: str
    is_active: bool
    is_verified: bool
    created_at: datetime
    wallets: List["WalletResponse"] = []

    class Config:
        from_attributes = True


class WalletResponse(BaseModel):
    id: int
    address: str
    wallet_type: str
    is_primary: bool
    created_at: datetime

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str
    user: UserResponse


class TokenData(BaseModel):
    user_id: Optional[int] = None
