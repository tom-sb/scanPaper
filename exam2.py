import cv2 as cv
import numpy as np
from fractions import Fraction
from matplotlib import pyplot as plt
from gaussfilter import GaussianFilter

class Image:
        def __init__(self,_image):
                self.image = _image#.astype(int)
                self.original = _image.copy()
                self.row = self.image.shape[0]
                self.col = self.image.shape[1]

        def beGray(self):
                return cv.cvtColor(self.image,cv.COLOR_BGR2GRAY)
        def makeGray(self):
            imageGray = cv.cvtColor(self.image,cv.COLOR_BGR2GRAY)
            return imageGray

        def cannyEdgeDetection(self,kernel=(5,5),sigma=0,minTh=100,maxTh=200):
            #Gaussian blurr
            #Gblurr = cv.GaussianBlur(self.beGray(),kernel,sigma)
            Gblurr = GaussianFilter(self.beGray())
            cv.imwrite('blurr.png',Gblurr)
            Cimg = cv.Canny(self.beGray(),minTh,maxTh)
            return Cimg

        def findcontours(self,edge):
            contours,hierarchy = cv.findContours(edge,cv.RETR_LIST,
                    cv.CHAIN_APPROX_SIMPLE)
            contours = sorted(contours,key=cv.contourArea,reverse=True)

            for c in contours:
                p=cv.arcLength(c,True)
                approx = cv.approxPolyDP(c,0.02*p,True)
                if len(approx)==4:
                    target = approx
                    break
            return target.reshape((4,2))

        def mapper(self,h):
            hnew = np.zeros((4,2),dtype = np.float32)

            add = h.sum(1)
            hnew[0] = h[np.argmin(add)]
            hnew[2] = h[np.argmax(add)]

            diff = np.diff(h,axis = 1)
            hnew[1] = h[np.argmin(diff)]
            hnew[3] = h[np.argmax(diff)]
            return hnew
        def distance(self, pt1, pt2):
            d=0
            for i in range(len(pt1)):
                d+=pow(pt2[i]-pt1[i],2)

            return np.sqrt(d) 

        def transform(self,approx):
            heigth = int(self.distance(approx[0],approx[1]))
            width = int(self.distance(approx[1],approx[2]))
            pts=np.float32([[0,0],[heigth,0],[heigth,width],[0,width]])  
            
            op=cv.getPerspectiveTransform(approx,pts)  
            dst=cv.warpPerspective(self.original,op,(heigth,width))
            return dst

        def makePadding(self, pixBorder):
                self.beGray()
                #newMatrix = [[]for i in range(int(self.row + (pixBorder)))]
                newMatrix = np.zeros((self.row + pixBorder, self.col + pixBorder))
                for i in range(int(pixBorder/2), self.row):
                        for j in range(int(pixBorder/2), self.col):
                                if(i < self.col + (pixBorder/2) or j < self.row + (pixBorder/2)):
                                        newMatrix[i,j] = self.image[i-(int(pixBorder/2)), j-(int(pixBorder/2))]
                return newMatrix
        
        def GaussianFunc(self, x, y):
                sigma = 1
                num = np.exp(-1*((x*x)+(y*y))/(2*(sigma*sigma)))
                den = 2*np.pi*(sigma*sigma)
                print(num/den)
                return num/den

        def makeKernel(self, kernelSize):
                kernelMatrix = [[]for i in range(kernelSize)]
                for i in range(kernelSize):
                        for j in range(kernelSize):
                                kernelMatrix[i].append(self.GaussianFunc(i,j))
                print(kernelMatrix)
                return kernelMatrix

        def convolution(self, kernelSize):
                self.makePadding(kernelSize-1)
                self.makeKernel(kernelSize)

        def beBlur(self):
                self.image = cv.GaussianBlur(self.image, (5,5), 0)
        def makeBlur(self):
                imageBlur = cv.GaussianBlur(self.image, (5,5), 0)
                return imageBlur

        def beCanny(self):
                self.image = cv.Canny(self.image, 75, 100)
        def makeCanny(self):
                imageCanny = cv.Canny(self.image, 75, 100)
                return imageCanny

if __name__ == '__main__':
    img = cv.imread('img1.png')
    #img = cv.resize(img,(1300,800))

    img1 = Image(img)
    canny = img1.cannyEdgeDetection()
    target = img1.findcontours(canny)
    approx = img1.mapper(target)
    print(approx)
    dst = img1.transform(approx)
    plt.imshow(dst)
    plt.show()

