from django.contrib import admin
from . import models
from adLocation.models import AdLocation


class AdLocationInline(admin.TabularInline):
    model = AdLocation


class AdImageInline(admin.TabularInline):
    model = models.AdImage
    extra = 4


class AdAdmin(admin.ModelAdmin):
    inlines = [AdImageInline, AdLocationInline]
    readonly_fields = ['author', ]

    def has_change_permission(self, request, obj=None):
        has_class_permission = super(
            AdAdmin, self).has_change_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superuser and request.user.id != obj.author.id:
            return False
        return True

    def get_queryset(self, request):
        if request.user.is_superuser:
            return models.Ad.objects.all()
        return models.Ad.objects.filter(author=request.user)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()

admin.site.register(models.Ad, AdAdmin)
admin.site.register(models.AdImage, admin.ModelAdmin)
admin.site.register(models.CategoryTag)
