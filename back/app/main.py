from typing import Union
from pydantic_settings import BaseSettings, SettingsConfigDict
from fastapi import FastAPI


class Settings(BaseSettings):
    auth_key: str
    model_config = SettingsConfigDict(env_file=".env")


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
