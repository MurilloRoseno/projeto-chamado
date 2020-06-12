# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import gettext_lazy as _
from sigc.constants import *

# Create your models here.
class Setor(models.Model):
    class Meta:
        verbose_name = 'Setor'
        verbose_name_plural = 'Setores'

    nome = models.CharField(verbose_name='Nome do Setor', max_length=50, blank=False)
    tipo = models.TextField(verbose_name='Tipo de Setor', choices=TIPOS_DE_SETOR.choices(), blank=False)
    contato = models.CharField(verbose_name='Ramal', max_length=9, blank=False)

    def __str__(self):
        return self.nome

class Chamado(models.Model):
    class Meta:
        verbose_name = 'Chamado'
        verbose_name_plural = 'Chamados'

    setor = models.ForeignKey(Setor, on_delete=models.CASCADE, null=False, blank=False)
    data_de_registro = models.DateTimeField(auto_now_add=True, verbose_name='Data de registro do chamado')
    situacao = models.IntegerField(verbose_name='Situação do Chamado', choices=TIPOS_DE_SITUACAO.choices(), default=1, null=False, blank=False)
    tipo = models.IntegerField(verbose_name='Tipo de Chamado', choices=TIPOS_DE_CHAMADO.choices(), null=False, blank=False)
    descricao = models.TextField(verbose_name='Descrição', null=False, blank=False)

    def __str__(self):
        return self.descricao