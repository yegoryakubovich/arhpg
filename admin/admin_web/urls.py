from django.urls import path

from admin_web.admin import admin_site
from admin_web.views import AddFaqTextView, AddFaqLinkView, AddFaqTypeView

urlpatterns = [
    path('add_faq_type', AddFaqTypeView.as_view(), name="add_faq_type"),
    path('add_faq_link', AddFaqLinkView.as_view(), name="add_faq_link"),
    path('add_faq_text', AddFaqTextView.as_view(), name="add_faq_text"),
    path('', admin_site.urls),
]
