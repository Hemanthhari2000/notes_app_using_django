from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from .models import Note
from .forms import NoteForm, CreateUserForm
from .decorators import *

import random


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registered Successfully!")
            return redirect('login')
    context = {
        'form': form,
    }
    return render(request, 'app_note/register.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'Username or Password is incorrect')
    context = {}
    return render(request, 'app_note/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    # notes = request.user.customer.note_set.all()
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


@login_required(login_url='login')
def add_note(request):
    form = NoteForm()
    context = {
        'form': form
    }

    return render(request, 'app_note/add_note.html', context)


@login_required(login_url='login')
def note_detail(request, pk):
    note = Note.objects.get(id=pk)
    context = {
        'note': note
    }

    return render(request, 'app_note/note_detail.html', context)


@login_required(login_url='login')
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


@login_required(login_url='login')
def note_delete(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return redirect('home')
