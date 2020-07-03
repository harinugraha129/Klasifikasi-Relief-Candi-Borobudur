from django.shortcuts import render, redirect
from .forms import DataTestForm
from .models import DataTesting

# Create your views here.
import pandas as pd
from lib.main_function import get_lbpDataset

from django.core.files.storage import FileSystemStorage
from myWebsite.settings import MEDIA_ROOT

import cv2
import os, sys

from lib.main_function import get_lbpImg, get_kNN_clasification
# from lib.database import DB
# Create your views here.
def index(request): 
    
	data, label, directory = get_lbpDataset('data_train', 8, 4)

	tb_dataTesting = DataTesting.objects.all()

	context = {
        'Judul' : 'Dataset',
        'SubJudul' : 'Data Testing',
        'tb_dataTesting' : tb_dataTesting
    }
	return render(request, 'Testing/index.html', context)

def upload(request):

	if request.method == 'POST':

		nilai_k = request.POST['nilai_k']
		point = request.POST['point']
		radius = request.POST['radius']

		fs = FileSystemStorage()
		uploaded_file = request.FILES['image']
		name = fs.save(uploaded_file.name, uploaded_file)
		print(name)
		directory = fs.url(name)
		# get directory OS
		file_name = os.path.join(MEDIA_ROOT,uploaded_file.name)
		# load image
		print(file_name)
		img = cv2.imread(file_name)
		lbp_value = get_lbpImg(img, int(point), int(radius))


		data, label, direc = get_lbpDataset('data_train', int(point), int(radius))

		result = get_kNN_clasification(int(nilai_k), data, label, lbp_value)
		print(result)

		final_result = DataTesting.objects.create(
    		image = name,
		    label = result,
		    directory = directory
		)

		form = DataTestForm()

		context = {
	        'Judul' 		: 'Form Pengujian',
	        'SubJudul' 		: 'Form Pengujian',
        	'hasil'			: result,
	        'directory'		: directory,
        	'form'			: form
    	}
		return render(request, 'Testing/upload.html', context)

	form = DataTestForm()
	context = {
        'Judul'		 : 'Dataset',
        'SubJudul' : 'Data Testing',
        'form'		: form
    }
	return render(request, 'Testing/upload.html', context)

def delete(request, id):
	
	tb_dataTesting = DataTesting.objects.get(id = id)
	print(tb_dataTesting)
	try:
		# dir_path = os.path.dirname(os.path.realpath(__file__))
		filepath = os.path.join(MEDIA_ROOT,tb_dataTesting.image)
		# print(MEDIA_ROOT)
		# print(tb_dataTesting.directory)
		print(filepath)
		os.remove(filepath)
	except:
		print('gagal hapus file')
	tb_dataTesting.delete()
	
	return redirect('testing')