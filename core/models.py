from django.db import models

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=30)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    estoque = models.IntegerField('Quantidade em Estoque')

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=30
                            )
    sobrenome = models.CharField('Sobrenome', max_length=30)
    email = models.CharField('E-mail', max_length=30)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
