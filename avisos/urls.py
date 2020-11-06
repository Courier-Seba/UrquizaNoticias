from django.urls import path

from .views import AvisosListView

urlpatterns = [
    path('', AvisosListView.as_view(), name='avisos-list'),
]
