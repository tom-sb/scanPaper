import cv2 as cv 
from gaussfilter import GaussianFilter
from sobelfilter import SobelFilter
from non_max_suppresion import non_max_suppression
from histeresis import hysteresis

def canny(img,kernel=5,sigma=1,lowT=15,highT=21):
    gauss = GaussianFilter(img,kernel,sigma)
    sobel,theta = SobelFilter(gauss)
    nms = non_max_suppression(sobel,theta)
    threshold = hysteresis(nms,lowT,highT)

    return threshold

if __name__=='__main__':
    img = cv.imread('test_img.jpg',0)
    Cimg = canny(img,sigma=23,lowT=15,highT=21)
    caimg = cv.Canny(img,100,200)
    cv.imwrite('canny.png',Cimg)
    cv.imwrite('cannyo.png',caimg)
