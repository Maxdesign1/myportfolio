from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def club(request):
    return render(request, 'club.html')

def flier(request):
    return render(request, 'flier.html')

def company(request):
    return render(request, 'company.html')

def logo(request):
    return render(request, 'logo.html')