from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.


# Django automatically creates id = models.AutoField(primary_key=True) for each
# model.

# For the Member table, we're manually specifying a barcode_id field to be the
# primary_key.
@python_2_unicode_compatible # used to support Python 2
class Member(models.Model):
	barcode_id = models.CharField(max_length=7, primary_key="True")
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	date_of_birth = models.DateField()
	# Set address to null="True" for now. Change later.
	address = models.CharField(max_length=50, null="True")

	# The following is used to return the details rather than [<Member: Member
	# object>]
	def __str__(self):
		return '%s %s' % (self.first_name, self.last_name)

@python_2_unicode_compatible # used to support Python 2
class Location(models.Model):
	LOCATION_TYPE = (
		('fb', 'Food Bank'),
		('cb', 'Club Bamboo'),
	)
	location_name = models.CharField(max_length=50)
	location_type = models.CharField(max_length=2, choices=LOCATION_TYPE)

	# The following is used to return the details rather than [<Location: Location object>]
	def __str__(self):
		return self.location_name

@python_2_unicode_compatible # used to support Python 2
class AttendanceRecord(models.Model):
	date = models.DateField()

	# If the member referred to in an AttendanceRecord is deleted, the member will
	# be set to null in this (AttendanceRecord) table. Alternatively,
	# models.SET_NULL can be changed to models.CASCADE to delete the entry, or
	# models.PROTECT to keep the referenced member entry from being deleted in the
	# first place.
	member = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL)
	location = models.ForeignKey(Location, on_delete=models.PROTECT)

	def __str__(self):
		return '%s %s %s' % (self.date, self.member, self.location)
