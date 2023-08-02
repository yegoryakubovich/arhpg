from django import forms

from admin_web.models.faq import FaqType


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class AddFaqTypeForm(forms.Form):
    type = forms.ChoiceField(label="Тип", choices=((FaqType.text, "Текст"), (FaqType.link, "Ссылка")), required=True)


class AddFaqBaseForm(forms.Form):
    title = forms.CharField(label="Вопрос", required=True)
    text_button = forms.CharField(label="Текст кнопки", required=True)


class AddFaqTextForm(AddFaqBaseForm):
    text_answer = forms.CharField(widget=forms.Textarea, label="Текст ответа", required=False)
    documents = MultipleFileField(label="Документы", required=False)
    photos = MultipleFileField(label="Фотографии", required=False)


class AddFaqLinkForm(AddFaqBaseForm):
    link = forms.CharField(label="Ссылка", required=True)
