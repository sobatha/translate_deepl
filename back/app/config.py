from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    items_per_user: int = 50
    model_config = SettingsConfigDict(env_file=".env")
