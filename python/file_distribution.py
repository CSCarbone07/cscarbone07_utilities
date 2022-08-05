import sys
import numpy as np
import glob, os
import re
import shutil
import random

fileDir = os.path.dirname(os.path.realpath('__file__'))
fileDir_toRead = os.path.join(fileDir, 'tmp_read')
fileDir_toWrite = os.path.join(fileDir, 'tmp_write')
filename = os.path.join(fileDir, 'sensor_abstract')

fileExtensions_toRead = [".jpg"]
fileExtensions_toCopy = [".txt",".jpg"]

distribution = [100,37,100]

dirs_toWrite = ["tmp_write", "tmp_write2", "tmp_write3"]

random_seed = 1
random.seed(random_seed)
random_fileOrder = True


print(len(sys.argv))
if (len(sys.argv)==3):
    print(sys.argv[0])
    print(sys.argv[1])
    print(sys.argv[2])
    fileDir_toRead = os.path.join(fileDir, sys.argv[1])
else:
    print("using default paths in script")
    print(fileDir_toRead)

fileList = []

for file in os.listdir(fileDir_toRead):
    for ext in fileExtensions_toRead:
        if file.endswith(ext):
            fileList.append(os.path.splitext(file)[0])


if random_fileOrder:
    random.shuffle(fileList)

print(fileList)

counter = 0
current_dir_index = 0
current_distribution_count = distribution[current_dir_index]

for file in fileList:
    print(file)
    counter +=1
    if counter > current_distribution_count:
        current_dir_index += 1
        if current_dir_index >= len(dirs_toWrite):
            quit()
        else:
            current_distribution_count += distribution[current_dir_index]
   
    fileToWrite = os.path.join(fileDir, dirs_toWrite[current_dir_index])
    
    for ext in fileExtensions_toCopy:
        shutil.copyfile(fileDir_toRead + "/" + file + ext, fileToWrite + "/" + file + ext)
