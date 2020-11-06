from django.views.generic.list import ListView

from .models import Aviso
# Create your views here.
class AvisosListView(ListView):

    model = Aviso
    paginate_by = 10
    template_name = 'aviso_list.html'

