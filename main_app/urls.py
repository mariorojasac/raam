from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pantries/', views.pantry_index, name='pantries'),
    path('pantries/<int:pk>/', views.pantry_detail, name='detail'),

]
