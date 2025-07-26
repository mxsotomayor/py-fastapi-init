 
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_CONN_STRING: str 
    API_KEY: str
    GOOGLE_RECAPTCHA_SECRET: str
    PORT: int

    class Config:
        env_file = ".env"


settings = Settings()