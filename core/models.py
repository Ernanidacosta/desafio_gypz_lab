from django.db import models

class Solicitante(models.Model):
    nome = models.CharField(max_length=50)
    renda = models.FloatField()
    score = models.IntegerField(default=0)
    data  = models.DateField(auto_now_add=True)
    limit = models.FloatField('Limite', default=0)
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.nome