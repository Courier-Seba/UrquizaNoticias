from django.urls import path, include
from .views import register

urlpatterns = [
    path('account/', include('django.contrib.auth.urls')),
    path('registrer/', register, name='signup'),
]
