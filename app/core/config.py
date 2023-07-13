from pydantic import BaseSettings
from functools import lru_cache
from pathlib import Path


class Settings(BaseSettings):
    # DB Settings
    sample_storage_db_service_name: str
    sample_storage_db_mongo_data_dir: Path
    sample_storage_db_mongo_root_username: str
    sample_storage_db_mongo_root_password: str

    class Config:
        env_file = "/repo/sample_storage_service2/.env"
        secrets_dir = "/run/secrets"
        validate_all = True


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
