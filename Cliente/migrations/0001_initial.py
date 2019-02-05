# Generated by Django 2.1.5 on 2019-02-04 22:25

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=14)),
                ('razao_social', models.CharField(max_length=255)),
                ('nome_fantasia', models.CharField(max_length=255)),
                ('insc_estadual', models.CharField(max_length=20, null=True)),
                ('insc_municipal', models.CharField(max_length=20, null=True)),
                ('cep', models.CharField(blank=True, max_length=9, null=True)),
                ('endereco', models.CharField(max_length=40, null=True)),
                ('numero', models.CharField(max_length=10, null=True)),
                ('complemento', models.CharField(blank=True, max_length=30, null=True)),
                ('bairro', models.CharField(max_length=50, null=True)),
                ('cidade', models.CharField(max_length=50, null=True)),
                ('uf', models.CharField(max_length=2, null=True)),
                ('contato', models.CharField(max_length=30, null=True)),
                ('telefone', models.CharField(max_length=30, null=True)),
                ('celular', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='E-mail')),
                ('site', models.CharField(max_length=50, null=True)),
            ],
            managers=[
                ('objetos', django.db.models.manager.Manager()),
            ],
        ),
    ]
