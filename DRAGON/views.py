
from django.views.generic.base import TemplateView
<<<<<<< HEAD
from django.http import HttpResponse
=======
>>>>>>> locations
from django.shortcuts import render

class HomeView(TemplateView):
	template_name = 'index.html'
def FoodBank(request):
        return render(request, 'FoodBank.html', {})
