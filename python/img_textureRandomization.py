from PIL import Image


import numpy as np
import matplotlib.pyplot as plt
import glob, os
import yaml
import random
import re
from matplotlib import colors
import cv2


def get_concat_h(im1, im2):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst

def get_concat_v(im1, im2):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst

def get_concat_h_double(im1, im2, im3):
    dst = Image.new('RGB', (im1.width + im2.width + im3.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    dst.paste(im3, (im1.width + im2.width, 0))
    return dst

def get_concat_v_double(im1, im2, im3):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height + im3.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    dst.paste(im3, (0, im1.height + im2.height))
    return dst

if __name__ == "__main__":

    fileDir = os.path.dirname(os.path.realpath('__file__'))
    fileDir_read = os.path.join(fileDir, 'tmp_toRead/')
    fileDir_write = os.path.join(fileDir, 'tmp_toWrite/')
    filename = os.path.join(fileDir, 'sensor_abstract')

    random.seed(1)
    img_total = 10
    format_read = '.png'
    format_write = '.png'

    img_list = os.listdir(fileDir_read)
    print(img_list)

    randomRotation = 180

    for i in range(img_total):
        print("Generating image " + str(i))
        img1 = img_list[random.randint(0,len(img_list)-1)]
        img2 = img_list[random.randint(0,len(img_list)-1)]
        alpha = random.random()
        selected_angleRotation1 = random.uniform(-randomRotation,randomRotation)
        selected_angleRotation2 = random.uniform(-randomRotation,randomRotation)
        print(img1)
        print(img2)
        print(alpha)
        print(selected_angleRotation1)
        print(selected_angleRotation2)

      
        """
        pil_img1 = Image.new('RGBA', size=(nw, nh), color=(0, 0, 0, 0))
        pil_img1.paste(img1)
        pil_img2 = Image.new('RGBA', size=(nw, nh), color=(0, 0, 0, 0))
        """
        # open
        pil_img1 = Image.open(fileDir_read + img1)
        pil_img2 = Image.open(fileDir_read + img2)
        # concatenate
        pil_img1 = get_concat_h_double(pil_img1,pil_img1,pil_img1)
        pil_img2 = get_concat_h_double(pil_img2,pil_img2,pil_img2)
        pil_img1 = get_concat_v_double(pil_img1,pil_img1,pil_img1)
        pil_img2 = get_concat_v_double(pil_img2,pil_img2,pil_img2)
        # rotate
        #pil_img1 = pil_img1.rotate(selected_angleRotation1, 0, 1, None, None, None)
        #pil_img2 = pil_img2.rotate(selected_angleRotation2, 0, 1, None, None, None)
        pil_img1 = pil_img1.rotate(selected_angleRotation1)
        pil_img2 = pil_img2.rotate(selected_angleRotation2)
        # recrop
        #pil_img1 = pil_img1.crop((1024,1024,2048,2048))
        #pil_img2 = pil_img2.crop((1024,1024,2048,2048))
        pil_img1 = pil_img1.crop((853,853,2218,2218))
        pil_img2 = pil_img2.crop((853,853,2218,2218))
        img_out = Image.blend(pil_img1,pil_img2,alpha)

        filename_write = os.path.join(fileDir_write, str(i))
        filename_write = filename_write + format_write
        print(filename_write)
        img_out.save(filename_write)

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




