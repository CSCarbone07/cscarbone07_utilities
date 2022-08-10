import numpy as np
import matplotlib.pyplot as plt
import glob, os
import yaml
import random
import re
from matplotlib import colors
import cv2


from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


if __name__ == "__main__":
    
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    fileDir_read = os.path.join(fileDir, 'tmp_toRead/')
    fileDir_write = os.path.join(fileDir, 'tmp_toWrite/')
    filename = os.path.join(fileDir, 'sensor_abstract')

    random.seed(1)
    img_total = 100
    format_read1 = '.jpg'
    format_read2 = '.txt'
    format_write = '.png'

    img_list = os.listdir(fileDir_read)
    #print(img_list)

    randomRotation = 180

    outImgSize_xy = 1365
    outImgCrop_original_x = 853
    outImgCrop_original_y = 2218
    offsetPercentageRange = 0.25
    sizePercentageRange = 0.25

    color_ground = (0,0,0)
    color_plants = (255,255,255)
    color_polygon = (128,128,128)
       
    '''
    for i in range(1, img_total+1):
        print("Generating image " + str(i))
        img1 = img_list[random.randint(0,len(img_list)-1)]
        img2 = img_list[random.randint(0,len(img_list)-1)]
        alpha = random.random()
        selected_angleRotation1 = random.uniform(-randomRotation,randomRotation)
    '''

    for file in os.listdir(fileDir_read):
        if file.endswith(format_read1):
            print("reading image " + file)
            #img = open(file, 'r')  
            img_original = cv2.imread(fileDir_read + file)
            img = cv2.imread(fileDir_read + file)
            h, w, c = img.shape
        
            text_file_in = os.path.join(fileDir_read, file.split(".")[0] + ".txt")
            f_in = open(text_file_in, 'r')
            print("reading image " + text_file_in)

            background = np.array([[0,0],[0,h],[w,h],[w,0]], np.int32)
             
            cv2.fillPoly(img, [background], color_ground)
            
            while(True):
                #read next line
                line_in = f_in.readline()
                line_in_np = np.array(line_in.split()).astype(float)
                
                if not line_in or line_in_np.shape[0]<=1:
                    break

                #if line is empty, you are done with all lines in the file
                line_out = ''


                rectangle = np.array([[10,5],[10,225],[50,225],[50,5]], np.int32)

                shapeUsed = Polygon(rectangle)
                rectangle = np.array([ \
                [(line_in_np[1]-line_in_np[3]/2)*w,(line_in_np[2]-line_in_np[4]/2)*h], \
                [(line_in_np[1]-line_in_np[3]/2)*w,(line_in_np[2]+line_in_np[4]/2)*h], \
                [(line_in_np[1]+line_in_np[3]/2)*w,(line_in_np[2]+line_in_np[4]/2)*h], \
                [(line_in_np[1]+line_in_np[3]/2)*w,(line_in_np[2]-line_in_np[4]/2)*h] \
                ], np.int32)
                print("Addint rectangle with points")
                print(rectangle)
                    
                cv2.fillPoly(img, [rectangle], color_plants)

       
            polygon_colorRange_minimum = 125
            polygon_colorRange_maximum = 130

            #height, width, depth = tagimg.shape
            for hi in range(0, h):
                for wi in range(0, w): 
                    if img_original[hi,wi,0]>=polygon_colorRange_minimum and
                    img_original[hi,wi,0]<=polygon_colorRange_maximum \
                    and img_original[hi,wi,1]>=polygon_colorRange_minimum and
                    img_original[hi,wi,1]<=polygon_colorRange_maximum \
                    and img_original[hi,wi,2]>=polygon_colorRange_minimum and
                    img_original[hi,wi,2]<=polygon_colorRange_maximum:
                        #tagimg[hi,wi] = [150,150,150]
                        img[hi,wi,0] = 128 
                        img[hi,wi,1] = 128
                        img[hi,wi,2] = 128 
            

            filename = fileDir_write + file
            print("saving image at " + filename)
            cv2.imwrite(filename, img)
            

            #you can access the line
            #print(line.strip())







