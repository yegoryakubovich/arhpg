from pydantic import BaseSettings


class Settings(BaseSettings):
    MYSQL_HOST: str
    MYSQL_PORT: int
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_NAME: str

    WEB_IP: str
    ADMIN_USER: str
    ADMIN_PASSWORD: str

    SSO_HOST: str
    SSO_CLIENT_ID: str
    SSO_CLIENT_SECRET: str
    SSO_REDIRECT_URL: str

    USER_API_HOST: str
    USER_API_TOKEN: str

    TELEGRAM_BOT_USERNAME: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


web_settings = Settings()
