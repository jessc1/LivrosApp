from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError 

# creating a validator function 
def validar_preco_maior_que_zero(preco): 
    if preco > 0: 
        return preco 
    else: 
        raise ValidationError("O preço deve ser maior que zero") 

class Livros(models.Model):
    nome =models.CharField(max_length=50, unique=True)
    autor = models.CharField(max_length = 30, unique=True)
    qtd_paginas = models.IntegerField()
    preco =  models.DecimalField(max_digits=6, decimal_places=2, validators=[validar_preco_maior_que_zero])
    data_inclusao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse('livros_detail',args=[str(self.id)])
