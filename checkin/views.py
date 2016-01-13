from django.shortcuts import render

# Create your views here.

def locations(request):
	return render(request, 'checkin/locations.html', {})