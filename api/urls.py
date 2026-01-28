from django.urls import path, include
from rest_framework_nested import routers
from food.views import CategoryViewSet, FoodViewSet, FoodImageViewSet, ReviewViewSet
from order.views import CartViewSet, CartItemViewSet, OrderViewSet

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
]