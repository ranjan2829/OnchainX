from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    supabase_url:str
    supabase_anon_key=str
    supabase_service_role_key=str

    #neon
    database_url=str
    jwt_secret_key:str
    jwt_algorithm:str="HS256"
    jwt_access_token_expire_minutes:int=30

    app_name="OnchainX"
    debug:bool=True
    cors_origins:List[str]=["http://localhost:3000","https://onchain-x.vercel.app"]

    class Config:
        env_file=".env"
settings=Settings()

