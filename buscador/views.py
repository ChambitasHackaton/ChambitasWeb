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
	oficio = Oficio.objects.all().filter(oficio = parameters['oficio'])
	usuarios = MyUser.objects.all().filter(oficio = oficio,
											zip_code = parameters['codigo_postal'],
											delegacion = parameters['delegacion'],)
	print(usuarios)
	if not request.GET.get('aa'):
		print('ups')
	else:
		print('yey')
	template = loader.get_template('test.html')
	return HttpResponse(template.render())