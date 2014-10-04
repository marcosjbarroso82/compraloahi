from django.contrib import admin
from . import models

class AdImageInline(admin.TabularInline):
    model = models.AdImage
    extra = 4

class AdAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ AdImageInline, ]

admin.site.register(models.Ad, AdAdmin)
