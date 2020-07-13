import cv2 as cv
import numpy as np
from scipy.ndimage.filters import convolve
from gaussfilter import GaussianFilter

#img en scala grises
def SobelFilter(img):
    Gx = np.array([[1,0,-1],[2,0,-2],[1,0,-1]], np.float32)
    Gy = np.array([[1,2,1],[0,0,0],[-1,-2,-1]], np.float32)
    
    G_x = convolve(img,Gx)
    G_y = convolve(img,Gy)
    
    #G = np.sqrt(np.power(G_x,2) + np.power(G_y,2))
    G = np.hypot(G_x,G_y)

    G = G/G.max()*255
    Theta = np.arctan2(G_y,G_x) * 180 /np.pi
    return G , Theta


if __name__=='__main__':
    img = cv.imread('img1.png',0)
    Gaussimg = GaussianFilter(img,5,1)
    Gimg, Theta = SobelFilter(Gaussimg)

    cv.imwrite('Gradiente.png',Gimg.astype(np.uint8))
    cv.imwrite('Theta.png',Theta.astype(np.uint8))
