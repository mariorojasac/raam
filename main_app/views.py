from django.shortcuts import redirect, render

from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pantry
from .forms import ScheduleForm


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def pantry_index(request):
    pantries = Pantry.objects.all()
    return render(request, 'pantries/index.html', { 'pantries': pantries})

def pantry_detail(request, pk):
    pantry = Pantry.objects.get(id=pk)
    schedule_form = ScheduleForm()
    return render(request, 'pantries/detail.html', {'pantry': pantry, 'schedule_form': schedule_form})

def add_schedule(request, pk):
    form = ScheduleForm(request.POST)
    print(form._errors)
    if form.is_valid():
        new_schedule = form.save(commit=False)
        new_schedule.pantry_id = pk
        new_schedule.save()
    return redirect('detail', pk=pk)


class PantryCreate(CreateView):
    model = Pantry
    fields = ('name', 'location', 'description')


class PantryUpdate(UpdateView):
    model = Pantry
    fields = ('name', 'location', 'description')


class PantryDelete(DeleteView):
    model = Pantry
    success_url = '/pantries/'



