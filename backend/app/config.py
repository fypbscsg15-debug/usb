import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

_backend_dir = Path(__file__).resolve().parent.parent
_root_dir = _backend_dir.parent

# Load .env file into environment variables (backend/.env or root .env)
for env_path in [_backend_dir / ".env", _root_dir / ".env", Path(".env")]:
    if env_path.exists():
        load_dotenv(env_path, override=False)


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./spss.db"
    SECRET_KEY: str = "spss-super-secret-jwt-key-change-in-production-32chars"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 480  # 8-hour pharmacy shift
    NVIDIA_API_KEY: str = ""

    model_config = {
        "env_file": [str(_backend_dir / ".env"), str(_root_dir / ".env"), ".env"],
        "extra": "ignore",
    }


settings = Settings()

