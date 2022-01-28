from dataclasses import field
import django_filters
from .models import Fooditem

class fooditemFilter(django_filters.FilterSet):
    class Meta:
        model = Fooditem
        fields = ['name']
        