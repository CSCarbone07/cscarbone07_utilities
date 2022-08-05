
import numpy as np
import matplotlib.pyplot as plt
import glob, os
import yaml
import random
import re
from matplotlib import colors
import cv2

fileDir = os.path.dirname(os.path.realpath('__file__'))
fileDir_toWrite = os.path.join(fileDir, '../rgb_motionBlur/')
filename = os.path.join(fileDir, 'sensor_abstract')
  


for file in os.listdir(fileDir):
	if file.endswith(".png"):
		#img = open(file, 'r')	
		img = cv2.imread(file)

		filename = os.path.join(fileDir_toWrite, file)
		print(filename)

		# Specify the kernel size. 
		# The greater the size, the more the motion. 
		kernel_size = random.randint(1, 10)
		print("kernel size " + str(kernel_size))
		  
		if kernel_size>0:
			# Create the vertical kernel. 
			kernel_v = np.zeros((kernel_size, kernel_size)) 
			  
			# Create a copy of the same for creating the horizontal kernel. 
			kernel_h = np.copy(kernel_v) 
			  
			# Fill the middle row with ones. 
			kernel_v[:, int((kernel_size - 1)/2)] = np.ones(kernel_size) 
			kernel_h[int((kernel_size - 1)/2), :] = np.ones(kernel_size) 
			  
			# Normalize. 
			kernel_v /= kernel_size 
			kernel_h /= kernel_size 
			  
			# Apply the vertical kernel. 
			vertical_mb = cv2.filter2D(img, -1, kernel_v) 
			  
			# Apply the horizontal kernel. 
			horizonal_mb = cv2.filter2D(img, -1, kernel_h) 
			  
			#dirname = os.path.dirname(__file__)
			#filename = os.path.join(dirname, '/rgb/')




			# Save the outputs. 
			cv2.imwrite(filename, vertical_mb) 
			#cv2.imwrite('car_horizontal.jpg', horizonal_mb) 


			#b_channel, g_channel, r_channel = cv2.split(img)

			#alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 50 #creating a dummy alpha channel image.

			#img_BGRA = cv2.merge((b_channel, g_channel, r_channel, alpha_channel))
		else:
			
			cv2.imwrite(filename, img)





