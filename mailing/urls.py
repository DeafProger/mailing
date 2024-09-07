from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from mailing.apps import MailingConfig
from mailing.views import MailingListView
    #MessageListView, MessageCreateView, MessageUpdateView, MessageDetailView, MessageDeleteView, \
    #CustomerListView, CustomerCreateView, CustomerUpdateView, CustomerDetailView, CustomerDeleteView, MailingListView, \
    #MailingCreateView, MailingUpdateView, MailingDetailView, MailingDeleteView, AttemptListView, \
    #AttemptDetailView

app_name = MailingConfig.name

urlpatterns = [
    # Урлы для рассылок
    path('', MailingListView.as_view(), name='mailing_list'),
    #path('create_mailing/', MailingCreateView.as_view(), name='create_mailing'),
    #path('edit_mailing/<int:pk>/', MailingUpdateView.as_view(), name='edit_mailing'),
    #path('info_mailing/<int:pk>/', MailingDetailView.as_view(), name='info_mailing'),
    #path('delete_mailing/<int:pk>/', MailingDeleteView.as_view(), name='delete_mailing'),
] 
