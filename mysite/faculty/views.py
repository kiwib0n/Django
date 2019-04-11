from django.shortcuts import render
from django.http import HttpResponse
from .models import Faculty, Group, Cafedra

def index(request):

    response = "<br/>"
    faculty = Faculty.objects.all()

    for i in range(len(faculty)):
        response += "<center>"+str(faculty[i].name)+"["+str(faculty[i].simple_name)+"]</center>"
        cafedra =  Cafedra.objects.filter(faculty_id=faculty[i].id)
        if len(cafedra) != 0:
            response += "<br/><ol>"
            for caf in cafedra:
                response += "<li key="+str(caf.id)+">"+str(caf.name)+ " [ "+ str(caf.simple_name)+" ];</li>"
            response += "</ol><br/>"

        response += "<br/>"

    return HttpResponse(response)