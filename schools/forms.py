from django.forms import ModelForm

from schools.models import School


class SchoolForm(ModelForm):
    class Meta:
        model = School
        fields = ('id', 'name', 'address', 'description')
