from django.db import models

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=100)
    estoque = models.IntegerField('Quantidade em estoque')
    
    def __str__(self):
        return f'{self.nome}'
    
class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('Email', max_length=100)
    nascimento = models.DateField('Data de alteração', auto_now=True)

    
    def __str__(self) -> str:
        return f'{self.nome} {self.sobrenome}'