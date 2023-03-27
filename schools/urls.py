from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.index, name='index'),
    path('details/<int:school_id>', views.details, name="details"),
    path('add', views.add, name='add'),
    path('edit/<int:school_id>', views.edit, name='edit'),
    path('delete/<int:school_id>', views.delete, name='delete')
]
