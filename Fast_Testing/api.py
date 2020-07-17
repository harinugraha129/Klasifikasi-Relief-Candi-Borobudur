# import the necessary packages
import numpy as np
import urllib
import json
import os
import cv2
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.core.files.storage import FileSystemStorage
from myWebsite.settings import MEDIA_ROOT
from lib.main_function import get_lbpDataset
from lib.knn import get_knn_clasification
from lib.main_function import get_lbpImg, get_kNN_clasification
from Testing.models import DataTesting
from lib.database import DB
DB.init()

@csrf_exempt
@api_view(['POST', ])
def testing(request):

	point = 8
	radius = 4
	nilai_k = 1
	fs = FileSystemStorage()
	uploaded_file = request.FILES['image']
	# get file name
	name = fs.save(uploaded_file.name, uploaded_file)
	print(name)
	# get directori
	directory = fs.url(name)
	# get directory OS
	file_name = os.path.join(MEDIA_ROOT,uploaded_file.name)
	print(file_name)
	img = cv2.imread(file_name)
	lbp_value = get_lbpImg(img, int(point), int(radius))

	# result = get_kNN_clasification(int(nilai_k), data, label, lbp_value)
	tb_dataTraining = DB.find('tb_fastDataTraining')
	dt_lbp = []
	dt_label = []
	for data in tb_dataTraining:
		lbp = data['lbp'].split(",")
		lbp = list(np.float_(lbp))

		dt_lbp.append(lbp)
		dt_label.append(data['label'])

	result = get_knn_clasification(int(nilai_k), dt_lbp, dt_label, lbp_value)

	final_result = DataTesting.objects.create(
    		image = name,
		    label = result[0],
		    directory = directory
		)
	
	response={
		'response'	:'sukses post',
		'result' 	: result[0]
	}
	return JsonResponse(response)