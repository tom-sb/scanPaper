from matplotlib import pyplot as plt
from figu import formA,knn
import cv2 as cv
import numpy as np
from exam2 import Image

class LineBuilder:
    def __init__(self, line,_x,_y):
        self.line = line
        self.xs =x #list(line.get_xdata())
        self.ys =y #list(line.get_ydata())
        self.cid = line.figure.canvas.mpl_connect('button_press_event', self)

    def __call__(self, event):
        print('click', event)
        if event.inaxes!=self.line.axes: return
        eventx,eventy =event.xdata,event.ydata
        # KNN para los vecinos cercanos
        kv = knn(zip(self.xs,self.ys),(eventx,eventy))
        if(kv[1] == 0):
            self.xs[4] = eventx
            self.ys[4] = eventy
        self.xs[kv[1]] = eventx
        self.ys[kv[1]] = eventy
        
        self.line.set_data(self.xs, self.ys)
        self.line.figure.canvas.draw()

img = cv.imread('img1.png')
orig = img.copy()
img1 = Image(img)
canny = img1.cannyEdgeDetection()
target = img1.findcontours(canny)
approx = img1.mapper(target)
final = img1.transform(apprapprox,origg)

#fig = plt.figure()
#ax = fig.add_subplot(111)
#ax.set_title('click to build line segments')
#x = [0,0,1,1,0]
#y = [0,1,1,0,0]

#line, = ax.plot(x, y,'.-')  # empty line
x,y = formA(np.array(approx))
plt.imshow(img,zorder=0)
line, = plt.plot(x,y,'.-')

linebuilder = LineBuilder(line,x,y)

plt.show()
