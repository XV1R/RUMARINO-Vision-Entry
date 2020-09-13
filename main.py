
import os,sys
sys.path.append("./images/")
sys.path.append("./model/")
sys.path.append("./src/")
from src import fileutils, darknetutils, cvutils



data = fileutils.files2list( "./images", ".jpg" )
#map applies the anonymous function to everything in the list; returns map object which can be treated as a list
#saves us a for loop
paths = list(map(lambda x: "./images/"+str(x),data))

#writes the training data 
with open("train.txt","w") as trainFile:
    for image in paths:
        trainFile.write(image)
        trainFile.write("\n")
    trainFile.close()


#test file 
test_lines = open("train.txt","r").readlines()
with open("test.txt","w") as testFile:
    for line in test_lines:
        testFile.write(line)
    testFile.close()


#My darknet installation is in /opt/
#Use the path to call darknet from this folder 
#NOTE: currently generates log file and is able to open graph
#NOTE: The custom.name file is copied into the overall folder; couldn't get the script to find it 
darknetutils.darknet_pretrain("/opt/darknet/darknet","./model/yolov3-tiny-generated.cfg","yolov3-tiny.weights")
darknetutils.darknet_train("/opt/darknet/darknet", "./model/detector.data", "./model/yolov3-tiny-generated.cfg","pretrained-weights.conv.15")
