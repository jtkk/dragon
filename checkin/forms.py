from django.forms import ModelForm, TextInput
from .models import AttendanceRecord

class AttendanceRecordForm(ModelForm):

	class Meta:
		model = AttendanceRecord
		fields = ('client_barcode_id',)
		# ForeignKey client_barcode_id defaults to a select box. Overriding
		# the widget to make it a text input.
		widgets = {
			'client_barcode_id': TextInput(attrs={'size': 7})
		}