from django.contrib import admin

from . import models


class GroupModelAdmin(admin.ModelAdmin):
    list_display = ["name",]

admin.site.register(models.InterestGroup, GroupModelAdmin)
admin.site.register(models.Suscription)
admin.site.register(models.Post)