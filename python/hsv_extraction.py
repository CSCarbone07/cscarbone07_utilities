import glob, os
import numpy as np
import cv2
 
if __name__ == '__main__':

    fileDir = os.path.dirname(os.path.realpath('__file__'))
    fileDir_toRead = os.path.join(fileDir, 'tmp_toRead/')
    fileDir_toWrite = os.path.join(fileDir, 'tmp_toWrite/')
    filename = os.path.join(fileDir, 'tmp')
    tempImageFileName = os.path.join(fileDir_toRead, "ground_02.png")

    
    format_read = '.png'
    format_write = '.png'

    print(fileDir)
    print(fileDir_toRead)

    sum_hue = np.empty(0)
    sum_sat = np.empty(0)
    sum_val = np.empty(0)

    for file in os.listdir(fileDir_toRead):
        if file.endswith(format_read):
            #IplImage *img, *hsv, *hue, *sat, *val
            key = 0
            #CvSize size;
            currentFilename = fileDir_toRead + file 
            img = cv2.imread(currentFilename)
            print(currentFilename)
         
            # Create a hsv image with 3 channels and hue, sat e val with 1 channel.
            #   All with the same size 
            #size, depth = cvGetSize(img)
            height, width, depth = img.shape
            size = (height, width)
            #depth = img.depth
           
            '''
            hue = cvCreateImage(size, depth, 1)
            sat = cvCreateImage(size, depth, 1)
            val = cvCreateImage(size, depth, 1)
            hsv = cvCreateImage(size, depth, 3)
            cvZero(hue)
            cvZero(sat)
            cvZero(val)
            cvZero(hsv)
            '''   
            hue = np.zeros((height,width, 1) ,np.uint8)
            sat = np.zeros((height,width, 1) ,np.uint8)
            val = np.zeros((height,width, 1) ,np.uint8)
            hsv = np.zeros((height,width, 3) ,np.uint8)
             

            #/* Convert from Red-Green-Blue to Hue-Saturation-Value */
            #img_hsv = cvCvtColor( img, hsv, CV_BGR2HSV )
            hsv = cv2.cvtColor( img, cv2.COLOR_BGR2HSV)
         
            #/* Split hue, saturation and value of hsv on them */
            #cvSplit(hsv, hue, sat, val, 0)
            hue, sat, val = cv2.split(hsv)
            
         
            #/* Create windows, display them, wait for a key */
            '''
            cvNamedWindow("original", CV_WINDOW_AUTOSIZE)
            cvNamedWindow("hue", CV_WINDOW_AUTOSIZE)
            cvNamedWindow("saturation", CV_WINDOW_AUTOSIZE)
            cvNamedWindow("value", CV_WINDOW_AUTOSIZE)
         
            cvShowImage("original", img)
            cvShowImage("hue", hue)
            cvShowImage("saturation", sat)
            cvShowImage("value", val)
            '''
            
            '''
            cv2.imshow("original", img)
            cv2.imshow("hue", hue)
            cv2.imshow("saturation", sat)
            cv2.imshow("value", val)
            
            #cvWaitKey(0)
            cv2.waitKey(0)
            '''

            #/* Free memory and get out */
            '''
            cvDestroyWindow("original")
            cvDestroyWindow("hue")
            cvDestroyWindow("saturation")
            cvDestroyWindow("value")
            
            cvReleaseImage(&img)
            cvReleaseImage(&hsv)
            cvReleaseImage(&hue)
            cvReleaseImage(&sat)
            cvReleaseImage(&val)
            '''

            hue_min = 0
            hue_min = 360
            sat_min = 0
            sat_min = 100
            val_min = 0
            val_min = 100
            '''
            for h in range(0, height):
                for w in range(0, width): 
                    if hue[h,w]>:
                    if sat[h,w]>200:
                    if val[h,w]>200:
                        #tagimg[h,w] = [150,150,150]
            '''

            hue_avg = np.mean(hue)
            sat_avg = np.mean(sat)
            val_avg = np.mean(val)
            hue_std = np.std(hue)
            sat_std = np.std(sat)
            val_std = np.std(val)

            print("hue avg " + str(hue_avg))
            print("hue std " + str(hue_std))
            print("sat std " + str(sat_avg))
            print("sat std " + str(sat_std))
            print("val avg " + str(val_avg))
            print("val std " + str(val_std))

            sum_hue = np.append([sum_hue], [hue])
            sum_sat = np.append([sum_sat], [sat])
            sum_val = np.append([sum_val], [val])
            #print(hue_sum.shape)


    print('getting overall values of all images')

    sum_hue_avg = np.mean(sum_hue)
    sum_sat_avg = np.mean(sum_sat)
    sum_val_avg = np.mean(sum_val)
    sum_hue_std = np.std(sum_hue)
    sum_sat_std = np.std(sum_sat)
    sum_val_std = np.std(sum_val)

    print("hue avg " + str(sum_hue_avg))
    print("hue std " + str(sum_hue_std))
    print("sat std " + str(sum_sat_avg))
    print("sat std " + str(sum_sat_std))
    print("val avg " + str(sum_val_avg))
    print("val std " + str(sum_val_std))



