from django.shortcuts import render
from datetime import date
from .models import Location, Client, AttendanceRecord
from .forms import AttendanceRecordForm

# Create your views here.

def locations(request):
	locations_list = Location.objects.all()
	context = {"locations": locations_list}
	return render(request, 'checkin/locations.html', context)

def FoodBank(request):
	loc_id = request.GET.get('loc_id')
	location = Location.objects.get(pk=loc_id)

	if request.method == "POST":
		ar_form = AttendanceRecordForm(request.POST)
		if ar_form.is_valid():
			ar = ar_form.save(commit=False)
			ar.date = date.today()
			ar.location_id = location
			ar.save()
	else:
		ar_form = AttendanceRecordForm()

	context = {'location': location, 'date': date.today(), 'ar_form': ar_form}
	return render(request, 'checkin/FoodBank.html', context)
