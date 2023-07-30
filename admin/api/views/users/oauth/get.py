from django.http import JsonResponse
from django.views import View

from integrations.api_client import api_client
from integrations.api_client.utils import Response

api_users_oauth_get_link = "users/oauth/get/"


class ApiUsersOauthGetView(View):
    def get(self, request):
        url = api_client.sso.oauth_url_create()
        return JsonResponse(Response(url=url))
