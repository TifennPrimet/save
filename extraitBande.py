from concurrent.futures.process import _ExceptionWithTraceback
from re import I
from tkinter import HORIZONTAL
import cv2 as cv
import numpy as np
# Files that read the information of 3 wavelength images and combine them in a false color image
# By default OpenCV use the BGR format ( red is the less important information)

path = "D:\STAGE\SUPPERPOSE\MS2_flat"      # path to all the images 
filename = '\_1.png'
image = cv.imread( path +  filename)
#image = cv.cvtColor(image, cv.COLOR_GRAY2RGB)

channel_1 = np.zeros((image.shape[0], image.shape[1],3)) # The new image null by default

cv.waitKey(0)
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        for k in range(3):
            channel_1[i,j][k] = image[i,j][0]
cv.imshow('image', channel_1)
cv.imwrite(path+"\_uneBande.png",255*channel_1/np.max(channel_1))