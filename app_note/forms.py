from django import forms
from .models import Note

# class NoteForm(forms.Form):
#     title = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control'}))
#     description = forms.CharField(
#         widget=forms.Textarea(attrs={'class': 'form-control'}))


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'name': 'title',
                    'type': 'text',
                    'id': 'titleInput',
                    'placeholder': "Title"
                }
            ),
            'description':  forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'name': 'description',
                    'type': 'text',
                    'id': 'noteInput',
                    'placeholder': "Note",
                    'style': 'height: 300px'
                }
            )
        }
