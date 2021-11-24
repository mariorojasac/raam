from django.shortcuts import render
from django.http import HttpResponse



class Pantry:
    def __init__(self, name, description, location):
        self.name = name
        self.description = description
        self.location = location


pantries = [
    Pantry('Corey', 'free food', 'Austin'),
    Pantry('Vernell', 'donated foods', 'Atlanta'),
    Pantry('Mario', 'free food', 'Indianapolis'),
    Pantry('Cahyl', 'free food', 'Brooklyn')
]





# Create your views here.
def home(request):
    return HttpResponse('Hola')

def about(request):
    return render(request, 'about.html')

def pantry_index(request):
    return render(request, 'pantries/index.html', { 'pantries': pantries})