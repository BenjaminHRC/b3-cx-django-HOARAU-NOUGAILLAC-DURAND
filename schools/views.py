import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.dateparse import parse_date
from django.db import connection

from schools.forms import SchoolForm
from schools.models import Reservation, School

def home(request):
    schools = School.objects.all()
    return render(request, 'schools/home.html', {'schools': schools})


def details(request, school_id):
    # connection.cursor().execute('DELETE FROM schools_reservation WHERE user_id = 16')
    school = School.objects.get(id=school_id)
    reservations = Reservation.objects.filter(school=school).order_by('date')
    return render(request, 'schools/details.html', {'school': school, 'reservations': reservations, 'user': request.user, 'today': datetime.date.today()})


def index(request):
    schools = School.objects.all()
    return render(request, 'schools/index.html', {'schools': schools})


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
