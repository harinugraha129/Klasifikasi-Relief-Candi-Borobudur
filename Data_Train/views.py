from django.shortcuts import render
import pandas as pd
import os
from lib.main_function import get_lbpDataset, get_Dataset

from django.conf import settings
from myWebsite.settings import MEDIA_ROOT
from django.core.files.storage import FileSystemStorage
my_storage = FileSystemStorage(location=os.path.join(settings.BASE_DIR, 'angga'))

from lib.database import DB
DB.init()
# Create your views here.
def index(request): 
	print(my_storage)
	# data, label, directory = get_lbpDataset('data_train', 8, 4)
	label, directory = get_Dataset('data_train')

	DB.delete_all('tb_dataTraining')
	for x in range(len(label)):
		
		# file_name = os.path.join("/home/night/Documents/Python3/TA_Wasis/myWebsite/",directory[x])

		# string = ""
		# for z in data[x]:
		# 	if string == "":
		# 		string = str(z)
		# 	else:
		# 		string += ","+str(z)

		data_tabel = {
			# 'lbp'	: string,
			'label'	: label[x],
			'directory'	: directory[x],
			# 'file_name'	: file_name,
		}
		DB.insert('tb_dataTraining', data_tabel)

	tb_dataTraining = DB.find('tb_dataTraining')

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
	return render(request, 'Data_Train/index.html', context)

