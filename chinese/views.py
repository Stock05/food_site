from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Food,Category
# Create your views here.

def index(request):
    if request.method == 'POST':
        # food_name = request.POST['foodname']
        # description = request.POST['description']
        # new_food = Food.objects.create(name=food_name, description = description)
        # new_food.save()
        fs=FileSystemStorage()
        uploaded_file = request.FILES['file']
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        return HttpResponse("{}에 저장이 잘 되었습니다.".format(url))
    else:
        pass    
    return render(request=request, template_name='chinese/index.html')


def exam(request):    
    categories = Category.objects.all()  # Get all categories
    context = {
        'categories': categories,  # Pass categories to context
    }
    return render(request=request, template_name='chinese/exam.html',context=context)

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core.files.storage import FileSystemStorage


# def upload_file(request):    
#     uploaded_file = request.FILES['file']
#     fs = FileSystemStorage()
#     name = fs.save(uploaded_file.name, uploaded_file)
#     url = fs.url(name)
#     return HttpResponse(f"File uploaded at {url}")


def upload(request):
    fs=FileSystemStorage()
    uploaded_file = request.FILES['file']
    name = fs.save(uploaded_file.name, uploaded_file)
    url = fs.url(name)
    return HttpResponse("{}에 저장이 잘 되었습니다.".format(url))