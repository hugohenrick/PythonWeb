from django.db import models

# Create your models here.
class Clientes(models.Model):

    cnpj = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )

    razao_social = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    nome_fantasia = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    insc_estadual = models.CharField(
        max_length=20,
        null=True,
        blank=False
    )

    insc_municipal = models.CharField(
        max_length=20,
        null=True,
        blank=False
    )

    cep = models.CharField(
        max_length=9,
        blank=True,
        null=True
    )

    endereco = models.CharField(
        max_length=40,
        blank=False,
        null=True
    )

    numero = models.CharField(
        max_length=10,
        blank=False,
        null=True
    )

    complemento = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )

    bairro = models.CharField(
        max_length=50,
        blank=False,
        null=True
    )

    cidade = models.CharField(
        max_length=50,
        blank=False,
        null=True
    )

    uf = models.CharField(
        max_length=2,
        blank=False,
        null=True
    )

    contato = models.CharField(
        max_length=30,
        blank=False,
        null=True
    )

    telefone = models.CharField(
        max_length=30,
        blank=False,
        null=True
    )

    celular = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )

    email = models.EmailField(
        'E-mail',
        blank=False,
        null=True
    )

    site = models.CharField(
        max_length=50,
        null=True
    )


    objetos = models.Manager()