from django.db import models


class Autor(models.Model):
    nome = models.CharField(max_length=70)
    email = models.EmailField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.nome} ({self.id})"

    class Meta:
        verbose_name_plural = "Autores"
        verbose_name = "Autor"
