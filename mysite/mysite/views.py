from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader

def index(request):

    return HttpResponse('');