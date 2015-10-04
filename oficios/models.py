from django.db import models
from django.conf import settings


class Oficio(models.Model):

	OFICIOS_CHOICES = (
		('JARDINERIA','Jardineria'),
		('LIMPIEZA','Limpieza'),
		('PLOMERIA Y ELECTRICIDAD','Plomeria y electricidad'),
		('MASCOTAS','Mascotas'),
		('ELECTRONICA','Electronica'),
		('ALBANILERIA','Albanileria'),
		('DECORACIONES','Decoraciones'),
		('CARPINTERIA','Carpinteria'),
		('HERRERIA','Herreria'),
	)
	oficio = models.CharField(max_length=25, choices=OFICIOS_CHOICES)

	def __unicode__(self):
		return self.oficio