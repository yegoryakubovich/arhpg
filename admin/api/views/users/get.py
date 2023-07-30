from django.http import JsonResponse
from django.views import View

from admin_web.models import User

api_users_link = "users/get"


class ApiUsersView(View):
    def get(self, request):
        users = [{
            'id': user.id, 'tg_user_id': user.tg_user_id,
            "lastname": user.lastname, "firstname": user.firstname, "email": user.email
        } for user in User.objects.filter().all()]
        return JsonResponse({'result': 'success', 'items': users})
