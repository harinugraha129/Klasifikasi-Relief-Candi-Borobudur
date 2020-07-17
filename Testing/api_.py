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

@csrf_exempt
def detect(request):
	# initialize the data dictionary to be returned by the request
	data = {"success": False}
	# check to see if this is a post request
	if request.method == "POST":
		# check to see if an image was uploaded
		if request.FILES.get("image", None) is not None:
			# grab the uploaded image
			image = _grab_image(stream=request.FILES["image"])
		# otherwise, assume that a URL was passed in
		else:
			# grab the URL from the request
			url = request.POST.get("url", None)
			# if the URL is None, then return an error
			if url is None:
				data["error"] = "No URL provided."
				return JsonResponse(data)
			# load the image and convert
			image = _grab_image(url=url)
		### START WRAPPING OF COMPUTER VISION APP
		# Insert code here to process the image and update
		# the `data` dictionary with your results
		### END WRAPPING OF COMPUTER VISION APP
		# update the data dictionary
		data["success"] = True
	# return a JSON response
	return JsonResponse(data)
def _grab_image(path=None, stream=None, url=None):
	# if the path is not None, then load the image from disk
	if path is not None:
		image = cv2.imread(path)
	# otherwise, the image does not reside on disk
	else:	
		# if the URL is not None, then download the image
		if url is not None:
			resp = urllib.urlopen(url)
			data = resp.read()
		# if the stream is not None, then the image has been uploaded
		elif stream is not None:
			data = stream.read()
		# convert the image to a NumPy array and then read it into
		# OpenCV format
		image = np.asarray(bytearray(data), dtype="uint8")
		image = cv2.imdecode(image, cv2.IMREAD_COLOR)
 
	# return the image
	return image

# @permission_classes([IsAuthenticated, ])
@csrf_exempt
@api_view(['GET'])
def test_api(request):
	data = {
		'data'	: 'contoh 1',
		'data2'	: 'contoh 2',
		'data3'	: 'contoh 3',
	}
	return JsonResponse(data)

@csrf_exempt
@api_view(['POST', ])
def test_post(request):
	fs = FileSystemStorage()
	uploaded_file = request.FILES['image']
	# get file name
	name = fs.save(uploaded_file.name, uploaded_file)
	# get directori
	directory = fs.url(name)
	# get directory OS
	file_name = os.path.join(MEDIA_ROOT,uploaded_file.name)
	response={
		'response':'sukses post'
	}
	return JsonResponse(response)

@csrf_exempt
@api_view(['POST', ])
def test_lantai(request):
	data = {
		'data'	: request.POST['lantai'],
	}
	response={
		'response':'sukses post '+str(request.POST['lantai'])
	}
	return JsonResponse(response)

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
	print(lbp_value)


	data, label, direc = get_lbpDataset('data_train', int(point), int(radius))
	print(data)

	# result = get_kNN_clasification(int(nilai_k), data, label, lbp_value)
	result = get_knn_clasification(int(nilai_k), data, label, lbp_value)
	print(result)
	
	response={
		'response'	:'sukses post',
		'result' 	: result[0]
	}
	return JsonResponse(response)