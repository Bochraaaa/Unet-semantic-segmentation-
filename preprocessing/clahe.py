import cv2 
import os

#CLAHE on One image
 
path = "/content/drive/MyDrive/mémoire/fond d'oeil drive/fond/03.png"
img = cv2.imread(path) 
#clahe
clahe = cv2.createCLAHE(clipLimit=3., tileGridSize=(1,1))
#print(img)
#lab = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)  # convert from BGR to LAB color space
#img2 = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
l, a, b = cv2.split(lab)  # split on 3 different channels
l2 = clahe.apply(l)  # apply CLAHE to the L-channel
lab = cv2.merge((l2,a,b))  # merge channels
img2 = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)  # convert from LAB to BGR
#fig, ax = plt.subplots()
#ax.imshow(img2, cmap=plt.cm.gray)
cv2.imwrite("/content/drive/MyDrive/01clahe.png",img2)
#CLAHE loop
path = "/content/drive/MyDrive/ODIR/pathologiques1920-893/patho/"
files = os.listdir(path)
for name in files:
    images_path = path + name
    print(images_path)
    img = cv2.imread(images_path)
    clahe = cv2.createCLAHE(clipLimit=3., tileGridSize=(1,1))
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)  # convert from BGR to LAB color space
    l, a, b = cv2.split(lab)  # split on 3 different channels
    l2 = clahe.apply(l)  # apply CLAHE to the L-channel
    lab = cv2.merge((l2,a,b))  # merge channels
    img2 = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)  # convert from LAB to BGR
    cv2.imwrite('/content/drive/MyDrive/ODIR/pathologiques1920-893/clahe/clahe3-1 '+ name,img2)
