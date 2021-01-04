from django import forms

from . import util

class CreateEntryForm(forms.Form):
    title = forms.CharField(label="Title", widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Title'
        }
    ))
    content = forms.CharField(label='Content', widget=forms.Textarea(
        attrs={
            'class':'form-control',
            'placeholder': 'Create Content'
        }
    ))

    def clean_title(self):
        data = self.cleaned_data['title']
        if util.get_entry(data):
            raise forms.ValidationError("An Entry Already exists with this name")

        return data


class EditEntryForm(forms.Form):

    
    content = forms.CharField(widget=forms.Textarea(
        attrs={
            'class':'form-control',
            'placeholder': 'Update Content'
        }
    ))

