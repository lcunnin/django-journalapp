from django.db import models
import datetime

class Entry(models.Model):
    text = models.TextField()
    date_posted = models.DateField(default=datetime.date.today)
