from mailing.views import AttemptListView, AttemptDeleteView, ContactsView, HomePageView,\
    MailingListView, MailingCreateView, MailingUpdateView, MailingDetailView, MailingDeleteView,\
    MessageListView, MessageCreateView, MessageUpdateView, MessageDetailView, MessageDeleteView,\
    ClientListView, ClientCreateView, ClientUpdateView, ClientDetailView, ClientDeleteView
from django.views.decorators.cache import cache_page
from mailing.apps import MailingConfig
from django.urls import path


app_name = MailingConfig.name

urlpatterns = [
    # Урлы для рассылок
    path('', HomePageView.as_view(), name='home_page'),
    path('mailing_list/', MailingListView.as_view(), name='mailing_list'),
    path('create_mailing/', MailingCreateView.as_view(), name='create_mailing'),
    path('edit_mailing/<int:pk>/', MailingUpdateView.as_view(), name='edit_mailing'),
    path('info_mailing/<int:pk>/', cache_page(60)(MailingDetailView.as_view()), name='info_mailing'),
    path('delete_mailing/<int:pk>/', MailingDeleteView.as_view(), name='delete_mailing'),

    # Урлы для клиентов сервиса
    path('client/', ClientListView.as_view(), name='client_list'),
    path('create_client/', ClientCreateView.as_view(), name='create_client'),
    path('edit_client/<int:pk>/', ClientUpdateView.as_view(), name='edit_client'),
    path('info_client/<int:pk>/', ClientDetailView.as_view(), name='info_client'),
    path('delete_client/<int:pk>/', ClientDeleteView.as_view(), name='delete_client'),

    # Урлы для сообщений для рассылки
    path('message/', MessageListView.as_view(), name='message_list'),
    path('create_message/', MessageCreateView.as_view(), name='message_create'),
    path('edit_message/<int:pk>/', MessageUpdateView.as_view(), name='edit_message'),
    path('info_message/<int:pk>/', MessageDetailView.as_view(), name='info_message'),
    path('delete_message/<int:pk>/', MessageDeleteView.as_view(), name='delete_message'),

    # Урлы для попыток рассылки
    path('attempt/', AttemptListView.as_view(), name='attempt_list'),
    path('attempt_delete/<int:pk>/', AttemptDeleteView.as_view(), name='delete_attempt'),

    path('contacts/', ContactsView.as_view(), name='contacts'),

] 
