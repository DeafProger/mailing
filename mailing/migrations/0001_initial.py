# Generated by Django 5.1.1 on 2024-09-11 12:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50, unique=True, verbose_name='email')),
                ('name', models.CharField(max_length=50, verbose_name='ФИО')),
                ('comment', models.TextField(blank=True, max_length=150, null=True, verbose_name='комментарии')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
            ],
            options={
                'verbose_name': 'клиент',
                'verbose_name_plural': 'клиенты',
            },
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(verbose_name='время начала рассылки')),
                ('frequency', models.CharField(choices=[('daily', 'раз в день'), ('weekly', 'раз в неделю'), ('monthly', 'раз в месяц')], default='daily', max_length=50, verbose_name='периодичность')),
                ('status', models.CharField(choices=[('completed', 'завершена'), ('created', 'создана'), ('started', 'запущена')], default='created', max_length=50, verbose_name='статус отправки')),
                ('client', models.ManyToManyField(related_name='mailing', to='mailing.client', verbose_name='клиенты')),
                ('owner', models.ForeignKey(blank=True, help_text='Укажите владельца', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'настройки',
                'verbose_name_plural': 'настройки',
                'permissions': [('can_disable_mailing', 'can disable mailing'), ('can_view_any_mailing', 'can view any mailing lists')],
            },
        ),
        migrations.CreateModel(
            name='Attempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attempt_last_time', models.DateTimeField(verbose_name='Дата и время последней попытки рассылки')),
                ('attempt_next_time', models.DateTimeField(verbose_name='Дата и время следующей попытки рассылки')),
                ('attempt_status', models.TextField(verbose_name='статус попытки (успешно/не успешно)')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.mailing', verbose_name='Связь рассылки и информации о её статусе')),
            ],
            options={
                'verbose_name': 'Попытка рассылки',
                'verbose_name_plural': 'Попытки рассылки',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_of_letter', models.CharField(max_length=100, verbose_name='Тема письма')),
                ('body_of_letter', models.TextField(verbose_name='Тело письма')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creator_message', to=settings.AUTH_USER_MODEL, verbose_name='Создатель сообщения')),
            ],
            options={
                'verbose_name': 'Сообщение для рассылки',
                'verbose_name_plural': 'Сообщения для рассылки',
            },
        ),
        migrations.AddField(
            model_name='mailing',
            name='message',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mailing_list_message', to='mailing.message', verbose_name='Сообщение рассылки'),
        ),
    ]
