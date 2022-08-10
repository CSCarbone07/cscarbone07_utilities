
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

fileDir = os.path.dirname(os.path.realpath('__file__'))
fileDir_toWrite = os.path.join(fileDir, '../rgb_polygon/')
filename = os.path.join(fileDir, 'sensor_abstract')
fileDir_text_in = os.path.join(fileDir, '../boxes/')
fileDir_text_out = os.path.join(fileDir, '../boxes_polygon/')

random.seed(1)

for file in os.listdir(fileDir):
    if file.endswith(".png"):
        #img = open(file, 'r')  
        img = cv2.imread(file)
        h, w, c = img.shape

        filename = os.path.join(fileDir_toWrite, file)

        text_file_in = os.path.join(fileDir_text_in, file.split(".")[0] + ".txt")
        text_file_out = os.path.join(fileDir_text_out, file.split(".")[0] + ".txt")
        f_in = open(text_file_in, 'r')
        f_out = open(text_file_out, 'w')

        print(filename)
        print(text_file_out)



        # Specify the kernel size. 
        # The greater the size, the more the motion. 
        #kernel_size = random.randint(1, 10)
        #print("kernel size " + str(kernel_size))

        #side_h = random.randint(0, 1)
        #side_v = random.randint(0, 1)
        side = random.randint(0,3)
        ext1 = random.random()*0.7
        ext2 = random.random()*0.7

        #rectangle = np.array([[10,5],[10,225],[50,225],[50,5]], np.int32)
        #rectangle = np.array([[50,5],[10,5],[10,225],[50,225]], np.int32)
        rectangle = np.array([[10,5],[10,225],[50,225],[50,5]], np.int32)


        if side == 0:
            rectangle[0] = [0,0]
            rectangle[1] = [0,h]
            rectangle[2] = [ext1*w,h]
            rectangle[3] = [ext2*w,0]
        elif side == 1: 
            rectangle[0] = [0,h]
            rectangle[1] = [w,h]
            rectangle[2] = [w,h-ext1*h]
            rectangle[3] = [0,h-ext2*h]
        elif side == 2: 
            rectangle[0] = [w,h]
            rectangle[1] = [w,0]
            rectangle[2] = [w-ext1*w,0]
            rectangle[3] = [w-ext2*w,h]
        elif side == 3: 
            rectangle[0] = [w,0]
            rectangle[1] = [0,0]
            rectangle[2] = [0,ext1*h]
            rectangle[3] = [w,ext2*h]


        isClosed = False
        color = (128,128,128)
        thickness = 2

        #cv2.polylines(img, [rectangle], isClosed, color, thickness)
        cv2.fillPoly(img, [rectangle], color)

        cv2.imwrite(filename, img)


        while(True):
            #read next line
            line_in = f_in.readline()
            line_in_np = np.array(line_in.split()).astype(float)
            
            if not line_in or line_in_np.shape[0]<=1:
                break

            #if line is empty, you are done with all lines in the file
            line_out = ''
            '''
            first_character = True
            for c in range(len(line_in)):
                if first_character:
                    first_character = False
                    line_out += '0'
                else:
                    line_out += line_in[c]
            '''

            #line_out = line_in[0] = '0'
            #continue
            #print(line_in_np.astype(np.float))
            isInside = False

            shapeUsed = Polygon(rectangle)
            points = np.array([ \
            [(line_in_np[1]-line_in_np[3]/2)*w,(line_in_np[2]-line_in_np[4]/2)*h], \
            [(line_in_np[1]-line_in_np[3]/2)*w,(line_in_np[2]+line_in_np[4]/2)*h], \
            [(line_in_np[1]+line_in_np[3]/2)*w,(line_in_np[2]+line_in_np[4]/2)*h], \
            [(line_in_np[1]+line_in_np[3]/2)*w,(line_in_np[2]-line_in_np[4]/2)*h] \
            ])
            #print(points)

                
            for p in points:
                #print(p)
                if shapeUsed.contains(Point(p[0],p[1])):
                    isInside = True             


            if not isInside:
                f_out.write(line_in)    

            
            

            #you can access the line
            #print(line.strip())
            




