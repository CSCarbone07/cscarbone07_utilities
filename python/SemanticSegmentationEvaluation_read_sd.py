import os, os.path
import yaml
#import cv2
import numpy as np
from argparse import ArgumentParser
import glob
import math
import shutil
import random
import os
import math
#from astropy.units import fP



def getStringNumber(line):

    start = line.find(':') + 2
    end = line.find('\n', start)
    number = float(line[start:end])

    return number

if __name__ == '__main__':


    #calibraiton_data_set_path = os.path.abspath("/home/cscarbone/.config/unity3d/DefaultCompany/AgriSim/Dataset/")
    calibration_data_set_path = os.path.abspath("/home/cscarbone/Dataset/Real/CKA_160523/annotations/dlp/colorCleaned/")
    #calibration_data_set_path = os.path.abspath("/home/cscarbone/Dataset/synthetic_sugarbeet_random_weeds/synthetic_sugarbeat_random_weeds/tag/")
    classification_data_set_path = os.path.abspath("/home/cscarbone/bonnResults/")

    #data_set_path = os.path.abspath("/home/cscarbone/Documents/SPQR_Aerial/Calibration/calibration_Jai/")
    #print(calibration_data_set_path)
    #rgb_cla_path = classification_data_set_path + '/log_unreal_randomWeeds_use_randomWeeds/'
    rgb_cla_path = classification_data_set_path + '/log3_unity4_use/'
    nir_cla_path = classification_data_set_path + '/log1_unity4_use/'
    rgbn_cla_path = classification_data_set_path + '/log4_unity4_use/'
    real_cla_path = calibration_data_set_path + '/'
    rgb_img_path = calibration_data_set_path + '/rgb/'
    nir_img_path = calibration_data_set_path + '/nir/'
    tag_img_path = calibration_data_set_path + '/tag/'

    merge_img_path = calibration_data_set_path + '/img/'
    
    useNIR = True
    
    '''
    file.write("Hello World") 
    file.write("\n")
    file.write("This is our new text file") 
    file.write("\n")
    file.write("and this is another line.")
    file.write("\n") 
    file.write("Why? Because we can.") 
    '''
    list = os.listdir(real_cla_path)
    list.sort()
    
    imgCount = 0
    totalRGBiouAccuracy = 0
    totalRGBNiouAccuracy = 0

    totalRGBPlantAccuracy = 0
    totalRGBWeedAccuracy = 0
    totalRGBGroundAccuracy = 0
    totalRGBmeanAccuracy = 0
    totalRGBNPlantAccuracy = 0
    totalRGBNWeedAccuracy = 0
    totalRGBNGroundAccuracy = 0
    totalRGBNmeanAccuracy = 0

    totalPlantIoU_rgb = 0
    totaWeedIoU_rgb = 0
    totalGroundIoU_rgb = 0
    
    totalPlantIoU_rgbn = 0
    totaWeedIoU_rgbn = 0
    totalGroundIoU_rgbn = 0
    
    totalMeanIoU_rgb = 0
    totalMeanIoU_rgbn = 0
    
    string_ImageNumber = "Image:"
    string_rgbIoUmean = "RGB IoU Mean:"
    string_rgbnIoUplant = "RGBN IoU Plant:"
    string_rgbnIoUweed = "RGBN IoU Weed:"
    string_rgbnIoUground = "RGBN IoU Ground:"
    string_rgbnIoUmean = "RGBN IoU Mean:"
    #string_RGBPlantAccuracy = "RGB IoU Plant:"
    #string_RGBPlantAccuracy = "RGB IoU Plant:"
    string_totalRGBPlantAccuracy = 'Total RGB Plant Accuracy:' 

    accumulated_sd_plant = 0
    accumulated_sd_weed = 0
    accumulated_sd_ground = 0
    accumulated_sd_mean = 0
    sd_mean_plant = 0.023052595555782318
    sd_mean_weed = 0.018362360075116158
    sd_mean_ground = 0.7601234316825867
    sd_mean_mean = 0.2671794593334198
    
    lastImage = None
    currentImage = 0
    max_RGBPlantIoU = 0
    max_RGBNPlantIoU = 0
    max_RGBPlantAccuracy = 0
    max_diff_IoUmean = 0
    max_diff_IoUmean_image = None
    min_diff_IoUmean = 0
    min_diff_IoUmean_image = None
    minPositive_diff_IoUmean = 0
    minPositive_diff_IoUmean_image = None
    last_rgbIoUmean = 0
    last_rgbnIoUmean = 0
    fileName = 'bonnClassificationResults_sugarbeets_sensorError_unity_v04'

    #f=open('/home/cscarbone/bonnClassificationResults_unity4.txt', 'r')
    with open('/home/cscarbone/'+ fileName + '.txt', 'r') as f:
        if f.mode == 'r':
            for line in f:
                

                
                if string_ImageNumber in line:
                    start = line.find(':') + 2
                    end = line.find('.', start) 
                    currentImage = float(line[start:end])
                    print(lastImage)
                    print(last_rgbnIoUmean - last_rgbIoUmean)
                    if max_diff_IoUmean == 0 or (max_diff_IoUmean < last_rgbnIoUmean - last_rgbIoUmean):
                        if (last_rgbnIoUmean - last_rgbIoUmean) < 0.16358:
                            max_diff_IoUmean = last_rgbnIoUmean - last_rgbIoUmean
                            max_diff_IoUmean_image = lastImage
                    if min_diff_IoUmean == 0 or (min_diff_IoUmean > last_rgbnIoUmean - last_rgbIoUmean):
                        min_diff_IoUmean = last_rgbnIoUmean - last_rgbIoUmean
                        min_diff_IoUmean_image = lastImage
                    if minPositive_diff_IoUmean == 0 or ((last_rgbnIoUmean - last_rgbIoUmean)>0 and (minPositive_diff_IoUmean > last_rgbnIoUmean - last_rgbIoUmean)):
                        minPositive_diff_IoUmean = last_rgbnIoUmean - last_rgbIoUmean
                        minPositive_diff_IoUmean_image = lastImage
                    lastImage = line
    
                if string_rgbIoUmean in line and not ("Total" in line):               
                    number = getStringNumber(line)
                    last_rgbIoUmean = number
                    print(number)
                    #if number > max_RGBPlantAccuracy:
                        #max_RGBPlantAccuracy = number #float(line[start:end])
                        #print(currentImage)
                        #print(max_RGBPlantIoU)
                        #print(number)
                        
                if not ("Total" in line):
                    if string_rgbnIoUplant in line:  
                        number = getStringNumber(line)
                        accumulated_sd_plant += pow((number-sd_mean_plant),2)
                    if string_rgbnIoUweed in line:    
                        number = getStringNumber(line)           
                        accumulated_sd_weed += pow((number-sd_mean_weed),2)
                    if string_rgbnIoUground in line:    
                        number = getStringNumber(line)
                        accumulated_sd_ground += pow((number-sd_mean_ground),2)           
                    if string_rgbnIoUmean in line:               
                        number = getStringNumber(line)
                        #print(line)
                        last_rgbnIoUmean = number
                        accumulated_sd_mean += pow((number-sd_mean_mean),2)
                        imgCount += 1
                        print(number)

                    #if number > max_RGBPlantAccuracy:
                        #max_RGBPlantAccuracy = number #float(line[start:end])

            #contents = f.readlines()
            #contents = f.read()
            #f.close()
    #file=open("/home/cscarbone/bonnClassificationResults_unity4_read.txt", "w")
    #file.write(contents)
    #file.write("Best averages")
    #file.write("Image: " + str(imgCount) + ". Name: " + x)
    #file.write("\n")
    print("max_diff_IoUmean_image:")
    print(max_diff_IoUmean_image)
    print(max_diff_IoUmean)
    print("min_diff_IoUmean_image:")
    print(min_diff_IoUmean_image)
    print(min_diff_IoUmean)
    print("minPositive_diff_IoUmean_image:")
    print(minPositive_diff_IoUmean_image)
    print(minPositive_diff_IoUmean)
    #file.write("Max Difference" + "\n")
    sd_mean_plant = math.sqrt(accumulated_sd_plant/imgCount);
    sd_mean_weed = math.sqrt(accumulated_sd_weed/imgCount);
    sd_mean_ground = math.sqrt(accumulated_sd_ground/imgCount);
    sd_mean_mean = math.sqrt(accumulated_sd_mean/imgCount);
    print("sd " + str(sd_mean_mean))

    with open('/home/cscarbone/'+ fileName + '.txt', 'a') as f:
        f.write("\n")
        f.write("RGBN IoU sd plant: " + str(sd_mean_plant) + "\n")
        f.write("RGBN IoU sd weed: " + str(sd_mean_weed) + "\n")
        f.write("RGBN IoU sd ground: " + str(sd_mean_ground) + "\n")
        f.write("RGBN IoU sd mean: " + str(sd_mean_mean) + "\n")

    #for x in contents:
        #print(x)
        
    












