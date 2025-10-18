from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import settings
from .models import Base

# Lazy initialization to avoid import errors
_engine = None
_SessionLocal = None

def get_engine():
    global _engine
    if _engine is None:
        _engine = create_engine(settings.database_url)
    return _engine

def get_session_local():
    global _SessionLocal
    if _SessionLocal is None:
        _SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=get_engine())
    return _SessionLocal


def create_tables():
    Base.metadata.create_all(bind=get_engine())


def get_db():
    db = get_session_local()()
    try:
        yield db
    finally:
        db.close()
