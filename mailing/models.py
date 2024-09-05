from django.db import models
# Create your models here.


class Client(models.Model):
    email = models.EmailField(max_length=50, verbose_name='email', unique=True)
    name = models.CharField(max_length=50, verbose_name='ФИО')
    comment = models.TextField(max_length=150, blank=True, null=True, verbose_name='комментарии')
    #  owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Владелец')

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = "клиент"
        verbose_name_plural = "клиенты"


class Message(models.Model):
    """Модель сообщений для рассылки"""
    subject_of_letter = models.CharField(max_length=100, verbose_name="Тема письма")
    body_of_letter = models.TextField(verbose_name='Тело письма')
    # creator = models.ForeignKey(User, verbose_name='Создатель сообщения', on_delete=models.SET_NULL,
    #                            related_name="creator_message", null=True, blank=True)

    def __str__(self):
        return f'{self.subject_of_letter}'

    class Meta:
        verbose_name = "Сообщение для рассылки"
        verbose_name_plural = "Сообщения для рассылки"


class Attempt(models.Model):
    """Модель попытки рассылки"""
    datetime_of_last_attempt = models.DateTimeField(verbose_name='Дата и время последней попытки рассылки')
    attempt_status = models.TextField(verbose_name='статус попытки (успешно/не успешно)')
    # answer = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='Ответ сервера рассылки, если есть')

    def __str__(self):
        return f'{self.attempt_status}'

    class Meta:
        verbose_name = "Попытка рассылки"
        verbose_name_plural = "Попытки рассылки"


class Mailing(models.Model):
    frequency_tuple = (('daily', 'раз в день'), ('weekly', 'раз в неделю'), ('monthly', 'раз в месяц'),)
    status_tuple = (('completed', 'завершена'), ('created', 'создана'), ('started', 'запущена'),)

    start_time = models.DateTimeField(verbose_name='время начала рассылки')
    frequency = models.CharField(max_length=50, verbose_name='периодичность', choices=frequency_tuple)
    status = models.CharField(max_length=50, verbose_name='статус отправки', choices=status_tuple)
    # message = models.ManyToManyField(Message, blank=True, null=True, verbose_name='сообщение')
    message = models.ForeignKey(Message, on_delete=models.SET_NULL, verbose_name="Сообщение рассылки",
                                related_name="mailing_list_message", null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='клиент')
    # owner = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True, 
    #                                help_text='Укажите владельца')

    def __str__(self):
        return f'{self.start_time}'

    class Meta:
        verbose_name = 'настройки'
        verbose_name_plural = 'настройки'
        # permissions = [('set_status_to_completed', 'Can disable mailing')]
