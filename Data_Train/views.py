from django.shortcuts import render
import pandas as pd
from lib.main_function import get_lbpDataset
# Create your views here.
def index(request): 
    
	data, label, directory = get_lbpDataset('data_train', 8, 4)

	# data_train = {}
	# id = 1
	# for dt, lbl, dire in zip(data, label, directory):
	# 	data_train[]

	# data_train = dict(zip(list(data), list(label)))
	# print(data_train)

	data_train = {
		'data' : data,
		'label': label,
		'directory':directory
	}
	data_train = pd.DataFrame(data=data_train)
	data_train = data_train.to_dict()
	print(data_train)
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
        # 'tb_dataTraining' : data_train
        'data' : data,
		'label': label,
		'directory':directory
    }
	return render(request, 'Data_Train/index.html', data_train)

