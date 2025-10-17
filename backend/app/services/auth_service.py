from supabase import create_client, Client
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Optional, Dict, Any
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from ..config import settings
from ..models import User
from ..schemas import UserCreate, UserLogin, TokenData


class AuthService:
    def __init__(self):
        self.supabase: Client = create_client(
            settings.supabase_url, settings.supabase_service_role_key
        )
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def create_access_token(
        self, data: dict, expires_delta: Optional[timedelta] = None
    ):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(
                minutes=settings.jwt_access_token_expire_minutes
            )
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(
            to_encode, settings.jwt_secret_key, algorithm=settings.jwt_algorithm
        )
        return encoded_jwt

    def verify_token(self, token: str) -> TokenData:
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(
                token, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm]
            )
            user_id: str = payload.get("sub")
            if user_id is None:
                raise credentials_exception
            token_data = TokenData(user_id=user_id)
        except JWTError:
            raise credentials_exception
        return token_data

    async def signup(self, user_data: UserCreate, db: Session) -> Dict[str, Any]:
        try:
            supabase_response = self.supabase.auth.sign_up(
                {
                    "email": user_data.email,
                    "password": user_data.password,
                    "options": {
                        "data": {
                            "username": user_data.username,
                            "full_name": user_data.full_name,
                        }
                    },
                }
            )

            if supabase_response.user is None:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Failed to create user",
                )

            db_user = User(
                supabase_id=supabase_response.user.id,
                email=user_data.email,
                username=user_data.username,
                full_name=user_data.full_name,
                is_active=True,
                is_verified=False,
            )
            db.add(db_user)
            db.commit()
            db.refresh(db_user)

            access_token = self.create_access_token(data={"sub": str(db_user.id)})

            return {
                "access_token": access_token,
                "token_type": "bearer",
                "user": db_user,
            }

        except Exception as e:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Registration failed: {str(e)}",
            )

    async def signin(self, user_data: UserLogin, db: Session) -> Dict[str, Any]:
        try:
            supabase_response = self.supabase.auth.sign_in_with_password(
                {"email": user_data.email, "password": user_data.password}
            )

            if supabase_response.user is None:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid credentials",
                )

            db_user = (
                db.query(User)
                .filter(User.supabase_id == supabase_response.user.id)
                .first()
            )

            if not db_user:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="User not found in database",
                )

            if not db_user.is_active:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user"
                )

            access_token = self.create_access_token(data={"sub": str(db_user.id)})

            return {
                "access_token": access_token,
                "token_type": "bearer",
                "user": db_user,
            }

        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Authentication failed: {str(e)}",
            )

    async def logout(self, token: str) -> Dict[str, str]:
        try:
            self.supabase.auth.sign_out()
            return {"message": "Successfully logged out"}
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Logout failed: {str(e)}",
            )

    def get_user_by_id(self, user_id: int, db: Session) -> Optional[User]:
        return db.query(User).filter(User.id == user_id).first()


auth_service = AuthService()
