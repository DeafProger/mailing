from django.db import models
from users.models import User
# Create your models here.


class Client(models.Model):
    email = models.EmailField(max_length=50, verbose_name='email', unique=True)
    name = models.CharField(max_length=50, verbose_name='ФИО')
    comment = models.TextField(max_length=150, blank=True, null=True, verbose_name='комментарии')
    owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Владелец')

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = "клиент"
        verbose_name_plural = "клиенты"


class Message(models.Model):
    """Модель сообщений для рассылки"""
    subject_of_letter = models.CharField(max_length=100, verbose_name="Тема письма")
    body_of_letter = models.TextField(verbose_name='Тело письма')
    creator = models.ForeignKey(User, verbose_name='Создатель сообщения', on_delete=models.SET_NULL,
                                related_name="creator_message", null=True, blank=True)

    def __str__(self):
        return f'{self.subject_of_letter}'

    class Meta:
        verbose_name = "Сообщение для рассылки"
        verbose_name_plural = "Сообщения для рассылки"


class Mailing(models.Model):
    frequency_tuple = (('daily', 'раз в день'), ('weekly', 'раз в неделю'), ('monthly', 'раз в месяц'),)
    status_tuple = (('completed', 'завершена'), ('created', 'создана'), ('started', 'запущена'),)

    start_time = models.DateTimeField(verbose_name='время начала рассылки')
    frequency = models.CharField(max_length=50, verbose_name='периодичность', choices=frequency_tuple, default='daily')
    status = models.CharField(max_length=50, verbose_name='статус отправки', choices=status_tuple, default='created')
    message = models.ForeignKey(Message, on_delete=models.SET_NULL, verbose_name="Сообщение рассылки",
                                related_name="mailing_list_message", null=True, blank=True)
    client = models.ManyToManyField(Client, related_name='mailing', verbose_name='клиенты')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, help_text='Укажите владельца')

    def __str__(self):
        return f'{self.start_time}'

    def address(self):
        result = str(self.client.all())
        templ = '<QuerySet [<Client: '
        if result[0:len(templ)] == templ:
            return result[len(templ):-3]
        else:
            return result

    class Meta:
        verbose_name = 'настройки'
        verbose_name_plural = 'настройки'
        # permissions = [('set_status_to_completed', 'Can disable mailing')]
        permissions = [
            ('can_view_userslist_mailing', 'can view userslist mailing'),
            ('can_disable_user_mailing', 'can disable user mailing'),
            ('can_view_any_mailing', 'can view any mailing lists'),
            ('can_disable_mailing', 'can disable mailing'),

            ('can_not_update_mailing_and_message', 'cannot edit mailing and message'),
            ('can_not_manage_mailing', 'cannot manage mailing'),
            ('can_not_edit_mailing', 'cannot edit mailing'),

        ]


class Attempt(models.Model):
    """Модель попытки рассылки"""
    attempt_last_time = models.DateTimeField(verbose_name='Дата и время последней попытки рассылки')
    attempt_next_time = models.DateTimeField(verbose_name='Дата и время следующей попытки рассылки')
    attempt_status = models.TextField(verbose_name='статус попытки (успешно/не успешно)')
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE,
                                verbose_name='Связь рассылки и информации о её статусе')

    def __str__(self):
        return f'{self.attempt_last_time}'

    class Meta:
        verbose_name = "Попытка рассылки"
        verbose_name_plural = "Попытки рассылки"
