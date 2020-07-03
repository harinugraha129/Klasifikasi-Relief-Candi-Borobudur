# import itertools
# from sklearn.model_selection import train_test_split
from .localbinarypatterns import LocalBinaryPatterns
from sklearn.neighbors import KNeighborsClassifier
from imutils import paths
import cv2
# import pandas as pd
# import numpy as np


def get_lbpImg(image, points, radius):
	desc = LocalBinaryPatterns(points, radius)
	try:
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	except:
		# print('ERROR di:', imagePath)
		gray = image
	hist = desc.describe(gray)

	return hist

def get_lbpDataset(db, points, radius):
	desc = LocalBinaryPatterns(points, radius)
	data = []
	labels = []
	directory = []
	print("load dataset", db)
	data_training = 'media_dataset/%s' % db
	for imagePath in paths.list_images(data_training):
        # load the image, convert it to grayscale, and describe it
		image = cv2.imread(imagePath)
		try:
			gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		except:
			print('ERROR di:', imagePath)
		hist = desc.describe(gray)
        # extract the label from the image path, then update the
        # label and data lists
		# print(imagePath)
		directory.append(imagePath)
		labels.append(imagePath.split("\\")[-2])  # use "\\" in Windows
		data.append(hist)
	return data, labels, directory

def get_kNN_clasification(k, X_train, y_train, hist_test):
	neigh = KNeighborsClassifier(n_neighbors=k)
	neigh.fit(X_train, y_train)
    
	prediction = neigh.predict([hist_test])[0]
	return prediction


# # load dataset
# fiture, label = get_lbpDataset("jaffe", 8, 4)

# # load datatest
# img = cv2.imread("db/jaffe/UY/UY.DI2.150.tiff")
# # img = cv2.imread("db/yale/01/subject01.jpg")
# hist = get_lbpImg(img, 8, 4)
# predicted = get_kNN_clasification(1, fiture, label, hist)
# print(predicted)

# cv2.imshow("image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()