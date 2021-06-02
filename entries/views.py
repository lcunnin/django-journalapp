from django.shortcuts import render, redirect
from .models import Entry
from .forms import EntryForm

# Create your views here.
def index(request):

    context = {'page_heading':'Gratitude Journal'}

    return render(request, 'entries/home.html', context)

def new_entry(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('')
    else:

        form = EntryForm()

    context = {
        'form' : form,
        'page_heading':'New Journal Entry'}
    
    return render(request, 'entries/new_entry.html', context)

def old_entries(request):
    entries = Entry.objects.order_by('-date_posted')

    context = {'entries' : entries,
        'page_heading':'My Journal Entries'}

    return render(request, 'entries/old_entries.html', context)