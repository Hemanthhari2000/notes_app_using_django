from django.shortcuts import render, redirect

from .models import Note
from .forms import NoteForm

import random


def home(request):
    notes = Note.objects.all()
    form = NoteForm()
    if request.method == 'POST':
        form = NoteForm(request.POST)

        if form.is_valid():
            form.save()
        # The reason to redirect is because we have stored the form data in the db so now to retrive the info only we again run the "home" function that is the home route so it will fetch the data and even the new data will be there this time. this is the reason we use the redirect again here.
        return redirect('home')

    context = {
        'notes': notes,
        'form': form
    }
    return render(request, 'app_note/home.html', context)


def add_note(request):
    form = NoteForm()
    context = {
        'form': form
    }

    return render(request, 'app_note/add_note.html', context)


def note_detail(request, pk):
    note = Note.objects.get(id=pk)
    context = {
        'note': note
    }

    return render(request, 'app_note/note_detail.html', context)


def note_edit(request, pk):
    note = Note.objects.get(id=pk)
    form = NoteForm(instance=note)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
        return redirect('home')

    context = {
        'form': form
    }

    return render(request, 'app_note/note_edit.html', context)


def note_delete(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return redirect('home')
