from django.shortcuts import render
from django.http import HttpResponse
from .models import Faculty, Group, Cafedra
from django.template import RequestContext, loader


def index(request):

    faculty = Faculty.objects.all()
    template = 'faculty/index.html'
    DATA = []

    for i in range(len(faculty)):
        DATA.append({faculty[i].name: []})
        cafedra = Cafedra.objects.filter(faculty_id=faculty[i].id)
        if len(cafedra) != 0:
            for caf in cafedra:
                DATA[i][faculty[i].name].append({caf.name: []})
                group = Group.objects.filter(cafedra_id=caf.id)
                group_list = []
                if len(group) != 0:
                    for j in range(len(group)):
                        group_list.append(group[j].name)
                DATA[i][faculty[i].name][0][caf.name] = group_list

    return render(request, template, {'data': DATA})