from unzip import *
from main import * 
PATH_images = "D:\STAGE\MS"
FOLDERS = glob.glob(PATH_images +'\*',recursive = True) 
for folder in FOLDERS : 
    unzip(folder)
    flatten(PATH_images)

PATH_MS1 = "D:\STAGE\MS\MS1"
PATH_MS2 = "D:\STAGE\MS\MS2"