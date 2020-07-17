from django.shortcuts import render, redirect
import pandas as pd

import os
import cv2
from lib.knn import get_knn_clasification
from lib.main_function import get_lbpDataset, get_Dataset, get_lbpImg
import numpy as np
from .forms import DataTestForm
from django.conf import settings
from myWebsite.settings import MEDIA_ROOT
from django.core.files.storage import FileSystemStorage
my_storage = FileSystemStorage(location=os.path.join(settings.BASE_DIR, 'angga'))

from lib.database import DB
DB.init()

def refresh_dataTrain(request):
	# label, directory = get_Dataset('data_train')

	lbp, label, directory = get_lbpDataset('data_train', 8, 4)

	# local = get_lbpDataset('data_train', 8, 4)
	# print(local)

	DB.delete_all('tb_fastDataTraining')
	for x in range(len(label)):
		
	# 	# file_name = os.path.join("/home/night/Documents/Python3/TA_Wasis/myWebsite/",directory[x])

		string = ""
		for z in lbp[x]:
			if string == "":
				string = str(z)
			else:
				string += ","+str(z)

		data_tabel = {
			'lbp'	: string,
			'label'	: label[x],
			'directory'	: directory[x],
			# 'file_name'	: file_name,
		}
		DB.insert('tb_fastDataTraining', data_tabel)

	return redirect('fast_train')

# Create your views here.
def data_train(request): 
	
	

	tb_dataTraining = DB.find('tb_fastDataTraining')
	# data_train[0][0]
	# for data in data_train:
	# 	for dt in data:
	# 		print(dt)
	# 	print("\n")
	# 	print(data[0])
		# print(data['label'])
		# print(data['directory'])
		# print("\n")



	context = {
        'Judul' : 'Dataset',
        'SubJudul' : 'Berikut dataset yang akan digunakan sebagai data training k-NN',
        'tb_dataTraining' : tb_dataTraining
  #       'data' : data,
		# 'label': label,
		# 'directory':directory
    }
	return render(request, 'Fast_Testing/data_train.html', context)


from Testing.models import DataTesting
def upload(request):

	if request.method == 'POST':

		nilai_k = request.POST['nilai_k']
		# point = request.POST['point']
		# radius = request.POST['radius']

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
		# lbp_value = get_lbpImg(img, int(point), int(radius))
		lbp_value = get_lbpImg(img, 8, 4)
		print(lbp_value)

		# data, label, direc = get_lbpDataset('data_train', int(point), int(radius))
		# data, label, direc = get_lbpDataset('data_train', 8, 4)
		tb_dataTraining = DB.find('tb_fastDataTraining')
		dt_lbp = []
		dt_label = []
		for data in tb_dataTraining:
			lbp = data['lbp'].split(",")
			lbp = list(np.float_(lbp))

			dt_lbp.append(lbp)
			dt_label.append(data['label'])
			

		# result = get_kNN_clasification(int(nilai_k), data, label, lbp_value)
		result = get_knn_clasification(int(nilai_k), dt_lbp, dt_label, lbp_value)
		print(result)

		final_result = DataTesting.objects.create(
    		image = name,
		    label = result[0],
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
		return render(request, 'Fast_Testing/upload.html', context)


	
	form = DataTestForm()
	context = {
        'Judul'		 : 'Dataset',
        'SubJudul' : 'Data Testing',
        'form'		: form
    }
	return render(request, 'Fast_Testing/upload.html', context)