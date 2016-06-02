from django.contrib import admin

from . import models


class GroupModelAdmin(admin.ModelAdmin):
    list_display = ["name",]

admin.site.register(models.InterestGroup, GroupModelAdmin)
admin.site.register(models.Membership)
admin.site.register(models.MemberShipRequest)
admin.site.register(models.Post)