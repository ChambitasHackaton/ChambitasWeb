from django.db import models
from django.conf import settings


class Oficio(models.Model):

	OFICIOS_CHOICES = (
		('JR','Jardineria'),
		('LP','Limpieza'),
		('PE','Plomeria y electricidad'),
		('MA','Mascotas'),
		('EL','Electronica'),
		('AL','Albanileria'),
		('DEC','Decoraciones'),
		('CAR','Carpinteria'),
		('HER','Herreria'),
	)
	oficio = models.CharField(max_length=20, choices=OFICIOS_CHOICES)

