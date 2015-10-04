from django.shortcuts import render
from usuarios.forms import MyUserForm
from usuarios.models import MyUser

def home(request):
	form = MyUserForm 
	return render(request, 'home.html', {'form' : form})