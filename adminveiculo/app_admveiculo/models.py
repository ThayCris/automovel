from django.db import models

class TipoDeVeiculo(models.Model):
    tipo = models.CharField('Tipo de Veículo', max_length=20,
                            help_text='Ex: Carro, Moto, Caminhão')

    def __str__(self):
        return "{}" . format(self.tipo)

    class Meta:
        ordering = ('tipo',)
        verbose_name = 'Tipo de Veículo'
        verbose_name_plural = 'Tipos de Veículos'

class MarcaDeVeiculo(models.Model):
    marca = models.CharField('Marca do Veiculo', max_length = 20,
                             help_text= 'Ex. Nissan, Renault, Chevrolet, Fiat')

    def __str__(self):
        return '{}' .format(self. marca)

    class Meta:
        ordering = ('marca',)
        verbose_name = 'Marca do Veículo'
        verbose_name_plural = 'Marcas dos Veículos'

class Veiculo(models.Model):
    tipo = models.ForeignKey(TipoDeVeiculo) # chaves estrangeiras
    marca = models.ForeignKey(MarcaDeVeiculo)

    modelo = models.CharField('Modelo', max_length=75)
    placa = models.CharField('Placa', max_length=75)
    cor = models.CharField('Cor', max_length=75)

    def __str__(self):
        return '{}' .format(self.placa, self.modelo)

    class Meta:
        ordering = ('tipo', 'marca', 'modelo')
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'

# python manage.py makemigrations - para criar as migrações do banco de dados
# python manage.py migrate - e para completar as migrações
# COLD9 TESTAR APLICAÇÃO
#procurar saber o que e post  guete




