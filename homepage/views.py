from django.shortcuts import render

# Create your views here.
from .models import Student


def index(request):
  students_list = Student.objects.all()
  context = {'students_list': students_list}
  return render(request, 'homepage/index.html', context=context)