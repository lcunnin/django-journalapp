from django.db import models
import datetime

class Entry(models.Model):
    date_posted = models.DateField(default=datetime.date.today)
    text = models.TextField()

    def __str__(self):
        return 'Entry #{}'.format(self.id)

    class Meta:
        verbose_name_plural = 'entries'