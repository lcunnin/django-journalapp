from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Entry
from .forms import EntryForm


#https://medium.com/swlh/authenticating-users-in-django-user-registration-880e11e39696
#https://stackoverflow.com/questions/65484009/integrityerror-at-new-entry-3-not-null-constraint-failed-learning-logs-entry

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            raw_password = form.cleaned_data.get('password2')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('new_entry.html')
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
            form.instance.user = request.user
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
    entries = Entry.objects.filter(user=request.user)

    context = {'entries' : entries,
        'page_heading':'My Journal Entries'}

    return render(request, 'entries/old_entries.html', context)