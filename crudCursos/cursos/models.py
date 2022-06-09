from django.db import models


# Create your models here.

class Curso(models.Model):
    codigo=models.CharField(primary_key=True, max_length=5)
    nombre=models.CharField(max_length=50)
    nota=models.PositiveIntegerField()
    
    def __str__(self):
        txt="{0} ({1})"
        return txt.format(self.nombre, self.nota)