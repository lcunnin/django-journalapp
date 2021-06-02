from django.db import models

class Entry(models.Model):
    title = models.CharField(max_length=100, default='')
    date_posted = models.DateTimeField(auto_now_add = True)
    text = models.TextField()

    def __str__(self):
        return 'Entry #{}'.format(self.id)

    class Meta:
        verbose_name_plural = 'entries'