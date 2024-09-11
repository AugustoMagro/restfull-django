from django.db import models

class Aluno(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=False, max_length=30)
    cpf = models.CharField(max_length=11)
    date_born = models.CharField(max_length=11)
    phone = models.CharField(max_length=14)

    def __str__(self):
        return self.name
    
class Treino(models.Model):

    NIVEL = (
        ('1','Iniciante'),
        ('2', 'Intermediário'),
        ('3', 'Avançado'),
    )

    name = models.CharField(max_length=10, blank=False)
    descricao = models.CharField(max_length=200)
    nivel = models.CharField(max_length=10 ,choices=NIVEL)
