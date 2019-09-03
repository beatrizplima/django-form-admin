from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(
        max_length = 255,
        verbose_name = 'Nome'
    )

    idade = models.CharField(
        max_length = 10,
        verbose_name = 'Idade'
    )

    email = models.CharField(
        max_length=255,
        verbose_name ='E-mail',
        unique = True
    )

    def __str__(self):
       return self.nome + ' sua idade é ' + self.idade + ' seu e-mail é ' + self.email