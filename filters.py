import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name= "date_low_range", lookup_expr='gte')
    end_date = DateFilter(field_name="date_high_range", lookup_expr='lte')
    NRO = CharFilter(field_name='NRO', lookup_expr='icontains')
    keyword = CharFilter(field_name='keyword', lookup_expr='icontains')
    information = CharFilter(field_name='information', lookup_expr='icontains')

    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['date_created']

