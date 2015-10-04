from usuarios.models import MyUser
from oficios.models import Oficio
from django.http import HttpResponse
from django.template import Context, loader

def search_results(request):
	parameters = {
		'oficio': request.GET.get('oficio'),
		'delegacion': request.GET.get('delegacion'),
		'codigo_postal': request.GET.get('cp'),
		'oficio': request.GET.get('oficio'),
	}
	usuarios = MyUser.objects.all().filter(oficio=1)
	print(usuarios)
	if not request.GET.get('aa'):
		print('ups')
	else:
		print('yey')
	template = loader.get_template('test.html')
	return HttpResponse(template.render())