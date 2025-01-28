from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'myapp/index.html')

def Budgeting(request):
    return render(request, "myapp/budgeting.html")

def ToolsAndCalculators(request):
    return render(request, "myapp/tools-and-calculators.html")

def TipsAndGuides(request):
    return render(request, "myapp/tips-and-guides.html")

def Resources(request):
    return render(request, "myapp/resources.html")

def ContactUs(request):
    return render(request, "myapp/Contact-Us.html")