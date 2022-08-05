
import numpy as np
import glob, os
import re


fileDir = os.path.dirname(os.path.realpath('__file__'))
fileDir_toWrite = os.path.join(fileDir, '../boxes_classNormalized/')
filename_train = os.path.join(fileDir, '../sets/train.txt')
filename_test = os.path.join(fileDir, '../sets/test.txt')

f_out_train = open(filename_train, 'w')
f_out_test = open(filename_test, 'w')
print("starting ")

#dirct = os.listdir()
#print(dirct)
#print(dirct.sort(key=os.path.getmtime))

count = 1

for file in os.listdir(fileDir):
    #for file in sorted( filter( os.path.isfile,glob.glob(fileDir + '*') ) ):
	if file.endswith(".txt"):


		#filename = os.path.join(fileDir_toWrite, file)
		print(file)

		#f_in = open(file, 'r')
		#f_out = open(filename, 'w')


		if count <= 100:
		    f_out_train.write(file[:-4])
		    f_out_train.write('\n')
		else:
		    f_out_test.write(file[:-4])
		    f_out_test.write('\n')

		count += 1


