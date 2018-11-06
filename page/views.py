
from django.views.generic import TemplateView
from .models import YEARS, Filial, Loko

class Home(TemplateView):
	template_name = 'page/home.html'


	def get_context_data(self, **kwargs):
		context = super(Home, self).get_context_data(**kwargs)
		context["year1"]		=  YEARS[0][1]
		context["year2"]		=  YEARS[-1][1]
		context["filials"]		=  Filial.objects.all()
		context["lokos"]		=  Loko.objects.all()
		return context