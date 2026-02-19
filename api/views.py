from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from food.models import Food, Review
from users.models import User
from order.models import Order
from django.db.models import Avg

@api_view(['GET'])
@permission_classes([IsAdminUser])
def dashboard_stats(request):
    total_foods = Food.objects.count()
    total_orders = Order.objects.count()
    total_users = User.objects.count()
    
    average_rating = Review.objects.aggregate(avg=Avg('ratings'))['avg'] or 0
    average_rating = round(average_rating, 1)

    return Response({
        "foods": total_foods,
        "orders": total_orders,
        "users": total_users,
        "average_rating": average_rating
    })