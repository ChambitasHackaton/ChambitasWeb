from django.shortcuts import render, redirect
from usuarios.models import MyUser
from django.views.generic import TemplateView
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from django.core.urlresolvers import reverse
from usuarios.admin import UserCreationForm

class Index(TemplateView):
	template_name = 'index.html'

	def get_context_data(self, **kwargs):
		context = super(Index, self).get_context_data(**kwargs)
		context['users'] = MyUser.objects.all()
		return context

def login(request):
	if request.method == 'POST':		
		email = request.POST['email']
		password = request.POST['password']
		user = authenticate(email=email, password=password)
		if user:
			auth_login(request, user)
			return render(request,'index.html')
		else:
			return render(request, "login.html")
	else:
		return render(request, "login.html")

def logout(request):
	auth_logout(request)
	return redirect(reverse('signup.html'))

def signup(request):
	form = UserCreationForm(request.POST or None)
	print form

	if form.is_valid():
		form.save()


	return render(request, 'signup.html', {'form' : form})