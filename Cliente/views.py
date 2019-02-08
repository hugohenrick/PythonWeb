from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from Cliente.models import Clientes
from Cliente.forms import InsereClienteForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render


# PÁGINA PRINCIPAL
# ----------------------------------------------

class IndexTemplateView(TemplateView):
    template_name = "website/index.html"

# LISTA DE PAGINAÇÃO
# ----------------------------------------------
def listing(request):
    clientes_lista = Clientes.objetos.all()
    paginator = Paginator(clientes_lista, 2) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        clientes = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        clientes = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        clientes = paginator.page(paginator.num_pages)

    return render(request, 'lista.html', {'clientes': clientes})


# LISTA DE CLIENTES
# ----------------------------------------------

class ClienteListView(ListView):
    template_name = "website/lista.html"
    model = Clientes
    context_object_name = "clientes"
    paginate_by = 8
    queryset = Clientes.objetos.all()  # Default: Model.objects.all(


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
    fields = [
        'razao_social',
        'nome_fantasia',
        'cnpj',
        'telefone',
        'email'
    ]
    context_object_name = 'cliente'
    success_url = reverse_lazy("website:lista_clientes")


# EXCLUSÃO DE CLIENTES
# ----------------------------------------------

class ClienteDeleteView(DeleteView):
    template_name = "website/exclui.html"
    model = Clientes
    context_object_name = 'cliente'
    success_url = reverse_lazy("website:lista_clientes")
