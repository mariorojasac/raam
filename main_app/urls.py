from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pantries/', views.pantry_index, name='pantries'),
    path('pantries/<int:pk>/', views.pantry_detail, name='detail'),
    path('pantries/create/', views.PantryCreate.as_view(), name='pantries_create'),
    path('pantries/<int:pk>/update/', views.PantryUpdate.as_view(), name='pantries_update'),
    path('pantries/<int:pk>/delete/', views.PantryDelete.as_view(), name='pantries_delete'),
    path('pantries/<int:pk>/add_schedule/', views.add_schedule, name='add_schedule'),
    path('foods/', views.FoodList.as_view(), name='foods_index'),
    path('foods/<int:pk>/', views.FoodDetail.as_view(), name='foods_detail'),
    path('foods/create/', views.FoodCreate.as_view(), name='foods_create'),
    path('foods/<int:pk>/update/', views.FoodUpdate.as_view(), name='foods_update'),
    path('foods/<int:pk>/delete/', views.FoodDelete.as_view(), name='foods_delete'),
    path('pantries/<int:pantry_id>/assoc_food/<int:food_id>/', views.assoc_food, name='assoc_food'),
    path('accounts/signup/', views.signup, name='signup'),
]
