

import numpy
from PIL import Image
import os
import cv2
from numpy import asarray
from PIL import Image, ImageFilter

# Importing Image and ImageFilter module from PIL package  
# creating a image object 
im1 = Image.open(r"/content/drive/MyDrive/mémoire/drive + clahe/03.png") 
# applying the median filter 
im2 = im1.filter(ImageFilter.MedianFilter(size = 3)) 
     
im2.save("/content/drive/MyDrive/03clahefilt.png")



#Meadin filter loop
path_1 = "/content/drive/MyDrive/ODIR/pathologiques1920-893/clahe/"
files = os.listdir(path_1)
for name in files:
    print(name)
    images_path = path_1 + name
    im1 = Image.open(images_path)
    im2 = im1.filter(ImageFilter.MedianFilter(size = 3)) 
    img_final = asarray(im2)
    img_op = "/content/drive/MyDrive/ODIR/pathologiques1920-893/clahe/filtred" + name
    #cv2.imwrite(img_op,img_final)
    cv2.imwrite(img_op, cv2.cvtColor(img_final, cv2.COLOR_BGR2RGB))
