from django.forms import ModelForm, BooleanField
from mailing.models import Message, Client, Mailing


class StyleFormMixin:
    """Класс для стилизации форм"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = "form-check-input"
            else:
                field.widget.attrs['class'] = "form-control"


class MailingForm(StyleFormMixin, ModelForm):
    """Класс форма для рассылок"""
    class Meta:
        model = Mailing
        exclude = ('owner',)  # , 'date_letter_was_sent', 'creator')


class MailingManagerForm(StyleFormMixin, ModelForm):
    """Класс форма для редактирования рассылки менеджером"""
    class Meta:
        model = Mailing
        fields = '__all__'


class ClientForm(StyleFormMixin, ModelForm):
    """Класс форма для клиентов сервиса"""
    class Meta:
        model = Client
        exclude = ('owner',)


class MessageForm(StyleFormMixin, ModelForm):
    """Класс форма для сообщений для рассылки"""
    class Meta:
        model = Message
        exclude = ('creator',)
