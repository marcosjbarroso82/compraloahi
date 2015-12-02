from django.db import models


class ErrorReport(models.Model):
    description = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True)
    screenshot = models.ImageField(null=True, upload_to='report')

