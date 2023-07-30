import httpx

from web.config import web_settings


class UserApi:
    def __init__(self, host: str = None, token: str = None):
        self.host: str = host if host else web_settings.API_USER_HOST
        self.token: str = token if token else web_settings.API_USER_TOKEN

    def get_link(self, path: str):
        return f"{self.host}{path}"

    def get(self, path: str, **kwargs):
        response = httpx.get(
            url=self.get_link(path),
            params=kwargs
        )
        return response.json()

    def get_all_tags(self):
        path = "/api/v1/tags"
        return self.get(path, app_token=self.token)

    def get_users_by_tags(self, tag_id: str):
        path = "/api/v1/users/tags"
        return self.get(path, app_token=self.token, tags=tag_id)


user_api = UserApi(host="https://user-php.k8-dev.u2035dev.ru", token="NZB8dfw8qzqqcaxvb")
