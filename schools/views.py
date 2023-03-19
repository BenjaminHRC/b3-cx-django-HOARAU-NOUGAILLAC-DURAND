from django.http import HttpResponseRedirect
from django.shortcuts import render

from schools.forms import SchoolForm
from schools.models import School


def index(request):
    schools = School.objects.all()
    context = {'schools': schools}
    return render(request, 'schools/index.html', context)


def add(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SchoolForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/schools')

    # if a GET (or any other method) we'll create a blank form
    form = SchoolForm()
    return render(request, 'schools/add.html', {'form': form})


def edit(request, school_id):
    school = School.objects.get(id=school_id)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SchoolForm(request.POST, instance=school)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/schools')

    # if a GET (or any other method) we'll create form with data
    form = SchoolForm(instance=school)
    return render(request, 'schools/edit.html', {'form': form, 'school': school})


def delete(request, school_id):
    school = School.objects.get(id=school_id)
    school.delete()
    return HttpResponseRedirect('/schools')
