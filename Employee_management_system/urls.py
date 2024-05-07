from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *


# Define your viewsets
router = DefaultRouter()
router.register(r'salary_slips', SalarySlipViewSet)
router.register(r'notifications', NotificationViewSet)

# Add your custom URL patterns
urlpatterns = [
    # URL patterns generated by router
    *router.urls,
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('register/', user_register, name='user_register'),
    path('users/', CustomUserListCreateAPIView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', CustomUserRetrieveUpdateDestroyAPIView.as_view(),
         name='user-detail'),
]
