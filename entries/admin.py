from django.contrib import admin
from .models import Entry

class EntryAdmin(admin.ModelAdmin):

    list_display = ('text', 'date_posted')

admin.site.register(Entry, EntryAdmin)