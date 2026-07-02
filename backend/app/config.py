from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # Async SQLAlchemy URL. Defaults to local SQLite so the app runs with no
    # external services; override with Postgres in production, e.g.
    # postgresql+asyncpg://user:pass@host/arbi
    DATABASE_URL: str = "sqlite+aiosqlite:///./arbi.db"

    # Create tables on startup (dev convenience). Use Alembic in production.
    AUTO_CREATE_TABLES: bool = True


@lru_cache
def get_settings() -> Settings:
    return Settings()
