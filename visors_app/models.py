from django.db import models

class InterfaceAR(models.Model):
    nombre = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='interfaces/')
    marcador = models.CharField(
        max_length=200, 
        choices=[
            ('hiro', 'Hiro Marker'),
            ('kanji', 'Kanji Marker'),
        ],
        default='hiro'
    )

    def __str__(self):
        return self.nombre

