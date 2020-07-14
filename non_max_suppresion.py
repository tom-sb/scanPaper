import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from gaussfilter import GaussianFilter
from sobelfilter import SobelFilter


def non_max_suppression(img,Angle):
    H, W = img.shape
    Z = np.zeros((H,W),dtype=np.int32)

    for i in range(1,H-1):
        for j in range(1,W-1):
            #angulo 0
            p=255
            q=255
            if (0<=Angle[i,j]<22.5) or (157.5<=Angle[i,j]<=180) or (
                    -22.5<=Angle[i,j]<0) or (-180<=Angle[i,j]<-157.5):
                p = img[i,j+1]
                q = img[i,j-1]
            #angulo 45
            elif (22.5 <= Angle[i,j]<67.5) or (-157.5<=Angle[i,j]<-112.5):
                p = img[i+1,j+1]
                q = img[i-1,j-1]
            #angulo 90
            elif (67.5<=Angle[i,j]<112.5) or (-112.5<=Angle[i,j]<-67.5):
                p = img[i+1,j]
                q = img[i-1,j]
            #angulo 135
            elif (112.5 <= Angle[i,j]<157.5)  or (-67.5<=Angle[i,j]<-22.5):
                p = img[i+1,j-1]
                q = img[i-1,j+1]

            #non max suppression
            if (img[i,j] >= p) and (img[i,j]>=q):
                Z[i,j] = img[i,j]
            else:
                Z[i,j] = 0
    return Z

if __name__=='__main__':
    img = cv.imread('img1.png',0)
    Gaussimg = GaussianFilter(img,5,15)
    Gimg , Theta = SobelFilter(Gaussimg)

    NMSimg = non_max_suppression(Gimg,Theta)
    cv.imwrite('nonmax.png',NMSimg.astype(np.uint8))

