
import numpy as np
import glob, os
import re


fileDir = os.path.dirname(os.path.realpath('__file__'))
fileDir_toWrite = os.path.join(fileDir, '../boxes_classNormalized/')
filename = os.path.join(fileDir, 'sensor_abstract')
  


for file in os.listdir(fileDir):
	if file.endswith(".txt"):


		filename = os.path.join(fileDir_toWrite, file)
		print(filename)

		f_in = open(file, 'r')
		f_out = open(filename, 'w')


		while(True):
			#read next line
			line_in = f_in.readline()
			#if line is empty, you are done with all lines in the file
			line_out = ''
			first_character = True
			valueFound = False
			for c in range(len(line_in)):
				if c == 0 and line_in[c] == '-':
					continue
				if c == 1 and line_in[0] == '-':
					line_out += '0'
				else:
					line_out += line_in[c]
			#line_out = line_in[0] = '0'

			f_out.write(line_out)
			

			if not line_in:
				break
			#you can access the line
			#print(line.strip())



		  






