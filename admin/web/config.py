from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    ADMIN_WEB_IP: str
    ADMIN_USER: str
    ADMIN_PASSWORD: str

    API_SSO_HOST: str
    API_SSO_CLIENT_ID: str
    API_SSO_CLIENT_SECRET: str
    API_SSO_REDIRECT_URL: str

    API_USER_HOST: str
    API_USER_TOKEN: str

    TG_BOT_USERNAME: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


web_settings = Settings()
