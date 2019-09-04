from django.db import models

class Professor(models.Model):
    nome = models.CharField(
        max_length = 255,
    )

    idade = models.IntegerField()

    def __str__(self):
       return self.nome + ' a idade do professor é ' + self.idade