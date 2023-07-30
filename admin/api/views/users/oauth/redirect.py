from django.http import JsonResponse, HttpResponseRedirect
from django.views import View

from admin_web.models import Oauth
from integrations.api_client import api_client
from integrations.api_client.utils import Response


api_users_oauth_link = "users/oauth/"


class ApiUsersOauthView(View):
    def get(self, request):
        hash = request.GET.get("hash")
        if not hash:
            return JsonResponse({'error': 'Hash required'})

        oauth = Oauth.objects.filter(hash=hash).first()
        if not oauth:
            return JsonResponse({'error': 'Hash not found'})

        response = HttpResponseRedirect(api_client.sso.oauth_url_create())
        response.set_cookie(key='hash', value=hash)

        return response
