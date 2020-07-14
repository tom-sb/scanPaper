import numpy as np
import cv2 as cv
from gaussfilter import GaussianFilter
from sobelfilter import SobelFilter
from non_max_suppresion import non_max_suppression

def threshold(img,lowT=0.05,highT=0.15,weakP=75,strongP=255):
    M,N = img.shape

    Thres = np.zeros((M,N),dtype=np.uint8)

    strongI,strongJ = np.where(img >= highT)
    zerosI,zerosJ = np.where(img < lowT)

    weakI,weakJ = np.where((img<=highT) & (img >= lowT))

    Thres[strongI,strongJ] = strongP
    Thres[zerosI,zerosJ] = 0
    Thres[weakI,weakJ] = weakP

    return Thres

def hysteresis(img,lowT=0.05,highT=0.15,weakP=75,strongP=255):
    M,N = img.shape

    thres = threshold(img,lowT,highT,weakP,strongP)

    for i in range(1,M-1):
        for j in range(1,N-1):
            if thres[i,j] == weakP:
                if strongP in [thres[i+1, j-1],
                        thres[i+1, j],thres[i+1, j+1],
                        thres[i, j-1],thres[i, j+1],
                        thres[i-1, j-1],thres[i-1, j],
                        thres[i-1, j+1]]:
                    thres[i,j] = 255
                else:
                    thres[i,j] = 0
    return thres

if __name__=='__main__':
    img = cv.imread('img1.png',0)
    gauss = GaussianFilter(img,5,10)
    sobel,Theta = SobelFilter(gauss)

    nms = non_max_suppression(sobel,Theta)
    
    threshold = hysteresis(nms,lowT=15,highT=21)

    cv.imwrite('hysteresis.png',threshold.astype(np.uint8))
