 
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_CONN_STRING: str 
    API_KEY: str

    class Config:
        env_file = ".env"


settings = Settings()