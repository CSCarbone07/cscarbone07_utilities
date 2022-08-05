


import os, os.path
import yaml
import cv2
import numpy as np
import matplotlib.pyplot as plt



dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, '/rgb/')
print(filename)

#b_channel, g_channel, r_channel = cv2.split(img)

#alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 50 #creating a dummy alpha channel image.

#img_BGRA = cv2.merge((b_channel, g_channel, r_channel, alpha_channel))



