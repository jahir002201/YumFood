from rest_framework import serializers
from food.models import Category, Food, FoodImage, Review
from django.contrib.auth import get_user_model


class CategorySerializer(serializers.ModelSerializer):
    food_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ["id", "name", "description", "food_count"]

class FoodImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = FoodImage
        fields = ['id', 'image']

class FoodSerializer(serializers.ModelSerializer):
    images = FoodImageSerializer(many=True, read_only=True)
    price_with_discount = serializers.SerializerMethodField()

    class Meta:
        model = Food
        fields = ['id','name','description','price','price_with_discount','stock','category','images','is_special','discount_percent']

    def get_price_with_discount(self, obj):
        if obj.discount_percent > 0:
            return round(obj.price * (100 - obj.discount_percent)/100, 2)
        return obj.price

class SimpleUserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(
        method_name='get_current_user_name')

    class Meta:
        model = get_user_model()
        fields = ['id', 'name']

    def get_current_user_name(self, obj):
        return obj.get_full_name()

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(method_name='get_user')
    class Meta:
        model = Review
        fields = ['id', 'user', 'food', 'ratings', 'comment']
        read_only_fields = ['user', 'food']
    
    def get_user(self, obj):
        return SimpleUserSerializer(obj.user).data

    def create(self, validated_data):
        food_id = self.context["food_id"]
        return Review.objects.create(food_id=food_id, **validated_data)