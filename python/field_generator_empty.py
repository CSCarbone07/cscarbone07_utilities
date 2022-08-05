import os

currentPath = os.path.dirname(os.path.abspath(__file__))
outputPath = currentPath + "/tmp"
outputName = "/field_"
outputFormat = ".yaml"

print(outputPath)

seed = 5
fieldSize_x = 16
fieldSize_y = 16

for i in range(0,25):
    file_out = outputPath + outputName + str(i+1) + outputFormat
    with open(file_out, 'w+') as f:
        print("writting " + file_out)
        
        # 5 0 0 0 0
        # seed id x y density 
       
        id = 0
        for y in range(fieldSize_y):
            for x in range(fieldSize_x):
                line_out = str(seed) \
                        + " " + str(id) \
                        + " " + str(x) \
                        + " " + str(y) \
                        + " 0" \
                        + "\n"
                f.write(line_out)
                id += 1
