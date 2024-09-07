from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, logout_then_login, auth_logout
from users.views import UserCreateView, email_verification, logout, UserListView, ManagerUserUpdateView
from users.apps import UsersConfig
from django.urls import path

app_name = UsersConfig.name

urlpatterns = [
    # Урлы для входа пользователя в систему, выхода из системы и регистрации
    path('login/', LoginView.as_view(template_name="login.html"), name='login'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('logout/', logout, name='logout'),

    # Урл для подтверждения почты
    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),

    # Урлы для просмотра и редактирования пользователя модератором
    # path('user/', UserListView.as_view(), name='user_list'),
    # path('edit_user/<int:pk>/', ManagerUserUpdateView.as_view(), name='edit_user'),
]  # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
