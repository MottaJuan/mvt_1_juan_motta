from django.db import models

"""
La clase del modelo, deberá guardar mínimo un número, una cadena y una fecha (puede guardar más cosas)
"""

class Familiares(models.Model):
    nombre=models.CharField(max_length=128)
    fecha_nacimiento=models.DateField()
    numero_fav=models.IntegerField()
    banda_fav=models.CharField(max_length=128)
    