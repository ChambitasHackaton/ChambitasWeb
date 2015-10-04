from usuarios.models import MyUser
from oficios.models import Oficio
from django.views.generic import TemplateView
from django.template import Context, loader

class SearchResults(TemplateView):
	template_name = 'search_results.html'
	
	def get_context_data(self, **kwargs):
		context = super(SearchResults, self).get_context_data(**kwargs)
		parameters = {
			'delegacion': self.request.GET.get('delegacion').upper().replace('-', ' '),
			'zip_code': self.request.GET.get('cp'),
			'oficio': self.request.GET.get('oficio').upper().replace('-', ' '),
		
		}
		print (parameters)
		try:
			oficio = Oficio.objects.only('id').get(oficio = parameters['oficio']).id
			usuarios = MyUser.objects.all().filter(
				oficio = oficio,
				delegacion = parameters['delegacion'],
				zip_code = parameters['zip_code'],
			)
		except:
			usuarios = []
		context['usuarios'] = usuarios
		return context