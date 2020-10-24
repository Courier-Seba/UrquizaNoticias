from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import UrquizaUserCreationForm

class UserCreationView(FormView):
    template_name = 'register.html'
    form_class = UrquizaUserCreationForm
    success_url = reverse_lazy('home')
