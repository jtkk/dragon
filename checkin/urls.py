from django.conf.urls import url

from . import views

app_name = 'checkin'
urlpatterns = [
	url(r'^$', views.locations, name='locations'), # /checkin/
	url(r'^FoodBank/$', views.FoodBank, name='FoodBank'), # /checkin/FoodBank
]