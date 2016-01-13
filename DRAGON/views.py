
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.shortcuts import render

class HomeView(TemplateView):
	template_name = 'index.html'
def FoodBank(request):
        return render(request, 'FoodBank.html', {})
