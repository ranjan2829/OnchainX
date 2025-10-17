from sqlalchemy.orm import Session
from typing import Optional, List
from ..models import User, Wallet
from ..schemas import UserCreate, WalletConnect


class DatabaseService:
    def __init__(self):
        pass

    def get_user_by_email(self, db: Session, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

    def get_user_by_supabase_id(self, db: Session, supabase_id: str) -> Optional[User]:
        return db.query(User).filter(User.supabase_id == supabase_id).first()

    def get_user_by_id(self, db: Session, user_id: int) -> Optional[User]:
        return db.query(User).filter(User.id == user_id).first()

    def create_user(self, db: Session, user_data: UserCreate, supabase_id: str) -> User:
        db_user = User(
            supabase_id=supabase_id,
            email=user_data.email,
            username=user_data.username,
            full_name=user_data.full_name,
            is_active=True,
            is_verified=False,
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def update_user(self, db: Session, user_id: int, **kwargs) -> Optional[User]:
        db_user = db.query(User).filter(User.id == user_id).first()
        if db_user:
            for key, value in kwargs.items():
                if hasattr(db_user, key):
                    setattr(db_user, key, value)
            db.commit()
            db.refresh(db_user)
        return db_user

    def deactivate_user(self, db: Session, user_id: int) -> bool:
        db_user = db.query(User).filter(User.id == user_id).first()
        if db_user:
            db_user.is_active = False
            db.commit()
            return True
        return False

    def get_user_wallets(self, db: Session, user_id: int) -> List[Wallet]:
        return db.query(Wallet).filter(Wallet.user_id == user_id).all()

    def add_wallet(
        self, db: Session, user_id: int, wallet_data: WalletConnect
    ) -> Wallet:
        existing_wallet = (
            db.query(Wallet).filter(Wallet.address == wallet_data.address).first()
        )

        if existing_wallet:
            raise ValueError("Wallet address already exists")

        user_wallets = self.get_user_wallets(db, user_id)
        is_primary = len(user_wallets) == 0

        db_wallet = Wallet(
            user_id=user_id,
            address=wallet_data.address,
            wallet_type=wallet_data.wallet_type,
            is_primary=is_primary,
        )
        db.add(db_wallet)
        db.commit()
        db.refresh(db_wallet)
        return db_wallet

    def set_primary_wallet(self, db: Session, user_id: int, wallet_id: int) -> bool:
        db.query(Wallet).filter(Wallet.user_id == user_id).update({"is_primary": False})

        wallet = (
            db.query(Wallet)
            .filter(Wallet.id == wallet_id, Wallet.user_id == user_id)
            .first()
        )

        if wallet:
            wallet.is_primary = True
            db.commit()
            return True
        return False

    def remove_wallet(self, db: Session, user_id: int, wallet_id: int) -> bool:
        wallet = (
            db.query(Wallet)
            .filter(Wallet.id == wallet_id, Wallet.user_id == user_id)
            .first()
        )

        if wallet:
            db.delete(wallet)
            db.commit()
            return True
        return False


database_service = DatabaseService()
