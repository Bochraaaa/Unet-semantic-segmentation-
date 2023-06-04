
import os, glob
import skimage.io as io
import PIL
from PIL import Image #pillow fork of the python imaging library
from skimage import io
import cv2

b = 0
for filename in glob.glob("C:/Users/Client/Desktop/gray/veines/*.png"):
    b = b + 1
    a = 1
    img = Image.open(filename)
    w, h = img.size
    print("la valeur de w :",w)
    print ("la valeur de h : ",h)
    x = 0
    while x < h : 
        y = 0
        while y < w :
            imm = img.crop(box=(x, y, x+100, y+100))
            imm.save("imgdrive" +str(b) + "_cropp" +str (a)+".png")
            a = a + 1
            y = y + 50
        x = x + 50



