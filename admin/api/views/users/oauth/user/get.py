from django.http import JsonResponse
from django.views import View

from integrations.api_client import api_client
from integrations.api_client.utils import Response, ResponseState

api_users_oauth_user_get_link = "users/oauth/user/get/"


class ApiUsersOauthUserGetView(View):
    def get(self, request):
        token = request.GET.get("token")
        if not token:
            return JsonResponse(Response(state=ResponseState.error,  error="Token not found"))
        user = api_client.sso.user_get(token=token)
        return JsonResponse(Response(user=user))
