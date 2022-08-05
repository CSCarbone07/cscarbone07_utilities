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




if __name__ == '__main__':


    calibraiton_data_set_path = os.path.abspath("/home/cscarbone/Dataset/Sensor/errors/viewPoint/")
    #calibraiton_data_set_path = os.path.abspath("/home/cscarbone/Dataset/Real/CKA_160523/annotations/dlp/")

    #calibraiton_data_set_path = os.path.abspath("/home/cscarbone/Dataset/synthetic_sugarbeet_random_weeds/synthetic_sugarbeat_random_weeds/")

    #data_set_path = os.path.abspath("/home/cscarbone/Documents/SPQR_Aerial/Calibration/calibration_Jai/")
    print(calibraiton_data_set_path)
    rgb_img_path = calibraiton_data_set_path + '/rgb/'
    nir_img_path = calibraiton_data_set_path + '/nir/'
    tag_img_path = calibraiton_data_set_path + '/tag/'
    #tag_img_path = calibraiton_data_set_path + '/colorCleaned/'
    tagNorm_img_path = calibraiton_data_set_path + '/tagNorm/'


    merge_img_path = calibraiton_data_set_path + '/img/'
    canIprint = True
    canShowImage = False
    for x in [name for name in os.listdir(tag_img_path) if os.path.isfile(tag_img_path + name)]:       
        print(x)
        #rgbimg = cv2.imread(data_set_raw + leafFolder + x)
        tagimg = cv2.imread(tag_img_path + x)
        bwTag = cv2.imread(tag_img_path + x,0)
        
        if canShowImage:        
            cv2.imshow('image',tagimg)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            
        #rgbimg = cv2.imread(rgb_img_path + x)
        #nirimg = cv2.imread(nir_img_path + x,0)
        height, width, depth = tagimg.shape
        for h in range(0, height):
            for w in range(0, width): 
                if tagimg[h,w,2]>200:
                    #tagimg[h,w] = [150,150,150]
                    bwTag[h,w] = 200
                if tagimg[h,w,1]>200: 
                    #tagimg[h,w] = [255,255,255]
                    bwTag[h,w] = 255

        for h in range(0, height):
            for w in range(0, width): 
                if bwTag[h,w]<199:
                    #tagimg[h,w] = [150,150,150]
                    bwTag[h,w] = 0

   

                      
                #if canIprint:
                    #print(pix)
                    #canIprint = False
        
        
        cv2.imwrite(tagNorm_img_path + x, bwTag)

        
        if canShowImage:        
            cv2.imshow('image',bwTag)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            canShowImage = False        
    
    def fast():
        img = example.copy()
        height, width, depth = img.shape
        img[0:height, 0:width//4, 0:depth] = 0 # DO THIS INSTEAD
        return img 


        #b_channel, g_channel, r_channel = cv2.split(rgbimg)
        #alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 50 #creating a dummy alpha channel image.
        
        #img_BGRA = cv2.merge((b_channel, g_channel, r_channel, nirimg))
        
        #cv2.imwrite(merge_img_path + "prueba" + x, tagimg)
        
        #for y in range(len(tagimg)): 
        #    print (tagimg[y])
        #print(tagimg)
        exit()




