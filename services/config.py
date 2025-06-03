from dotenv import load_dotenv
import os
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    VALIDATOR_HOST: str = os.getenv("VALIDATOR_HOST", "127.0.0.1")
    VALIDATOR_PORT: int = int(os.getenv("VALIDATOR_PORT", "8000"))
    DETECT_IP: str = os.getenv("DETECT_IP", "8.8.8.8")
    SI_API_URL: str = os.getenv("SI_API_URL")
    SI_API_JWT_SECRET_KEY: str = os.getenv("SI_API_JWT_SECRET_KEY")
    SI_API_JWT_EXPIRE_IN: int = int(os.getenv("SI_API_JWT_EXPIRE_IN", "30"))
    SI_API_JWT_ALGORITHM: str = os.getenv("SI_API_JWT_ALGORITHM", "HS256")

    class Config:
        case_sensitive = True
        env_file = ".env"
        extra = "allow"

settings = Settings() 