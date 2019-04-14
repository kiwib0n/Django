from django.shortcuts import render
from django.http import HttpResponse
from .models import Faculty, Group, Cafedra
from django.template import RequestContext, loader
from django.shortcuts import redirect

def FOR_TEST():

    return 25

def faculty_index(request):

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

def faculty_add(request):

    if request.POST['name'] and request.POST['simple_name']:
        new_faculty = Faculty()
        new_faculty.name = request.POST['name']
        new_faculty.simple_name = request.POST['simple_name']
        new_faculty.save()
        return redirect('faculty_index')
    else:
        return redirect('faculty_index')

def faculty_NewCafedra(request):
    if request.POST['facultet'] and request.POST['cafedra_name'] and request.POST['simple_name']:
        facultet = Faculty.objects.all()
        cafedra = Cafedra()

        print("\n\n")
        print(request.POST['facultet'])
        print("\n\n")

        for i in range(len(facultet)):

            if facultet[i].name.lower() == request.POST['facultet'].lower():
                facultet = facultet[i]
                break

        cafedra.faculty = facultet
        cafedra.name = request.POST['cafedra_name']
        cafedra.simple_name = request.POST['simple_name']

        cafedra.save()
        return redirect('faculty_index')
    else:
        return redirect('faculty_index')
