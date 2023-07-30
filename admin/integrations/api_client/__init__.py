from integrations.api_client.sso import ApiClientSSO
from web.config import web_settings

API_SSO_HOST = web_settings.SSO_HOST


class ApiClient:
    sso = ApiClientSSO(host=API_SSO_HOST)


api_client = ApiClient()
