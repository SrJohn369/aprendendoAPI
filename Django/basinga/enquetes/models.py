from django.db import models

# Create your models here.
class Questao(models.Model):
    questao_texto = models.CharField(max_length=200)
    data_publicacao = models.DateTimeField("data publicada")


class Escolha(models.Model):
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
    escolha_texto = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)