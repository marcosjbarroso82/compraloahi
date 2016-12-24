from django.contrib import admin

from apps.msg import models

class MsgsAdmin(admin.ModelAdmin):
    list_display = ('subject', 'body', 'sender', 'recipient', 'thread', 'parent', 'object_id', 'is_new', 'sender_deleted',
                    'recipient_deleted', 'recipient_deleted_at')

admin.site.register(models.Msg, MsgsAdmin)