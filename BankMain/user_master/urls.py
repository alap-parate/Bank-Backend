from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProtectedView, CustomPasswordResetConfirmView, UserStatusView, UserActivationView

router = DefaultRouter()
# router.register(r'users', CustomUserViewSet, basename='user')
# router.register(r'users',UserViewSet)

urlpatterns = [
    path('test/', ProtectedView.as_view(), name='Test'),
    path('activate/<uid>/<token>', UserActivationView.as_view({'get': 'activation'}), name='activation'),
    path('', include(router.urls)),
    path('users/<int:pk>/status/', UserStatusView.as_view({'patch': 'update_status'})),
    path('password/reset/confirm/<uidb64>/<token>',CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm')
]