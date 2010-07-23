from django.db import models
import datetime
# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField("Proprietário",
                            max_length=100,
                            help_text='Nome do Proprietário do Imóvel')
    cpf = models.IntegerField("CPF",
                              max_length=11)
    tel1 = models.IntegerField()
    tel2 = models.IntegerField()
    tel3 = models.IntegerField()

class Inquilino(Pessoa):
    pass

class Proprietario(Pessoa):
    pass

    
class Imovel(models.Model):
    dono = models.ForeignKey(Proprietario)
    inquilino = models.ForeignKey(Inquilino)
    ##casa/apartamento/escritorio/fazenda...
    tipo = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
    cidade = models.CharField(max_length=100)
    bairro = models.CharFIeld(max_length=100)
    endereco = models.TextField("Endereço do Imóvel")
    ##tamanho da propriedade em metros quadrados
    tamanho = models.IntegerField("Área Útil do Imóvel")
    qtdDormitorios = models.IntegerField()    
    ##a seguir: true --> disponivel para venda/aluguel
    aluguel = models.BooleanField()
    venda = models.BooleanField()
    ##condiçao geral do imovel
    condicao = models.CharField(max_length=50)
    descricao = models.TextField("Descrição do Imóvel")
    ##valores-base para venda/aluguel
    valorAluguel = models.IntegerField()
    valorVenda = models.IntegerField()




    
