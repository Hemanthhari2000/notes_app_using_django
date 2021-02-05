from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.forms import ModelForm
from django import forms
from .models import Note


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = '__all__'

        widgets = {
            'note_title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'name': 'title',
                    'type': 'text',
                    'id': 'titleInput',
                    'placeholder': "Title"
                }
            ),
            'note_body':  forms.Textarea(
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


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
