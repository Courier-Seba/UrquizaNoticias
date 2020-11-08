from django.urls import path

from .views import AvisosListView, AvisosCreateView

urlpatterns = [
    path('', AvisosListView.as_view(), name='avisos-list'),
    path('nuevo/', AvisosCreateView.as_view(), name='nuevo-aviso')
]
