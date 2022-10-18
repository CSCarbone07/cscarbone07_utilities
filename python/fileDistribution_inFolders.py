
import numpy as np
import glob, os
import re

# this is used to take the files from a folder a distribute them into folders, each file gets its
# own folder

fileDir = os.path.dirname(os.path.realpath('__file__'))
fileDir_toRead = os.path.join(fileDir, 'tmp_toRead_5/')
fileDir_toWrite = os.path.join(fileDir, 'tmp_toWrite_5/')
filename_train = os.path.join(fileDir, '../sets/train.txt')
filename_test = os.path.join(fileDir, '../sets/test.txt')

#f_out_train = open(filename_train, 'w')
#f_out_test = open(filename_test, 'w')
in_format = ".txt"
out_formats = [".txt", ".jpg"]
print("starting ")
print(fileDir_toRead)

#dirct = os.listdir()
#print(dirct)
#print(dirct.sort(key=os.path.getmtime))

count = 1

for file in sorted(os.listdir(fileDir_toRead)):
    if file.endswith(in_format):


        #filename = os.path.join(fileDir_toWrite, file)
        print(file)

        newFolder = fileDir_toWrite + file.split('.')[0]
        cmd_dir = "mkdir " + newFolder
        print(cmd_dir)
        os.system(cmd_dir)

        for outFormat in out_formats:
            file_in = fileDir_toRead + file.split('.')[0] + outFormat
            file_out = newFolder + "/" + file.split('.')[0] + outFormat
            cmd = "cp " + file_in + " " + file_out
            
            print(cmd)
            os.system(cmd)

        #f_in = open(file, 'r')
        #f_out = open(filename, 'w')




