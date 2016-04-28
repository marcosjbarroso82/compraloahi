from django.contrib import admin

from . import models


class GroupModelAdmin(admin.ModelAdmin):
    list_display = ["name",]

admin.site.register(models.InterestGroup, GroupModelAdmin)