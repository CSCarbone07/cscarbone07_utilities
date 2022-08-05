from PIL import Image
from math import *

import numpy as np
import matplotlib.pyplot as plt
import glob, os
import yaml
import random
import re
from matplotlib import colors
import cv2

import img2texture


if __name__ == "__main__":

    

    fileDir = os.path.dirname(os.path.realpath('__file__'))
    fileDir_read = os.path.join(fileDir, 'tmp_toRead')
    fileDir_read = os.path.join(fileDir, 'tmp_toWrite')
    fileDir_write = os.path.join(fileDir, 'tmp_toWrite2')
    filename = os.path.join(fileDir, 'sensor_abstract')

    format_read = ".png"
    format_write = ".png"

    overlap = 0.25
    

    for file in os.listdir(fileDir_read):
            if file.endswith(format_read):

                    filename_read = os.path.join(fileDir_read, file)
                    
                    filename_write = os.path.join(fileDir_write, file[:-4])
                    filename_write += format_write

                    cmd_overlap = " --overlap " + str(overlap)

                    cmd_rm = "rm " + filename_write
                    print(cmd_rm)
                    os.system(cmd_rm)


                    cmd = "img2texture " + filename_read + " " + filename_write + cmd_overlap
                    print(cmd)
                    os.system(cmd)
                
