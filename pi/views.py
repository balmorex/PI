from django.shortcuts import render
from django.http import HttpResponse	#n
from django.template import loader	#n
from django.http import Http404	#n
from .models import Pizza

from django.views import generic
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
# Create your views here.

class IndexView(generic.ListView):
	template_name='pi/index.html'
	context_object_name='pizza_list'

	def get_queryset(self):
		return Pizza.objects.all()

class HomeView(generic.DetailView):
	model=Pizza
	template_name='pi/home.html'


#nuevo
def home(request, pizza_id):
	pizza=get_object_or_404(Pizza, pk=pizza_id)
	#return HttpResponse("estas mirando la pizza: %s." % pizza_id)
	return render(request,'pi/home.html', {'pizza':pizza})

