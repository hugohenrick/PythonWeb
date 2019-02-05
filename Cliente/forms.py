from Cliente.models import Clientes
from django import forms


# FORMULÁRIO DE INCLUSÃO DE CLIENTES
# -------------------------------------------

class InsereClienteForm(forms.ModelForm):

    # chefe = forms.BooleanField(
    #     label='Chefe?',
    #     required=False,
    # )
    #
    # biografia = forms.CharField(
    #     label='Biografia',
    #     required=False,
    #     widget=forms.Textarea
    # )

    class Meta:
        # Modelo base
        model = Clientes

        # Campos que estarão no form
        fields = [
            'razao_social',
            'nome_fantasia',
            'cnpj',
            'telefone',
            'email'
        ]
