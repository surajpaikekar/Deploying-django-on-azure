from django.shortcuts import render, HttpResponse

# Create your views here.

def SampleView(request):
    return HttpResponse("This is sample Home page")