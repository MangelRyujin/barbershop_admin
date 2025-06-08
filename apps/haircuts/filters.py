import django_filters
from apps.haircuts.models import HairCut

class HairCutFilter(django_filters.FilterSet):
    name=  django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = HairCut
        fields = ['name']