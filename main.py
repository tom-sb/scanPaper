from matplotlib import pyplot as plt
from tools import formA, knn
import cv2 as cv
import numpy as np
from exam2 import Image
from line import LineBuilder

def main():
    img = cv.imread('img1.png')
    
    scanner = Image(img)
    canny = scanner.cannyEdgeDetection()
    target = scanner.findcontours(canny)
    points = scanner.mapper(target)

    xs, ys = formA(np.array(points))
    plt.imshow(img)
    line, = plt.plot(xs,ys,'.-')
    plt.axis('off')

    interactive = LineBuilder(line,xs,ys,scanner)
    interactive.connect()
    
    plt.show()


main()



