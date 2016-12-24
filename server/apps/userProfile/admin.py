from django.contrib import admin
from .models import UserLocation, UserProfile, Store

admin.site.register(UserLocation)
admin.site.register(UserProfile)
admin.site.register(Store)
# Register your models here.
