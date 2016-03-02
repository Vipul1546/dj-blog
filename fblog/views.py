from django.shortcuts import render
from models import Employee
from django.http import HttpResponse

# Create your views here.

def index(request):
    employee = Employee.objects.create(
        email="vipul.kong@company.com",
        first_name="tiwari",
        last_name="vipul"
    )
    employee.save()
    return HttpResponse("<h1>Saved!</h1>")