from django.contrib import admin
from models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
	list_display = ('id', 'id_employees', 'id_employers', 'date', 'price')

# Register your models here.
