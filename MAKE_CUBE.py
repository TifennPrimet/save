"""  crée le cube d'image et écrit le fichier Tiff """

import numpy as np
import libtiff as tiff
import cv2 as cv

path = "D:\STAGE\MS"
CUBE = np.zeros((320, 385, 18))
for ms in ('\MS1', '\MS2') : 
    pathcam = path + ms
    for channel in range(9):
        img = cv.imread(pathcam + '\_20220519_134340_657_imgraw.tiff\imgChannel_' + str(channel) + '.tiff')
        if ms == '\MS1' : 
            newImg = img[:-8,32:]
        else : 
            newImg = img[8:,:-32]
        for i in range(CUBE.shape[0]):
                for j in range(CUBE.shape[1]): 
                            if ms == '\MS1' : 
                                CUBE[i,j][channel] = newImg[i,j][0]
                            else : 
                                CUBE[i,j][8+channel] = newImg[i,j][0]
print(CUBE)
print("max CUBE", np.max(CUBE))
cv.imwrite(pathcam +'CUBE.bmp', CUBE)



