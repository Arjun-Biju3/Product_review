from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ProductReviewListCreateView, UserRegistrationView
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('register', UserRegistrationView, basename='register')

urlpatterns = [
    path('auth/', obtain_auth_token),
    path('', include(router.urls)),
    path('products/<int:product_id>/reviews/', ProductReviewListCreateView.as_view(), name='product-reviews'),
]
