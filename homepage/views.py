from django.shortcuts import render

# Create your views here.
from .models import Menu


# def index(request):
#   students_list = Student.objects.all()
#   context = {'students_list': students_list}
#   return render(request, 'homepage/index.html', context=context)

def index(request):
  menu_list = Menu.objects.all()
  context = {'menu_list': menu_list}
  return render(request, 'homepage/index.html', context=context)
  