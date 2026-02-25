from django.db.models import Count, Avg
from django.utils.timezone import now, timedelta
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from food.models import Food, Review
from order.models import Order, OrderItem
from users.models import User

@api_view(['GET'])
@permission_classes([IsAdminUser])
def dashboard_stats(request):
    total_foods = Food.objects.count()
    total_orders = Order.objects.count()
    total_users = User.objects.count()
    average_rating = Review.objects.aggregate(avg=Avg('ratings'))['avg'] or 0
    average_rating = round(average_rating, 1)

    # Weekly Orders (last 7 days)
    last_week = now() - timedelta(days=7)
    weekly_orders = Order.objects.filter(created_at__gte=last_week).count()

    # Trending Foods (most ordered)
    trending_foods = (
        OrderItem.objects
        .values('food__id', 'food__name')
        .annotate(order_count=Count('id'))
        .order_by('-order_count')[:5]
    )

    # Most liked Foods (highest average rating)
    most_liked_foods = (
        Review.objects
        .values('food__id', 'food__name')
        .annotate(avg_rating=Avg('ratings'))
        .order_by('-avg_rating')[:5]
    )

    return Response({
        "foods": total_foods,
        "orders": total_orders,
        "users": total_users,
        "average_rating": average_rating,
        "weekly_orders": weekly_orders,
        "trending_foods": list(trending_foods),
        "most_liked_foods": list(most_liked_foods)
    })