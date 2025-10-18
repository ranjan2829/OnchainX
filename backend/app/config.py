from pydantic_settings import BaseSettings
from typing import List, Optional
import os


class Settings(BaseSettings):
    supabase_url: Optional[str] = None
    supabase_anon_key: Optional[str] = None
    supabase_service_role_key: Optional[str] = None

    # neon
    database_url: Optional[str] = None
    jwt_secret_key: Optional[str] = None
    jwt_algorithm: str = "HS256"
    jwt_access_token_expire_minutes: int = 30

    app_name: str = "OnchainX"
    debug: bool = True
    cors_origins: List[str] = ["http://localhost:3000", "https://onchain-x.vercel.app"]

    class Config:
        env_file = ".env"

    def validate_required_vars(self):
        """Validate that all required environment variables are set"""
        required_vars = [
            "supabase_url",
            "supabase_anon_key", 
            "supabase_service_role_key",
            "database_url",
            "jwt_secret_key"
        ]
        
        missing_vars = []
        for var in required_vars:
            if not getattr(self, var):
                missing_vars.append(var)
        
        if missing_vars:
            raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")
        
        return True


settings = Settings()

# Validate environment variables on import
try:
    settings.validate_required_vars()
except ValueError as e:
    print(f"Configuration Error: {e}")
    print("Please set the following environment variables:")
    print("- SUPABASE_URL")
    print("- SUPABASE_ANON_KEY") 
    print("- SUPABASE_SERVICE_ROLE_KEY")
    print("- DATABASE_URL")
    print("- JWT_SECRET_KEY")
    raise
