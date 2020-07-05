# import the necessary packages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import numpy as np
import urllib
from rest_framework.decorators import api_view
from django.core.files.storage import FileSystemStorage
from myWebsite.settings import MEDIA_ROOT
import json
import os
import cv2
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

@csrf_exempt
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
	data = {
		'data'	: request.POST['data'],
		'data1'	: request.POST['data1'],
		'data2'	: request.POST['data2'],
	}
	fs = FileSystemStorage()
	uploaded_file = request.FILES['gambar']
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