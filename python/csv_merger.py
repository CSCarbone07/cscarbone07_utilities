
import numpy as np
import glob, os
import re


fileDir = os.path.dirname(os.path.realpath('__file__'))
#fileDir_toWrite = os.path.join(fileDir, '../boxes_classNormalized/')
filename = os.path.join(fileDir, 'sensor_abstract')
  

fileDir_toRead = os.path.join(fileDir, "tmp_read")
fileDir_toWrite = os.path.join(fileDir, "tmp_write")

fileToWrite = os.path.join(fileDir, 'agisoft_transforms.csv')
f_out = open(fileToWrite, 'w')

print("starting loop")
print(fileDir)
print(fileDir_toRead)
firstLoop = True
for file in os.listdir(fileDir_toRead):
        if file.endswith(".txt"):


                fileWithoutExtension = os.path.splitext(file)[0]
                
                filenameToRead = os.path.join(fileDir_toRead,
                        fileWithoutExtension + ".txt")
                print(file)
                print(filenameToRead)

                f_in = open(filenameToRead, 'r')


                line_in = f_in.readlines()
                if (firstLoop):
                    f_out.write(line_in[0])
                line_out = line_in[1]
                f_out.write(line_out)


                  
                firstLoop = False





