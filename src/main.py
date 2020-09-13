import fileutils, darknetutils, cvutils
import os,sys
sys.path.append("./images")


data = fileutils.files2list( "./images", ".jpg" )
#map applies the anonymous function to everything in the list; returns map object which can be treated as a list
#saves us a for loop
paths = list(map(lambda x: "./images/"+str(x),data))

#writes the training data into the model folder 
os.chdir("./model/")
with open("train.txt","w") as trainFile:
    for image in paths:
        trainFile.write(image)
        trainFile.write("\n")
    trainFile.close()
os.chdir("..")

#My darknet installation is in /opt/
#Use the path to call darknet from this folder 
#NOTE: currently only generates a log file
darknetutils.darknet_pretrain("/opt/darknet/darknet","./model/yolov3-tiny-generated.cfg","yolov3-tiny.weights")
darknetutils.darknet_train("/opt/darknet/darknet", "./model/detector.data", "./model/yolov3-tiny-generated.cfg","pretrained-weights.conv.15")
