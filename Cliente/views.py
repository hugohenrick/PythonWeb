from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from Cliente.models import Clientes
from Cliente.forms import InsereClienteForm


# PÁGINA PRINCIPAL
# ----------------------------------------------

class IndexTemplateView(TemplateView):
    template_name = "website/index.html"


# LISTA DE CLIENTES
# ----------------------------------------------

class ClienteListView(ListView):
    template_name = "website/lista.html"
    model = Clientes
    context_object_name = "clientes"


# CADASTRAMENTO DE CLIENTES
# ----------------------------------------------

class ClienteCreateView(CreateView):
    template_name = "website/cria.html"
    model = Clientes
    form_class = InsereClienteForm
    success_url = reverse_lazy("website:lista_clientes")


# ATUALIZAÇÃO DE CLIENTES
# ----------------------------------------------

class ClienteUpdateView(UpdateView):
    template_name = "website/atualiza.html"
    model = Clientes
    fields = '__all__'
    context_object_name = 'cliente'
    success_url = reverse_lazy("website:lista_clientes")


# EXCLUSÃO DE CLIENTES
# ----------------------------------------------

class ClienteDeleteView(DeleteView):
    template_name = "website/exclui.html"
    model = Clientes
    context_object_name = 'cliente'
    success_url = reverse_lazy("website:lista_clientes")
