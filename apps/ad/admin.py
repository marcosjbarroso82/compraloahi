from django.contrib import admin
from . import models

class AdImageInline(admin.TabularInline):
    model = models.AdImage
    extra = 4

def tags_temp6(instance):
    return ', '.join(instance.categories)

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', tags_temp6]

class AdAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ AdImageInline, ]
    list_display = ['title', tags_temp6]

admin.site.register(models.Ad, AdAdmin)
