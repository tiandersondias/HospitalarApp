from django.db import models
from PIL import Image

# Create your models here.
class Hospital (models.Model):
    """Representa a entidade hospital"""
    nome_hospital = models.CharField(max_length=200)
    foto = models.ImageField(null=True, blank=True)
    desc_hospital = models.TextField
    tipo_hospital = models.CharField(max_length=200)
    conceito_hospital = models.CharField(max_length=200)

    def __str__(self):
        """Retorna uma representação de um string do modelo"""
        return self.nome_hospital