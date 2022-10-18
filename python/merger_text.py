
import numpy as np
import glob, os
import re


if __name__ == "__main__":
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    fileDir_read = os.path.join(fileDir, 'tmp_toRead_text/')
    fileDir_write = os.path.join(fileDir, 'tmp_toWrite_text/')
    filename = os.path.join(fileDir, 'sensor_abstract')
  

    filename_write = fileDir_write + "mergedTexts" + ".txt"
    f_out = open(filename_write, 'w')

    print(fileDir_read)

    for file in os.listdir(fileDir_read):
        #print(file)
        if file.endswith(".txt"):


            filename_toOpen = os.path.join(fileDir_read, file)
            print(filename_toOpen)

            f_in = open(filename_toOpen, 'r')

            lineCounter = 0
            while(True):
                lineCounter += 1
                

                #read next line
                line_in = f_in.readline()
                #if line is empty, you are done with all lines in the file
                line_out = line_in

                '''
                first_character = True
                for c in range(len(line_in)):
                    if first_character:
                        first_character = False
                        line_out += '0'
                    else:
                        line_out += line_in[c]
                #line_out = line_in[0] = '0'
                '''

                if lineCounter >= 2:
                    f_out.write(line_out)
                

                #you can access the line
                #print(line.strip())

                if not line_in:
                    break


              






