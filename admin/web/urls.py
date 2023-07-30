from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + [
    path('admin/', include('admin_web.urls')),
    path('', include('api.urls')),
    path('', RedirectView.as_view(url="admin")),
]
