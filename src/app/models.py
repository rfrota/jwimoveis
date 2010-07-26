# -*- coding: utf-8 -*-
from django.db import models
import datetime
# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField("Proprietário",
                            max_length=100,
                            help_text='Nome do Proprietário do Imóvel',
                            blank=False,
                            null=False)
    cpf = models.IntegerField("CPF",
                              max_length=11,
                              primary_key=True)
    tel1 = models.IntegerField(null=True)
    tel2 = models.IntegerField(null=True)
    tel3 = models.IntegerField(null=True)
def __unicode__(self):
        return self.nome
class Inquilino(Pessoa):
    pass

class Proprietario(Pessoa):
    pass

    
class Imovel(models.Model):
    dono = models.ForeignKey(Proprietario)
    inquilino = models.ForeignKey(Inquilino,
                                  blank=True)
    ##casa/apartamento/escritorio/fazenda...
    tipo = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100,
                              blank=True)
    endereco = models.TextField("Endereço do Imóvel")
    ##tamanho da propriedade em metros quadrados
    tamanho = models.IntegerField("Área Útil do Imóvel",
                                  null=True)
    qtdDormitorios = models.IntegerField(null=True)    
    ##a seguir: true --> disponivel para venda/aluguel
    aluguel = models.NullBooleanField(null=True)
    venda = models.NullBooleanField(null=True)
    ##condiçao geral do imovel
    condicao = models.CharField(max_length=50,
                                blank=True)
    descricao = models.TextField("Descrição do Imóvel",
                                 blank=True)
    ##valores-base para venda/aluguel
    valorAluguel = models.IntegerField(null=True)
    valorVenda = models.IntegerField(null=True)
    def __unicode__(self):
        return '%s\n%s\n%s'(self.tipo,self.endereco,self.dono)




    
