import datetime
from django.shortcuts import redirect, render
from django.contrib import messages
from schools.models import Reservation, School
from django.utils.dateparse import parse_date

def new_booking(request, school_id):
    school = School.objects.get(id=school_id)
    if request.method == 'POST':
        date = request.POST['date']

        if date == "":
            messages.success(request, "Veuillez choisir une date pour votre réservation.")
            return render(request, 'reservations/new.html', {'school': school})
        
        if parse_date(date) <= datetime.date.today():
            messages.success(request, "Veuillez choisir une date à partir de demain.")
            return render(request, 'reservations/new.html', {'school': school})
        
        if len(Reservation.objects.filter(school=school, date=date)) > 0:
            messages.success(request, "Une réservation a déjà été prise en ce jour, choississez un autre jour.")
            return render(request, 'reservations/new.html', {'school': school})
        else:
            booking = Reservation(user=request.user, school=school, date=date)
            booking.save()
            messages.success(request, "Réservation éffectuée.")

        if booking is not None:
            return redirect('../../schools')

        else:
            messages.success(request, "Il y a eu une erreur dans vos identifiants de connexion, réessayez.")
            return render(request, 'reservations/new.html', {'school': school})

    return render(request, 'reservations/new.html', {'school': school})
