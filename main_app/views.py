from django.shortcuts import redirect, render
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from .models import Pantry, Food
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

    foods_pantry_doesnt_have = Food.objects.exclude(
        id__in=pantry.foods.all().values_list('id'))
    
    
    return render(
        request, 
        'pantries/detail.html', {
            'pantry': pantry, 
            'schedule_form': schedule_form,
            'foods': foods_pantry_doesnt_have
        })

def add_schedule(request, pk):
    form = ScheduleForm(request.POST)
    print(form._errors)
    if form.is_valid():
        new_schedule = form.save(commit=False)
        new_schedule.pantry_id = pk
        new_schedule.save()
    return redirect('detail', pk=pk)

def assoc_food(request, pantry_id, food_id):
    Pantry.objects.get(id=pantry_id).foods.add(food_id)
    return redirect('detail', pk=pantry_id)

def unassoc_food(request, pantry_id, food_id):
    Pantry.objects.get(id=pantry_id).foods.remove(food_id)
    return redirect('detail', pk=pantry_id)


class PantryCreate(CreateView):
    model = Pantry
    fields = ('name', 'location', 'description')


class PantryUpdate(UpdateView):
    model = Pantry
    fields = ('name', 'location', 'description')


class PantryDelete(DeleteView):
    model = Pantry
    success_url = '/pantries/'



class FoodList(ListView):
    model = Food
    template_name = 'main_app/food_list.html'

class FoodDetail(DetailView):
    model = Food
    template_name = 'main_app/food_detail.html'
    

class FoodCreate(CreateView):
    model = Food
    fields = '__all__'

class FoodUpdate(UpdateView):
    model = Food
    fields = ['name', 'description', 'quantity']

class FoodDelete(DeleteView):
    model = Food
    success_url = '/foods/'