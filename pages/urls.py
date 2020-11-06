
from django.urls import path

from .views import HomePageView, UsPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('nos/', UsPageView.as_view(), name='us'),
]
