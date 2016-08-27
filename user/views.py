from django.shortcuts import render


def register(request):
    a = 10
    return render(request, 'index.html')
# Create your views here.
