from django.contrib import messages
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import FormView

from admin_web.admin import admin_site
from admin_web.forms import AddFaqTypeForm, AddFaqTextForm, AddFaqLinkForm
from admin_web.models import Faq, FaqAttachmentType, FaqAttachment
from admin_web.models.faq import FaqType


class AddFaqTypeView(FormView):
    form_class = AddFaqTypeForm
    template_name = 'admin/custom_form.html'

    def form_valid(self, form: AddFaqTypeForm):
        if form.cleaned_data["type"] == FaqType.text:
            return redirect("add_faq_text")
        elif form.cleaned_data["type"] == FaqType.link:
            return redirect("add_faq_link")
        HttpResponseRedirect("/")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '[FAQ] Выбор типа ответа'
        context['has_permission'] = True
        context['has_file_field'] = True
        context.update(**admin_site.each_context(self.request))
        return context


class AddFaqTextView(FormView):
    form_class = AddFaqTextForm
    template_name = 'admin/custom_form.html'

    def form_valid(self, form: AddFaqTextForm):
        title = form.cleaned_data["title"]
        text_button = form.cleaned_data["text_button"]
        text = form.cleaned_data["text_answer"]
        images = form.cleaned_data["photos"]
        files = form.cleaned_data["documents"]
        if not text and not images and not files:
            messages.info(self.request, f"Добавьте вложение или текст")
            return redirect("add_faq_text")

        faq = Faq.objects.create(type=FaqType.text, question=title, priority=1, answer_button=text_button)
        if text:
            FaqAttachment.objects.create(faq=faq, type=FaqAttachmentType.text, value=text)
        for image in images:
            local = default_storage.save(f'bots/photos/{image.name}', ContentFile(image.read()))
            FaqAttachment.objects.create(faq=faq, type=FaqAttachmentType.image, value=local)
        for file in files:
            local = default_storage.save(f'bots/files/{file.name}', ContentFile(file.read()))
            FaqAttachment.objects.create(faq=faq, type=FaqAttachmentType.file, value=local)
        messages.info(self.request, f"Вопрос #{faq.id} добавлен")
        return redirect("add_faq_type")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '[FAQ] Добавить (Текст)'
        context['has_permission'] = True
        context['has_file_field'] = True
        context.update(**admin_site.each_context(self.request))
        return context


class AddFaqLinkView(FormView):
    form_class = AddFaqLinkForm
    template_name = 'admin/custom_form.html'

    def form_valid(self, form: AddFaqLinkForm):
        title = form.cleaned_data["title"]
        text_button = form.cleaned_data["text_button"]
        url = form.cleaned_data["link"]
        faq = Faq.objects.create(type=FaqType.text, question=title, priority=1, answer_button=text_button)
        FaqAttachment.objects.create(faq=faq, type=FaqAttachmentType.url, value=url)
        return redirect("add_faq_type")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '[FAQ] Добавить (Ссылка)'
        context['has_permission'] = True
        context['has_file_field'] = True
        context.update(**admin_site.each_context(self.request))
        return context
