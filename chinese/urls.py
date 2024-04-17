"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views
app_name = 'chinese'
urlpatterns = [
    path('add_food/', views.add_food, name ='add_food'),   
    path('c/', views.exam),
    path("food_detail/<int:pk>/", views.food_detail, name='food_detail'),
    path("food_delete/<int:pk>/", views.food_delete, name='food_delete'),  

]
