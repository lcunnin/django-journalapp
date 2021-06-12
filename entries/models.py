from django.db import models
from django.contrib.auth.models import User

class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="new_entry", null=True)
    title = models.CharField(max_length=100, default='')
    date_posted = models.DateTimeField(auto_now_add = True)
    text = models.TextField(blank = False)

    def __str__(self):
        return 'Entry #{}'.format(self.id)

    class Meta:
        verbose_name_plural = 'entries'

