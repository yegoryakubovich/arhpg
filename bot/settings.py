from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    TG_BOT_USERNAME: str
    TG_BOT_TOKEN: str

    ADMIN_WEB_IP: str
    ADMIN_USER: str
    ADMIN_PASSWORD: str

    API_SSO_HOST: str
    API_SSO_CLIENT_ID: str
    API_SSO_CLIENT_SECRET: str
    API_SSO_REDIRECT_URL: str
    API_XLE_HOST: str
    API_XLE_TOKEN: str
    API_XLE_CONTEXT: str
    API_USER_HOST: str
    API_USER_TOKEN: str
    API_USER_TAG_ID: str
    API_EVENT_HOST: str
    API_EVENT_TOKEN: str

    URL_PROGRAM_GENERAL: str
    URL_PROGRAM_PERSONAL: str
    URL_PROGRAM: str

    HASH_HOST: str

    USEDESK_HOST: str
    USEDESK_ID: str
    USEDESK_TOKEN: str

    KAFKA_HOSTS: str
    KAFKA_SP: str
    KAFKA_SASL_MECHANISM: str
    KAFKA_SASL_USER: str
    KAFKA_SASL_PASSWORD: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()
