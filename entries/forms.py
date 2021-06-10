from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Entry

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']

class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ('title', 'text', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'textarea', 'placeholder': 'Enter a title'})
        self.fields['text'].widget.attrs.update({'class' : 'textarea', 'placeholder' : 'Write here'})

