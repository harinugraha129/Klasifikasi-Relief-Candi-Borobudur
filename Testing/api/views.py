from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# from account.models import Account
from Testing.models import DataTesting
from Testing.api.serializers import DataTestingSerializer

@api_view(['GET', ])
def api_data_testing(request):

	try:
		data_testing = DataTesting.objects.all()
		print(data_testing)
		# return Response(serializers.data)
	except DataTesting.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == "GET":
		serializers = DataTestingSerializer(data_testing)
		return Response(serializers.data)