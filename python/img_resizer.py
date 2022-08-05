
import numpy as np
import matplotlib.pyplot as plt
import glob, os
import yaml
import random
import re
from matplotlib import colors
import cv2

fileDir = os.path.dirname(os.path.realpath('__file__'))
fileDir_toWrite = os.path.join(fileDir, '../rgb_reduced/')
filename = os.path.join(fileDir, 'sensor_abstract')
  
resize_height = 300
resize_width = 300


for file in os.listdir(fileDir):
	if file.endswith(".png"):
		#img = open(file, 'r')	
		img = cv2.imread(file)

		filename = os.path.join(fileDir_toWrite, file[:-4])
		filename = filename + '.jpg'
		print(filename)

		new_shape = (resize_height,resize_width)
		img = cv2.resize(img, new_shape, interpolation=cv2.INTER_LINEAR)


		# Save the outputs. 
		cv2.imwrite(filename, img) 





