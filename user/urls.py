from django.urls import path, include

urlpatterns = [
    path('account/', include('django.contrib.auth.urls')),
]
