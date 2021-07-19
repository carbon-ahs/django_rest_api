from django.shortcuts import render, redirect

def home(request):

    contex = {
        'key': 'value',
    }
    return render(request, 'home.html', contex)