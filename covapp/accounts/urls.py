from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.UserRegistrationView.as_view(), name='register'),
    path('get-token/', views.CustomAuthToken.as_view(), name='api_token_auth'),
]