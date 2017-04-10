from django.contrib import admin

from app_admveiculo.models import TipoDeVeiculo, MarcaDeVeiculo, Veiculo

admin.site.register(TipoDeVeiculo)
admin.site.register(MarcaDeVeiculo)
admin.site.register(Veiculo)