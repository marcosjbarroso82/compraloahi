from django.contrib import admin

from apps.notification import models

class NotificationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'receiver', 'receiver')


admin.site.register(models.Notification, NotificationsAdmin)