from django.urls import path, include
from .views import register, change_password

urlpatterns = [
    path('account/', include('django.contrib.auth.urls')),
    path('account/registrarse/', register, name='signup'),
    path('account/cambiar-contrasenia', change_password, name='change_password')
]
