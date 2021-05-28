from django.forms import ModelForm
from .models import Entry

class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ('title', 'text', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'textarea', 'placeholder': 'Enter a title'})
        self.fields['text'].widget.attrs.update({'class' : 'textarea', 'placeholder' : 'Today I am grateful for...'})
        