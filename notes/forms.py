from django import forms
from django.core.exceptions import ValidationError

from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'text']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-3'}),
            'text': forms.Textarea(attrs={'class': 'form-control mb-3'}),
        }
        labels = {
            'text': 'Write your note here:'
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        # if 'Django' not in title:
        #     raise ValidationError('title is not valid')
        return title