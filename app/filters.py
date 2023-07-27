import django_filters
from .models import Person
from django import forms
from django.contrib.auth.models import User


def departments(request):
    if request is None:
        return Person.objects.none()

    user = request.user.company
    print(user)
    return user.department_set.all()

class ManagerFilter(django_filters.FilterSet):
    code = forms.CharField(initial=departments)

    class Meta:
      model = Person
      fields = ['code','month', 'year']
    
        
