from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('budgeting/', views.Budgeting, name="budgeting"),
    path('tools-and-calculators/', views.ToolsAndCalculators, name="toolsandcalculators"),
    path('tips-and-guides/', views.TipsAndGuides, name="tipsandguides"),
    path('resources/', views.Resources, name="resources"),
    path('contact-us/', views.ContactUs, name="contactUs"),
]