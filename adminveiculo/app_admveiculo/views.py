from django.shortcuts import render

from.models import TipoDeVeiculo
# Create your views here.
def index(request):

    consulta_no_banco = TipoDeVeiculo.objects.all()

    return render(request, 'index.html',
                   {'consulta_no_banco': consulta_no_banco})