from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pantry



def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def pantry_index(request):
    pantries = Pantry.objects.all()
    return render(request, 'pantries/index.html', { 'pantries': pantries})

def pantry_detail(request, pk):
    pantry = Pantry.objects.get(id=pk)
    return render(request, 'pantries/detail.html', {'pantry': pantry})

class PantryCreate(CreateView):
    model = Pantry
    fields = ('name', 'location', 'description')


class PantryUpdate(UpdateView):
    model = Pantry
    fields = ('name', 'location', 'description')


class PantryDelete(DeleteView):
    model = Pantry
    success_url = '/pantries/'