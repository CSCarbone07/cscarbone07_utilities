
import numpy as np
import matplotlib.pyplot as plt
import glob, os
import yaml
import random
import re
from matplotlib import colors
import cv2

fileDir = os.path.dirname(os.path.realpath('__file__'))
fileDir_read = os.path.join(fileDir, 'tmp_toRead/')
fileDir_write = os.path.join(fileDir, 'tmp_toWrite/')
filename = os.path.join(fileDir, 'sensor_abstract')
  
format_read = '.png'
format_write = '.png'

img_list = os.listdir(fileDir_read)
print(img_list)


'''
for file in os.listdir(fileDir_read):
	if file.endswith(format_read):
		#img = open(file, 'r')	
		img = cv2.imread(file)

		filename_write = os.path.join(fileDir_write, file[:-4])
		filename_write = filename_write + format_write
		print(filename_write)





		new_shape = (resize_height,resize_width)
		img = cv2.resize(img, new_shape, interpolation=cv2.INTER_LINEAR)


		# Save the outputs. 
		cv2.imwrite(filename, img) 
'''




