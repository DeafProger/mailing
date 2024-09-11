from mailing.models import Client, Mailing, Attempt
from django.contrib import admin


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'comment',)
    list_filter = ('name', 'email',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('get_clients', 'frequency', 'status',)  # 'owner')
    list_filter = ('client', 'status',)

    def get_clients(self, obj):
        return ', '.join([p.email for p in obj.client.all()])


@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    list_display = ('attempt_status',)
    list_filter = ('attempt_status',)
