from django.urls import path, include
from rest_framework_nested import routers
from food.views import CategoryViewSet, FoodViewSet, FoodImageViewSet, ReviewViewSet
from order.views import CartViewSet, CartItemViewSet, OrderViewSet, initiate_payment, payment_success, payment_fail, payment_cancel, HasOrderedFood
from api.views import dashboard_stats

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet, basename='category')
router.register('foods', FoodViewSet, basename='food')
router.register('carts', CartViewSet, basename='cart')
router.register('orders', OrderViewSet, basename='order')

food_router = routers.NestedDefaultRouter(router, 'foods', lookup='food')
food_router.register('images', FoodImageViewSet, basename='food-image')
food_router.register('reviews', ReviewViewSet, basename='food-review')

cart_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
cart_router.register('items', CartItemViewSet, basename='cart-item')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(food_router.urls)),
    path('', include(cart_router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path("payment/initiate/", initiate_payment, name="initiate-payment"),
    path("payment/success/", payment_success, name="payment-success"),
    path("payment/fail/", payment_fail, name="payment-fail"),
    path("payment/cancel/", payment_cancel, name="payment-cancel"),
    path('orders/has-ordered/<int:food_id>/', HasOrderedFood.as_view()),
    path('dashboard/stats/', dashboard_stats, name='dashboard-stats'),
]