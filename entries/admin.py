from django.contrib import admin
from .models import Entry

class EntryAdmin(admin.ModelAdmin):

    list_display = ('title', 'text', )

admin.site.register(Entry, EntryAdmin)