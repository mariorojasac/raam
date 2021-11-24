from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pantries/', views.pantry_index, name='pantries'),

    # //// detail path ////
    # path('pantries/<int:pantry_id>/', views.raam_detail, name='detail'),
    path('pantries/<int:pk>/', views.pantry_detail, name='detail'),

    # //// route to show form for creating a Pantry ////
    # path('pantries/create/', views.PantryCreate.as_view(), name='pantires_create'),


    # //// EDIT ////
    # path('pantries/<int:pantry_id>/update/', views.PantryUpdate.as_view(), name='pantries_update'),
    # path('pantries/<int:pk>/update/', views.PantryUpdate.as_view(), name='pantries_update'),

    # //// DELETE PATH ////
    # path('pantries/<int:pantry_id>/delete/', views.PantryDelete.as_view(), name='pantries_delete'),
    # path('pantries/<int:pk>/delete/', views.PantryDelete.as_view(), name='pantries_delete'),

    # //// DROP OFF////
    # path('foods/<int:pantry_id>/add_dropoff/', views.add_dropoff, name='add_dropoff'),
    # path('foods/<int:pk>/add_dropoff/', views.add_dropoff, name='add_dropoff'),

    # //// FOODS LIST ////
    # path('foods/', views.FoodList.as_view(), name='foods_index'),

    # //// FOOD DETAIL ////
    # path('foods/<int:food_id>/', views.FoodDetail.as_view(), name='foods_detail'),
    # path('foods/<int:pk>/', views.FoodDetail.as_view(), name='foods_detail'),

    # //// CREATE FOOD ///
    # path('foods/create/', views.FoodCreate.as_view(), name='foods_create'),


    # //// UPDATE FOOD ///
    # path('foods/<int:pk>/update/', views.FoodUpdate.as_view(), name='foods_update'),

    # //// DELETE FOOD ///
    # path('foods/<int:pk>/delete/', views.FoodDelete.as_view(), name='foods_delete'),


    # //// FOOD ASSOCIATION ////
    # path('foods/<int:food_id>/assoc_food/<int:food_id>/', views.assoc_food, name='assoc_food'),

    # //// SIGN UP ////
    # path('accounts/signup/', views.signup, name='signup'),














]
