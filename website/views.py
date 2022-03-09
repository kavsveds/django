from django.http import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request,'index.html')

def heaven(request):
    return render(request,'heaven.html')

def mumm(request):
    return render(request,'mumm.html')

def singapore(request):
    return render(request,'singapore.html')

def every(request):
    return render(request,'every.html')

def last(request):
    return render(request,'last.html')
