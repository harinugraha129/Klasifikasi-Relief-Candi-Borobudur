from django.urls import path

from Testing.api.views import api_data_testing

app_name = 'testing'

urlpatterns = [
	path('<slug>/', api_data_testing, name="detail_testing"),
]