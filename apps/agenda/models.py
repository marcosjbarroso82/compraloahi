from django.db import models

class Day(models.Model):
    time_begin = models.TimeField(default="00:00:00")
    time_end = models.TimeField(default="23:59:59")

class Agenda(models.Model):
    monday      = models.ForeignKey(Day, null=True, related_name="monday",      on_delete=models.SET_NULL, blank=True)
    tuesday     = models.ForeignKey(Day, null=True, related_name="tuesday",     on_delete=models.SET_NULL, blank=True)
    wednesday   = models.ForeignKey(Day, null=True, related_name="wednesday",   on_delete=models.SET_NULL, blank=True)
    thursday    = models.ForeignKey(Day, null=True, related_name="thursday",    on_delete=models.SET_NULL, blank=True)
    friday      = models.ForeignKey(Day, null=True, related_name="friday",      on_delete=models.SET_NULL, blank=True)
    saturday    = models.ForeignKey(Day, null=True, related_name="saturday",    on_delete=models.SET_NULL, blank=True)
    sunday      = models.ForeignKey(Day, null=True, related_name="sunday",      on_delete=models.SET_NULL, blank=True)

    class Meta:
        verbose_name = "Agenda"
        verbose_name_plural = "Agendas"

    def delete(self, *args, **kwargs):
        if self.monday is not None: self.monday.delete()
        if self.tuesday is not None: self.tuesday.delete()
        if self.wednesday is not None: self.wednesday.delete()
        if self.thursday is not None: self.thursday.delete()
        if self.friday is not None: self.friday.delete()
        if self.saturday is not None: self.saturday.delete()
        if self.sunday is not None: self.sunday.delete()
        return super(self.__class__, self).delete(*args, **kwargs)