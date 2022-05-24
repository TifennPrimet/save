import zipfile
import glob 
import os
def unzip(folder ) :
    
    FILES = glob.glob(folder +'\*' + '.zip')
    print(folder)
    for file in FILES :
        with zipfile.ZipFile(file,"r") as zip_ref:
            if not os.path.exists(folder + '_unziped'):
                os.makedirs(folder + '_unziped')
            print(file)
            zip_ref.extractall(folder + '_unziped' +file[len(folder):-4])
    print("extracted")


