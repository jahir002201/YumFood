from django.contrib import admin
from food.models import Category, Food, FoodImage, Review

admin.site.register(Category)
admin.site.register(Food)
admin.site.register(FoodImage)
admin.site.register(Review)