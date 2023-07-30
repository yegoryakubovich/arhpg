from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse, HttpResponseRedirect
from django.views import View

from admin_web.models import Oauth
from integrations.api_client import api_client
from web.config import web_settings


api_users_oauth_callback_link = "users/oauth/callback/"


class ApiUsersOauthCallbackView(View):
    def get(self, request: WSGIRequest):

        code = request.GET.get("code")
        hash = request.COOKIES.get('hash')

        if not code:
            return JsonResponse({'error': 'Code required'})
        if not hash:
            return JsonResponse({'error': 'Hash required'})

        oauth = Oauth.objects.filter(hash=hash).first()
        if not oauth:
            return JsonResponse({'error': 'Hash not found'})

        token = api_client.sso.oauth_token_create(code=code)

        oauth.token = token
        oauth.save()

        return HttpResponseRedirect(f'https://t.me/{web_settings.TG_BOT_USERNAME}')
