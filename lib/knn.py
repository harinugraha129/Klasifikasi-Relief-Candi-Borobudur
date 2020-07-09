import pandas as pd
from .distance import chebishev_D



def get_knn_clasification(K, dataTraining, labels, dataTesting):
	#Menghitung Jarak Data
	y_pred = []
	Distance = []
	label = []
	for j in range(0, len(dataTraining) ):
		x = dataTesting
		y = dataTraining[j]
		Distance.append(chebishev_D(x,y, len(x)))
		label.append(labels[j])
		dataJarak = {'jarak' : pd.Series(Distance),
					'label' : pd.Series(label)} 

	# Mencari data terdekat dengan K
	df = pd.DataFrame(dataJarak, columns = ['jarak', 'label'])
	df = df.sort_values(by=['jarak'])
	df = df.head(K)
	
	# mengambil mayoritas dari label
	y_pred.append(df.groupby(["label"]).count().sort_values(by=['jarak']).
	tail(1).index.get_level_values('label')[0])
	print("manual knn")
	return y_pred
	# Mendapatkan Label Sebenarnya
	# y_true.append(dtTest[a][i][n_feature])