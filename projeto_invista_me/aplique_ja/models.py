from django.db import models
from datetime import datetime

# Create your models here.
class Produto(models.Model):
    produto = models.TextField(max_length=255)
    quantidade = models.IntegerField(default=1)
    valor = models.FloatField()
    total = models.IntegerField(null=True)
    pago = models.BooleanField(default=False)
    data = models.DateField(default=datetime.now)


