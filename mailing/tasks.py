from config.settings import EMAIL_HOST_USER
from mailing.models import Mailing, Attempt
from django.core.mail import send_mail
from django.utils import timezone
from django.conf import settings
from datetime import timedelta
from time import sleep
import smtplib

DELTA_MONTHLY = timedelta(minutes=30)  # use timedelta(month=1) in release
DELTA_WEEKLY = timedelta(minutes=7)  # use timedelta(week=1) in release
DELTA_DAILY = timedelta(minutes=1)  # use timedelta(day=1) in release


def send_mailing():
    # Получаю все рассылки
    mailings = Mailing.objects.all()

    # Запускаю цикл по рассылкам, где получаю данные и запускаю отправку сообщений
    for maIling in mailings:
        # Создаю словарь, который будет содержать почту получателя и получил ли он письмо
        mailing_list_recipients = []
        # Узнаю надо ли отправить рассылку в данный момент цикла
        if maIling.frequency == 'daily' and maIling.start_time <= timezone.now():
            # Получаю название рассылки
            subject_of_letter = maIling.message.subject_of_letter
            # Получаю текст сообщения
            message = maIling.message.body_of_letter
            # Получаю клиентов которым надо отправить сообщение
            mails = [maIling.address(),]
            # Отправляю рассылку пользователям
            for mail in mails:
                try:
                    send_mail(
                        subject=subject_of_letter,
                        message=message,
                        from_email=EMAIL_HOST_USER,
                        recipient_list=[mail]
                    )

                    # Создаю получателя и добавляю его в список получивших письмо
                    recipient = f'{mail} - успешно получил рассылку'
                    mailing_list_recipients.append(recipient)

                except smtplib.SMTPException as e:
                    # Создаю получателя и добавляю его в список не получивших письмо
                    recipient = f'{mail} - не получил рассылку в связи с {e}'
                    mailing_list_recipients.append(recipient)

                next_time = maIling.start_time
                while next_time < timezone.now():
                    next_time += DELTA_DAILY
                maIling.start_time = next_time
                maIling.save()

                # Создаю новый экземпляр модели попытки рассылки и пишу что он успешный
                Attempt.objects.create(attempt_last_time=timezone.now(),
                                       attempt_next_time=next_time,
                                       mailing=maIling,
                                       attempt_status=mailing_list_recipients)

        if maIling.frequency == 'weekly' and maIling.start_time <= timezone.now():
            # Получаю название рассылки
            subject_of_letter = maIling.message.subject_of_letter
            # Получаю текст сообщения
            message = maIling.message.body_of_letter
            # Получаю клиентов которым надо отправить сообщение
            mails = [maIling.address(), ]
            # Отправляю рассылку пользователям
            for mail in mails:
                try:
                    send_mail(
                        subject=subject_of_letter,
                        message=message,
                        from_email=EMAIL_HOST_USER,
                        recipient_list=[mail]
                    )

                    # Создаю получателя и добавляю его в список получивших письмо
                    recipient = f'{mail} - успешно получил рассылку'
                    mailing_list_recipients.append(recipient)

                except smtplib.SMTPException as e:
                    # Создаю получателя и добавляю его в список не получивших письмо
                    recipient = f'{mail} - не получил рассылку в связи с {e}'
                    mailing_list_recipients.append(recipient)

                # Создаю новый экземпляр модели попытки рассылки и пишу что он успешный
                next_time = maIling.start_time
                while next_time < timezone.now():
                    next_time += DELTA_WEEKLY
                maIling.start_time = next_time
                maIling.save()

                # Создаю новый экземпляр модели попытки рассылки и пишу что он успешный
                Attempt.objects.create(attempt_last_time=timezone.now(),
                                       attempt_next_time=next_time,
                                       mailing=maIling,
                                       attempt_status=mailing_list_recipients)

        if maIling.frequency == 'monthly' and maIling.start_time <= timezone.now():
            # Получаю название рассылки
            subject_of_letter = maIling.message.subject_of_letter
            # Получаю текст сообщения
            message = maIling.message.body_of_letter
            # Получаю клиентов которым надо отправить сообщение
            mails = [maIling.address(), ]
            # Отправляю рассылку пользователям
            for mail in mails:
                try:
                    send_mail(
                        subject=subject_of_letter,
                        message=message,
                        from_email=EMAIL_HOST_USER,
                        recipient_list=[mail]
                    )

                    # Создаю получателя и добавляю его в список получивших письмо
                    recipient = f'{mail} - успешно получил рассылку'
                    mailing_list_recipients.append(recipient)

                except smtplib.SMTPException as e:
                    # Создаю получателя и добавляю его в список не получивших письмо
                    recipient = f'{mail} - не получил рассылку в связи с {e}'
                    mailing_list_recipients.append(recipient)

                next_time = maIling.start_time
                while next_time < timezone.now():
                    next_time += DELTA_MONTHLY
                maIling.start_time = next_time
                maIling.save()

                # Создаю новый экземпляр модели попытки рассылки и пишу что он успешный
                Attempt.objects.create(attempt_last_time=timezone.now(),
                                       attempt_next_time=next_time,
                                       mailing=maIling,
                                       attempt_status=mailing_list_recipients)



def shedule():
    while (True):
        send_mailing()
        sleep(10)