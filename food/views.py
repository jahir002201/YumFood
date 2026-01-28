from api.permissions import IsAdminOrReadOnly
from food.permissions import IsReviewAuthorOrReadonly
from food.serializers import CategorySerializer, FoodSerializer, FoodImageSerializer, ReviewSerializer
from food.filters import FoodFilter
from food.paginations import DefaultPagination
from food.models import Category, Food, FoodImage, Review
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

class CategoryViewSet(ModelViewSet):
    """
    Category CRUD operations for Food categories.
    - Admin can create, update, delete categories.
    - Everyone can list and view categories.
    """
    permission_classes = [IsAdminOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class FoodViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = DefaultPagination
    serializer_class = FoodSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = FoodFilter
    search_fields = ['name','description','category__name']
    ordering_fields = ['price','updated_at']
    def get_queryset(self):
        return Food.objects.prefetch_related('images').all()
    @action(detail=False)
    def specials(self, request):
        specials = Food.objects.filter(is_special=True)
        serializer = self.get_serializer(specials, many=True)
        return Response(serializer.data)
    
class FoodImageViewSet(ModelViewSet):
    serializer_class = FoodImageSerializer
    permission_classes = [IsAdminOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(food_id=self.kwargs.get('food_pk'))
    def get_queryset(self):
        return FoodImage.objects.filter(food_id=self.kwargs.get('food_pk'))
    
class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadonly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
    
    def get_queryset(self):
        return Review.objects.filter(food=self.kwargs.get('food_pk'))
    
    def get_serializer_context(self):
        return {'food_id': self.kwargs.get('food_pk')}