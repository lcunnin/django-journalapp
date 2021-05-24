from django.shortcuts import render
from .models import Entry
# Create your views here.
def index(request):
    entries = Entry.ojects.all()

    context = {'entires' : entries}
    return render(request, 'entries/home.html', context)

def add(request):
    return render(request, 'entries/add.html')