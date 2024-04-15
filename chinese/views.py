from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Food
# Create your views here.

def index(request):
    if request.method == 'POST':
        food_name = request.POST['foodname']
        description = request.POST['description']
        new_food = Food.objects.create(name=food_name, description = description)
        new_food.save()
    else:
        pass    
    return render(request=request, template_name='chinese/index.html')


def add_food(request):
    if request.method == 'POST':
        food_name = request.POST['foodname']
        # 입력 데이터 검증 및 처리
        # ...
        new_food = Food.objects.create(name=food_name)
        # 성공 처리
        return redirect('food_list')
    else:
        return render(request, 'add_food.html')
    
from django.core.exceptions import ValidationError

