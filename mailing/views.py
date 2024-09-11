from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from mailing.forms import MailingForm, ClientForm, MailingManagerForm, MessageForm
from mailing.models import Message, Client, Mailing, Attempt


# Create your views here.
class ClientUpdateView(LoginRequiredMixin, UpdateView):
    """Класс контролер для редактирования клиентов сервиса"""
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:customer_list')
    template_name = 'client_form.html'


class ClientDetailView(DetailView):
    """Класс-контроллер для вывода информации о клиентах сервиса"""
    template_name = 'client_detail.html'
    model = Client


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    """Класс-контроллер для удаления клиента сервиса"""
    model = Client
    success_url = reverse_lazy('mailing:customer_list')
    template_name = 'client_delete.html'


class ClientListView(ListView):
    """Класс-контроллер для вывода всех клиентов сервиса"""
    template_name = 'client_list.html'
    model = Client


class ClientCreateView(LoginRequiredMixin, CreateView):
    """Класс контроллер для создания клиентов сервиса"""
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')
    template_name = 'client_form.html'

    def form_valid(self, form):
        """Метод для добавления к клиенту сервиса его создателя"""
        client = form.save()
        user = self.request.user
        client.creator = user
        client.save()
        return super().form_valid(form)


class MailingListView(ListView):
    """Класс-контроллер для вывода всех рассылок"""
    template_name = 'mailing_list.html'
    model = Mailing


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    """Класс контролер для редактирования рассылок"""
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')
    template_name = 'mailing_form.html'

    def get_form_class(self):
        """В зависимости от роли пользователя будет выводиться определенная форма"""
        user = self.request.user
        if user.has_perm('mailing.can_disable_mailing'):
            return MailingManagerForm
        return MailingForm


class MailingDetailView(DetailView):
    """Класс-контроллер для вывода информации о рассылке"""
    template_name = 'mailing_detail.html'
    model = Mailing


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    """Класс-контроллер для удаления рассылки"""
    model = Mailing
    success_url = reverse_lazy('mailing:mailing_list')
    template_name = 'mailing_delete.html'


class MailingCreateView(LoginRequiredMixin, CreateView):
    """Класс контроллер для создания рассылок"""
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')
    template_name = 'mailing_form.html'

    def form_valid(self, form):
        """Метод для добавления к рассылке её создателя"""
        mailing = form.save()
        user = self.request.user
        mailing.owner = user
        mailing.save()
        return super().form_valid(form)


class MessageListView(ListView):
    """Класс-контроллер для вывода всех сообщений"""
    model = Message
    template_name = 'message_list.html'


class MessageCreateView(LoginRequiredMixin, CreateView):
    """Класс контроллер для создания сообщений для рассылки"""
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')
    template_name = 'message_form.html'

    def form_valid(self, form):
        """Метод для добавления к сообщениям рассылок их создателей"""
        message = form.save()
        user = self.request.user
        message.creator = user
        message.save()
        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    """Класс контролер для редактирования сообщения для рассылки"""
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')
    template_name = 'message_form.html'


class MessageDetailView(DetailView):
    """Класс-контроллер для вывода информации о сообщении для рассылки"""
    template_name = 'message_detail.html'
    model = Message


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    """Класс-контроллер для удаления сообщения для рассылки"""
    model = Message
    success_url = reverse_lazy('mailing:message_list')
    template_name = 'message_delete.html'


class AttemptListView(ListView):
    """Класс-контроллер для вывода всех попыток рассылки"""
    template_name = 'attempt_list.html'
    model = Attempt


class AttemptDeleteView(DeleteView):
    """Класс-контроллер для вывода информации по попытке рассылки"""
    success_url = reverse_lazy('mailing:attempt_list')
    template_name = 'attempt_delete.html'
    model = Attempt
