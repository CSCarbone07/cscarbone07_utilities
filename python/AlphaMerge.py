import os, os.path
import yaml
import cv2
import numpy as np
from argparse import ArgumentParser
import glob
import math
import shutil
import random
import os
import math
#export PYTHONIOENCODING=utf-8



if __name__ == '__main__':


    #calibraiton_data_set_path = os.path.abspath("/home/cscarbone/.config/unity3d/DefaultCompany/AgriSim/Dataset/")
    #calibraiton_data_set_path = os.path.abspath("/home/cscarbone/Dataset/Real/CKA_160523/images/")
    #calibraiton_data_set_path = os.path.abspath("/home/cscarbone/Dataset/Unity4/")
    calibraiton_data_set_path = os.path.abspath("/home/cscarbone/Dataset/Sensor/errors/motionBlur_horizontal/")
    #calibraiton_data_set_path = os.path.abspath("/home/cscarbone/Dataset/University/NIR+RGB/sunflower2/jesi_05_18_unitySampleRemoved/")
    #data_set_path = os.path.abspath("/home/cscarbone/Documents/SPQR_Aerial/Calibration/calibration_Jai/")

    rgb_img_path = calibraiton_data_set_path + '/rgb/'
    nir_img_path = calibraiton_data_set_path + '/nir/'
    tag_img_path = calibraiton_data_set_path + '/tag/'

    merge_img_path = calibraiton_data_set_path + '/img/'
    
    print(calibraiton_data_set_path) 
    print(rgb_img_path)   
    print(nir_img_path)   
    print(tag_img_path)   
    print(merge_img_path)   
  
       
    for x in [name for name in os.listdir(rgb_img_path) if os.path.isfile(rgb_img_path + name)]:       
        #rgbimg = cv2.imread(data_set_raw + leafFolder + x)
        
        tagimg = cv2.imread(tag_img_path + x,0)
        rgbimg = cv2.imread(rgb_img_path + x, cv2.IMREAD_UNCHANGED)
        nirimg = cv2.imread(nir_img_path + x,0)
        

        b_channel, g_channel, r_channel = cv2.split(rgbimg)
        #alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 50 #creating a dummy alpha channel image.
        
        img_BGRA = cv2.merge((b_channel, g_channel, r_channel, nirimg))
        print(merge_img_path + x)
        print(img_BGRA)
        #cv2.imwrite(merge_img_path + "prueba" + x, tagimg)
        cv2.imwrite(merge_img_path + x, img_BGRA)
        
        #for y in range(len(tagimg)): 
            #print (tagimg[y])
        #print(tagimg)
        #exit()
        



