import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from scipy.ndimage.filters import convolve

"""
    img_filt = np.zeros_like(img, dtype=np.float32)
    if len(img.shape)==2:
        return convolution(img,kernel).astype(np.uint8)
    for c in range(3):
        img_filt[:,:,c] = convolution(img[:,:,c],kernel)

    return img_filt.astype(np.uint8)"""

def convolution(oldimg,kernel):
    heigh,width = oldimg.shape[0],oldimg.shape[1]

    kernel_h,kernel_w = kernel.shape[0],kernel.shape[1]

    if len(oldimg.shape)==3:
        img_pad = np.pad(oldimg,pad_width=(
            (kernel_h//2,kernel_h//2),(kernel_w//2,kernel_w//2),
            (0,0)),mode='constant',
            constant_values=0).astype(np.float32)
    if len(oldimg.shape)==2:
        img_pad = np.pad(oldimg,pad_width=(
            (kernel_h//2,kernel_h//2),(kernel_w//2,kernel_w//2)),
            mode='constant',constant_values=0).astype(np.float32)
    h = kernel_h//2
    w = kernel_w//2
    img_conv = np.zeros(img_pad.shape)

    for i in range(h,img_pad.shape[0]-h):
        for j in range(w,img_pad.shape[1]-w):
            x = img_pad[i-h:i-h+kernel_h,j-w:j-w+kernel_w]
            x = x.flatten()*kernel.flatten()
            img_conv[i,j]=x.sum()

    h_end = -h
    w_end = -w
    if h==0:
        return  img_conv[h:,w:w_end]
    if w==0:
        return img_conv[h:h_end,w:]
    return img_conv[h:h_end,w:w_end]

def GaussianFunction(sigma,x,y):
    num = np.exp(-(((x**2) + (y**2))/(2.0*(sigma**2))))
    den = 2.0*np.pi*(sigma**2)
    return num/den


def GaussianFilter(img,kernel_size=5,sigma=1):
    kernel = np.zeros((kernel_size,kernel_size),dtype=np.float32)
    m = n = kernel_size//2

    for x in range(-m,m+1):
        for y in range(-n,n+1):
            kernel[x+2,y+2] = GaussianFunction(sigma,x,y)
    
    return convolve(img,kernel)

if __name__=='__main__':
    img =cv.imread('img1.png',0)
    Gimg = GaussianFilter(img,5,1)
    Gim =cv.GaussianBlur(img,(5,5),1)
    #Cimg = cv.Canny(Gimg,100,200)
    cv.imwrite('gimg.png',Gimg)
    cv.imwrite('Cimg.png',Gim)

