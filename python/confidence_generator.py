
import numpy as np
import matplotlib.pyplot as plt
import glob, os
import yaml
import random
import re
import math
from matplotlib import colors
import cv2
import sys
np.set_printoptions(threshold=sys.maxsize)

fileDir = os.path.dirname(os.path.realpath('__file__'))
fileDir_toWrite = os.path.join(fileDir, '../confidences/')
filename_ref = os.path.join(fileDir, '1_5.txt')
filename = os.path.join(fileDir, 'test_confidence.png')

W = 1024
H = 1024
img_shape = (H,W) #H x W
#location(y,x)(row,column)


def dnorm(x, mu, sd):
    return 1 / (np.sqrt(2 * np.pi) * sd) * np.e ** (-np.power((x - mu) / sd, 2) / 2)

def gaussian_kernel(size, sigma=1, verbose=False):
    #print("generating kernel")
    kernel_1D = np.linspace(-(size // 2), size // 2, size)
    for i in range(size):
        kernel_1D[i] = dnorm(kernel_1D[i], 0, sigma)
    #print(kernel_1D.T)
    kernel_2D = np.outer(kernel_1D.T, kernel_1D.T)
    '''
    print("kernel")
    print(kernel_1D.shape)    
    print(kernel_2D.max())
    '''
    kernel_2D *= 1.0 / kernel_2D.max()





    #final_image = np.zeros((img_shape[0], img_shape[1], 1), dtype = "uint8")

    #final_image = fill_a_with_b(final_image,kernel_2D,location) 

    #final_image_plot = fill_a_with_b(background,kernel_2D,location) 

    if verbose:
        plt.imshow(final_image_plot, interpolation='none',cmap='gray')
        plt.title("Image")
        plt.show()
        
    return kernel_2D


def fill_a_with_b(a, b, pos = [0,0]):
    print("slicing")
    print(a.shape)
    print(b.shape)

    boundaries = [pos[0] - int(b.shape[0]/2), pos[0] + int(b.shape[0]/2),
    pos[1] - int(b.shape[1]/2), pos[1] + int(b.shape[1]/2)]    
    aa = a.copy()
    bb = b.copy()

    cuttingPoints = [0,0,0,0]
    cutting = False
    if (pos[1]-b.shape[1]/2)<0:
        cutting = True
        #print("slice left")
        boundaries[2] = 0

    if (pos[0]-b.shape[0]/2)<0:
        cutting = True
        #print("slice up")
        boundaries[0] = 0
        bb = b.copy()[:,-(pos[1]-int(b.shape[1]/2)):]
    
    if (pos[1]+b.shape[1]/2)<0:
        cutting = True
        #print("slice right")
        boundaries[1] = img_shape[1]

    if (pos[1]-b.shape[1]/2)<0:
        cutting = True
        #print("slice down")
        boundaries[3] = img_shape[1]

    #bb = b.copy()[:,-(pos[1]-int(b.shape[1]/2)):]

    #aa[slice(pos[0] - int(b.shape[0]/2), pos[0] + int(b.shape[0]/2)), 
    #   slice(pos[1] - int(b.shape[1]/2), pos[1] + int(b.shape[1]/2))] = bb
    #aa[slice(boundaries[0], boundaries[1]), 
       #slice(boundaries[2], boundaries[3])] = bb
    
    return aa



if __name__ == '__main__':
    kernel_size = 100
    sigma=math.sqrt(kernel_size)
    print("starting")

    for file in os.listdir(fileDir):
        if file.endswith(".txt"):
    
            print(file)
            f_in = open(file, 'r')

            final_image = np.zeros((img_shape[0], img_shape[1], 1), dtype = "uint8")
            line = 1
            while(True):
                #read next line
                line_in = f_in.readline()
                line_in_np = np.array(line_in.split()).astype(float)
		        
                if not line_in or line_in_np.shape[0]<=1:
                    break
                
                if(line_in_np[3]<=0 or line_in_np[4]<=0):
                    continue                


                #print("doing line " + str(line))
                #line += 1               

                if(line_in_np[3]<line_in_np[4]):
                    kernel_size = int(line_in_np[3]*H)
                else:
                    kernel_size = int(line_in_np[4]*W)
                #print(kernel_size)
                sigma=math.sqrt(kernel_size)
                
                blur = gaussian_kernel(kernel_size,sigma,False)*255

                #final_image = fill_a_with_b(final_image,kernel_2D,location) 
                #location = [20,20] #(HxW)
                location = [line_in_np[2]*H,line_in_np[1]*W] #(HxW)


                #blur_img = blur.reshape(blur.shape[0],blur.shape[1],1)  
                blur_img = np.expand_dims(blur, axis=-1)


                for h in range(0, kernel_size):
                    for w in range(0, kernel_size):
                        '''
                        if(final_image[int(location[0]+(h-kernel_size/2))][int(location[1]+(w-kernel_size/2))][0]>0):
                            print("adding blur")
                            print(final_image[int(location[0]+(h-kernel_size/2))][int(location[1]+(w-kernel_size/2))][0])
                            print(blur_img[h][w][0])
                        '''
                        if (final_image[int(location[0]+(h-kernel_size/2))][int(location[1]+(w-kernel_size/2))][0]+blur_img[h][w][0])>255:
                            final_image[int(location[0]+(h-kernel_size/2))][int(location[1]+(w-kernel_size/2))][0] = 255

                        elif int(location[0]+(h-kernel_size/2)) >= 0 and int(location[1]+(w-kernel_size/2)) >= 0 and int(location[0]+(h-kernel_size/2)) < H and int(location[1]+(w-kernel_size/2)) < W:
                            final_image[int(location[0]+(h-kernel_size/2))][int(location[1]+(w-kernel_size/2))][0]+=blur_img[h][w][0]
                            '''
                            if final_image[int(location[0]+(h-kernel_size/2))][int(location[1]+(w-kernel_size/2))][0]>255:
                                print("above 255")                                
                                print(final_image[int(location[0]+(h-kernel_size/2))][int(location[1]+(w-kernel_size/2))][0])

                                final_image[int(location[0]+(h-kernel_size/2))][int(location[1]+(w-kernel_size/2))][0] = 255
                            
                                print(final_image[int(location[0]+(h-kernel_size/2))][int(location[1]+(w-kernel_size/2))][0])
                            '''

            #final_image = fill_a_with_b(final_image,blur_img,location) 
            #final_image2 = image.reshape(image.shape[0],image.shape[1],1)
            #final_image2 = np.expand_dims(image, axis=-1)

            #print(final_image)
            #print(final_image2)
            #print(file.split('.'))
        
            savefile = fileDir_toWrite+file.split('.')[0]+".png"
            cv2.imwrite(savefile, final_image) 






