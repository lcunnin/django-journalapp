from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserCreationForm
from .models import Entry
from .forms import EntryForm
from django.contrib.auth.decorators import login_required

#https://medium.com/swlh/authenticating-users-in-django-user-registration-880e11e39696

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('entries/home.html')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

#Referred to https://www.youtube.com/watch?v=YkpEtE_x6xk

def index(request):

    context = {'page_heading':'Write It Down'}

    return render(request, 'entries/home.html', context)

@login_required
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

@login_required
def old_entries(request):
    entries = Entry.objects.order_by('-date_posted')

    context = {'entries' : entries,
        'page_heading':'My Journal Entries'}

    return render(request, 'entries/old_entries.html', context)