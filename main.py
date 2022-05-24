import glob
from reforme_images import *
from read_XML import *
import doctest
def flatten(PATH) :
    # path = "D:\STAGE\SUPPERPOSE\MS2\_imgraw.tiff"
    path_xml = "D:\STAGE\XML"
    extention =".tiff"
    name = "\MatriceMS1"
    # row = 6
        # columns = 9
    val = cv.CALIB_CB_ADAPTIVE_THRESH + cv.CALIB_CB_FAST_CHECK + cv.CALIB_CB_NORMALIZE_IMAGE + cv.CALIB_CB_FILTER_QUADS
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.00001)                                             #forme le critère de recherche #modification du dernier critère

        #objpoints, imgpoints, images , mtx, dist, rvecs, tvecs =findCorners(path, extention, row, columns, criteria, val)
    pathMS = glob.glob(PATH+'\*',recursive = True)

    for path in pathMS :
        pathMS_part = glob.glob(path+'\*',recursive = True) 
        for pt in pathMS_part : 
            print(pt)
            images = glob.glob(pt+'\*'+ extention,recursive = True)            
            mtx, dist = read_XML(path_xml, name)
            for fname in images:
                reforme_images(fname, PATH, extention, mtx, dist)
            print('flattenned')
        # print("Camera Matrix : ", mtx)
        # print("Distortion Parameters : ", dist)
        # uncomment if findCorners ins used
        # f = open(path +'\Matrices.txt', 'w')
        # f.write(str(dist)+ '\n')
        # f.write(str(mtx)+ '\n')
    # f.close()
        # print("Matrices écrites")

doctest.testmod()