from django.shortcuts import render
# Create your views here.

def index(request):

    return render(request,'index.html')


def results(request):

    return render(request,'result.html')

def login(request):

    pass

def register(request):
    pass