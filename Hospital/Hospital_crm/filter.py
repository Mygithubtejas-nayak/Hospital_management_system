import django_filters
from .models import *

class InventoryFilterForm(django_filters.FilterSet):
    class Meta:
        model = Inventory_item
        fields = '__all__'
    