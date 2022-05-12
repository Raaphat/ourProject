from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    # this jwt view is to generate a token basen on a user, that token expires after a short time
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('', views.getRoutes),
    path('doctors/', views.getDoctors),
    path('doctor/<str:pk>/', views.getDoctor),
    path('patients/', views.getPatients),
    path('patient/<str:pk>/', views.getPatient),
    path('messages/', views.getMessages),
    
] 