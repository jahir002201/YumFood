from django_filters.rest_framework import FilterSet
from food.models import Food

class FoodFilter(FilterSet):
    class Meta:
        model = Food
        fields = {
            'category_id': ['exact'],
            'price': ['gt', 'lt'],
            'is_special': ['exact']
        }