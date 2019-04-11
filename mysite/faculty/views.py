from django.shortcuts import render
from django.http import HttpResponse
from .models import Faculty, Group, Cafedra

def index(request):

    response = "<br/>"
    faculty = Faculty.objects.all()

    for i in range(len(faculty)):
        response += "<center>"+str(faculty[i].name)+"["+str(faculty[i].simple_name)+"]</center>"
       # cafedra =  Cafedra.objects.get(faculty_id=faculty[i].id)
        #response += str(len(cafedra))
        response += "<br/>"

    return HttpResponse(response)