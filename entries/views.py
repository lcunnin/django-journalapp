from django.shortcuts import render, redirect
from .models import Entry
from .forms import EntryForm

#Referred to https://www.youtube.com/watch?v=YkpEtE_x6xk

def index(request):

    context = {'page_heading':'Write It Down'}

    return render(request, 'entries/home.html', context)

def new_entry(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('old_entries')
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