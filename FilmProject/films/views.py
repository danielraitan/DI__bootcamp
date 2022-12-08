from django.shortcuts import render, redirect
from .forms import AddFilmForm, AddDirectorForm

def homepage(request):

    form = AddFilmForm()
    if request.method == 'POST':
        form = AddFilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    
    context = {'form': form}

    return render(request, 'homepage.html', context)

def addDirector(request):

    form = AddDirectorForm()
    if request.method == 'POST':
        form = AddDirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    
    context = {'form': form}

    return render(request, 'director/addDirector.html', context)

def addFilm(request):

    form = AddFilmForm()
    if request.method == 'POST':
        form = AddFilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    
    context = {'form': form}

    return render(request, 'addFilm.html', context)