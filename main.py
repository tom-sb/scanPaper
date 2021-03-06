from matplotlib import pyplot as plt
from tools import formA, knn
import cv2 as cv
import numpy as np
from exam2 import Image
from line import LineBuilder

def main():
    #img = cv.imread('test_img.jpg')
    #img = cv.imread('fot1.jpg')
    img = cv.imread('fot2.jpg')
    scanner = Image(img)
    #canny = scanner.cannyEdgeDetection()
    canny = scanner.cannyEdgeDetection(sigma=15,)
    plt.imshow(canny)
    plt.show()
    target = scanner.findpoints(canny)
    points = scanner.mapper(target)

    xs, ys = formA(np.array(points))
    plt.imshow(img)
    line, = plt.plot(xs,ys,'.-')
    plt.axis('off')
    cv.imwrite('cannyimg.png',canny)
    interactive = LineBuilder(line,xs,ys,scanner)
    interactive.connect()
    
    plt.show()


main()



