from django.contrib import admin

from .models import Ad, AdImage, Category
from apps.adLocation.models import AdLocation


class AdLocationInline(admin.TabularInline):
    model = AdLocation


class AdImageInline(admin.TabularInline):
    model = AdImage
    extra = 4


class AdAdmin(admin.ModelAdmin):
    inlines = [AdImageInline]
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
            return Ad.objects.all()
        return Ad.objects.filter(author=request.user)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "color",]
    list_editable = ["color",]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Ad, AdAdmin)
admin.site.register(AdImage, admin.ModelAdmin)
