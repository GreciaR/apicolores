from django.db import models

# Create your models here (aquí se ponen todos los modelos (funciones) de la aplicación)

class Color(models.Model):
	name = models.CharField(max_length=40, blank=False, unique=True)
	hexadecimal = models.CharField(max_length=7, unique=True)
	red = models.PositiveSmallIntegerField()
	green = models.PositiveSmallIntegerField()
	blue = models.PositiveSmallIntegerField()

	def __str__(self):
		return self.name