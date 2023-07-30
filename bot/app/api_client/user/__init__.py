import requests

from app.api_client.api_client_base import ApiClientBase
from settings import settings


class ApiClientUSER(ApiClientBase):
    @staticmethod
    async def add_tag_user(arhpg_id: int):
        response = requests.post(
            url=f'{settings.API_USER_HOST}/api/v1/users/{arhpg_id}/tags',
            params={'app_token': settings.API_USER_TOKEN},
            json={"tag_id": [settings.API_USER_TAG_ID]},
        )
        return response
