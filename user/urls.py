from django.urls import path

from .views import UserCreationView

urlpatterns = [
    path('registrarse/', UserCreationView.as_view(), name='register'),
]
