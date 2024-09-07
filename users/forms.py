from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from mailing.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    """Класс форма для регистрации пользователей"""
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class ManagerChangeUserForm(StyleFormMixin, ModelForm):
    """Форма для менеджера, который может заблокировать пользователя"""
    class Meta:
        model = User
        fields = ('is_active',)
