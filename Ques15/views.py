from django.shortcuts import render

def home(request):
    return render(request, 'login.html') 

def result(request):
    username=request.GET.get('username')
    return render(request, 'output.html', {'username':username})