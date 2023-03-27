from django.urls import path

from . import views

urlpatterns = [
    path('new/<int:school_id>', views.new_booking, name='new_booking'),
]