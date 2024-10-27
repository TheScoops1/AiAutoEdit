from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request, 'AutoEdit/homePage.html')

def login_page(request):
    return render(request, 'AutoEdit/loginPage.html')

def editing_page(request):
    return render(request, 'AutoEdit/editingPage.html')
