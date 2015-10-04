from django.db import models
from usuarios.models import MyUser

# Create your models here.
class Transaction(models.Model):
	id_employees = models.ForeignKey(MyUser, related_name='empleados')
	id_employers = models.ForeignKey(MyUser, related_name='empleadores')
	date = models.DateTimeField(auto_now=True)
	price = models.FloatField(default=0.0)

