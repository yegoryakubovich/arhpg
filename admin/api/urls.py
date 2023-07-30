from django.urls import path

from api.views.users.oauth.callback import api_users_oauth_callback_link, ApiUsersOauthCallbackView
from api.views.users.oauth.get import api_users_oauth_get_link, ApiUsersOauthGetView
from api.views.users.oauth.redirect import ApiUsersOauthView, api_users_oauth_link
from api.views.users.oauth.user.get import api_users_oauth_user_get_link, ApiUsersOauthUserGetView


urlpatterns = [
    path(api_users_oauth_callback_link, ApiUsersOauthCallbackView.as_view(), name='api_users_oauth_callback'),
    path(api_users_oauth_get_link, ApiUsersOauthGetView.as_view(), name='api_users_oauth_get'),
    path(api_users_oauth_user_get_link, ApiUsersOauthUserGetView.as_view(), name='api_users_oauth_user_get'),
    path(api_users_oauth_link, ApiUsersOauthView.as_view(), name='api_users_oauth'),
]
