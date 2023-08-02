import requests

from app.api_client.api_client_base import ApiClientBase
from settings import settings


class ApiClientUSER(ApiClientBase):

    async def get_all_tags(self):
        response = await self.get(
            path = "/api/v1/tags",
            parameters={
                'app_token': settings.API_USER_TOKEN,
            },
        )
        return response


    async def get_users_by_tags(self, tag_id: str):
        response = await self.get(
            path =f'/api/v1/users/tags',
            parameters={
                'app_token': settings.API_USER_TOKEN,
                'tags': tag_id
            },
        )
        return response


    @staticmethod
    async def add_tag_user(arhpg_id: int):
        response = requests.post(
            url=f'https://{settings.API_USER_HOST}/api/v1/users/{arhpg_id}/tags',
            params={'app_token': settings.API_USER_TOKEN},
            json={"tag_id": [settings.API_USER_TAG_ID]},
        )
        return response
