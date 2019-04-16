from django.shortcuts import render
from django.http import HttpResponse

def home_index(request):

    template = 'home/index.html'

    return render(request, template)
