from integrations.api_client.api_client_base import ApiClientBase
from web.config import web_settings


class ApiClientSSO(ApiClientBase):
    def oauth_url_create(self):
        url = self.url_create(
            path='/oauth2/authorize',
            parameters={
                'client_id': web_settings.API_SSO_CLIENT_ID,
                'redirect_uri': web_settings.API_SSO_REDIRECT_URL,
                'response_type': 'code',
            },
        )
        return url

    def oauth_token_create(self, code):
        response = self.post(
            path='/oauth2/access_token',
            data={
                'client_id': web_settings.API_SSO_CLIENT_ID,
                'client_secret': web_settings.API_SSO_CLIENT_SECRET,
                'grant_type': 'authorization_code',
                'redirect_uri': '',
                'code': code,
            },
        )
        token = response['access_token']
        return token

    def user_get(self, token: str):
        response = self.get(
            path='/users/me',
            token=token,
        )
        return response
