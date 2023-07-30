 
from app.api_client.event import ApiClientEVENT
from app.api_client.sso import ApiClientSSO
from app.api_client.user import ApiClientUSER
from app.api_client.xle import ApiClientXLE
from settings import settings


class ApiClient:
    sso = ApiClientSSO(host=settings.API_SSO_HOST)
    xle = ApiClientXLE(host=settings.API_XLE_HOST)
    user = ApiClientUSER(host=settings.API_USER_HOST)
    event = ApiClientEVENT(host=settings.API_EVENT_HOST)
