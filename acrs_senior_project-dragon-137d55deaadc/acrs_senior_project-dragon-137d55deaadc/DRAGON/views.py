
from django.views.generic.base import TemplateView
from django.shortcuts import render

class HomeView(TemplateView):
	template_name = 'index.html'

def StartPage(request):
        return render(request, 'start.html', {})