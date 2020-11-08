from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Aviso
# Create your views here.
class AvisosListView(ListView):

    model = Aviso
    paginate_by = 10
    template_name = 'aviso_list.html'
    ordering = ['-created_at']

class AvisosCreateView(CreateView):

    model = Aviso
    fields = '__all__'
    template_name = 'aviso_form.html'
    success_url = reverse_lazy('home')
