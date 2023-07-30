from django.http import JsonResponse, HttpResponseRedirect
from django.views import View

from integrations.api_client import api_client
from web.config import web_settings

api_users_oauth_callback_link = "users/oauth/callback/"


class ApiUsersOauthCallbackView(View):
    def get(self, request):
        code = request.GET.get("code")
        if not code:
            return JsonResponse({'error': 'Code not found'})
        token = api_client.sso.oauth_token_create(code=code)
        return HttpResponseRedirect(f'https://t.me/{web_settings.TG_BOT_USERNAME}?start={token}')
