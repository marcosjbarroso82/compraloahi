from django.db import models


class Day(models.Model):
    time_begin = models.TimeField()
    time_end = models.TimeField()

class Agenda(models.Model):
    #monday      = models.OneToOneField(Day, related_name="monday", null=True, on_delete=models.CASCADE)
    """
    tuesday     = models.OneToOneField(Day, related_name="tuesday", null=True)
    wednesday   = models.OneToOneField(Day, related_name="wednesday", null=True)
    thursday    = models.OneToOneField(Day, related_name="thursday", null=True)
    friday      = models.OneToOneField(Day, related_name="friday", null=True)
    saturday    = models.OneToOneField(Day, related_name="saturday", null=True)
    sunday      = models.OneToOneField(Day, related_name="sunday", null=True)
    """
    class Meta:
        verbose_name = "Agenda"
        verbose_name_plural = "Agendas"

    """
    def delete(self, using=None):
        self.monday.delete()
        return super(self.__class__, self).delete(*args, **kwargs)
    def pre_delete_handler(self):
        self.monday.delete()
        pass
    """