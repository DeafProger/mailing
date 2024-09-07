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
        exclude = ('start_time', 'status') #  , 'date_letter_was_sent', 'creator')


'''
class MessageForm(StyleFormMixin, ModelForm):
    """Класс форма для сообщений для рассылки"""
    class Meta:
        model = Message
        exclude = ('creator',)


class CustomerForm(StyleFormMixin, ModelForm):
    """Класс форма для клиентов сервиса"""
    class Meta:
        model = Customer
        exclude = ('creator',)


class MailingManagerForm(StyleFormMixin, ModelForm):
    """Класс форма для редактирования рассылки менеджером"""
    class Meta:
        model = Mailing
        fields = ('active',)
'''