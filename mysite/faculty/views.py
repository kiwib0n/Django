from django.shortcuts import render
from django.http import HttpResponse
from .models import Faculty, Group, Cafedra
from django.template import RequestContext, loader


def index(request):

    response = """
        <!DOCTYPE hml>
            <html>
                <head>
                    <title>Факультеты</title>
                    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
                     <style>
                        body{
                            margin:0 auto;
                                margin-bottom:15%;
                                margin-left:15%;
                                margin-right:15%;
                            
                            background-color: #222;
                            color: whitesmoke;
                        }
                        button{
                            margin:0 auto;
                                margin-top:5px;
                                margin-left:5px;
                                margin-right:5px;
                                margin-bottom:5px;
                            border: 2px solid whitesmoke;
                        }
                    </style>
                </head>
            <body>
                <br>
    """
    faculty = Faculty.objects.all()

    for i in range(len(faculty)):
        response += "<center><button class='btn btn-dark'>"+str(faculty[i].name)+"["+str(faculty[i].simple_name)+"]</button></center>"
        cafedra =  Cafedra.objects.filter(faculty_id=faculty[i].id)
        if len(cafedra) != 0:
            response += "<br/><ol name='cafedra_"+str(faculty[i].simple_name)+"'>"
            for caf in cafedra:
                response += "<li key="+str(caf.id)+"><button class='btn btn-success'>"+str(caf.name)+ " [ "+ str(caf.simple_name)+" ];</button></li>"

                group = Group.objects.filter(cafedra_id=caf.id)
                if len(group) != 0:
                    response += "<ul>"
                    for j in range(len(group)):
                        response += "<li key="+str(group[j].id)+"><button class='btn btn-primary'>"+str(group[j].name)+"</button></li>"
                    response += "</ul>"


            response += "</ol><br/>"
        else:
            response += "<br/><center><ol name='cafedra_"+str(faculty[i].simple_name)+"'><button class='btn btn-warning'>Пока пусто ...</button></ol></center>"
        response += "<br/>"
        response += """
            </body>
        </html>
        """
    return HttpResponse(response)