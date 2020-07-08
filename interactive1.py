from exam2 import Image
from figu import formA, knn
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

class DraggableRectangle:
    lock = None  # only one can be animated at a time
    def __init__(self, scatter,line,_x,_y):
        self.scatter = scatter
        self.line=line
        self.x =_x
        self.y =_y
        self.press = None
        self.background = None

    def connect(self):
        'connect to all the events we need'
        self.cidpress = self.scatter.figure.canvas.mpl_connect(
            'button_press_event', self.on_press)
        self.cidrelease = self.scatter.figure.canvas.mpl_connect(
            'button_release_event', self.on_release)
        self.cidmotion = self.scatter.figure.canvas.mpl_connect(
            'motion_notify_event', self.on_motion)

    def on_press(self, event):
        'on button press we will see if the mouse is over us and store some data'
        if event.inaxes != self.scatter.axes: return

        contains, attrd = self.scatter.contains(event)
        if not contains: return
        #print('event contains', self.rect.xy)
        #x0, y0 = self.rect.xy
        #self.press = x0, y0, event.xdata, event.ydata
        eventx, eventy = event.xdata, event.ydata
        
        pointd = knn(zip(self.x,self.y),(eventx,eventy))
        self.x[pointd[1]] = eventx
        self.y[pointd[1]] = eventy

    def on_motion(self, event):
        'on motion we will move the rect if the mouse is over us'
        if self.press is None: return
        if event.inaxes != self.scatter.axes: return
        #x0, y0, xpress, ypress = self.press
        #dx = event.xdata - xpress
        #dy = event.ydata - ypress
        
        #self.rect.set_x(x0+dx)
        #self.rect.set_y(y0+dy)

        self.scatter = plt.scatter(self.x,self.y,zorder=1)
        self.line = plt.plot(self.x,self.y,zorder=1)

        self.scatter.figure.canvas.draw()

    def on_release(self, event):
        'on release we reset the press data'
        self.press = None
        self.scatter.figure.canvas.draw()

    def disconnect(self):
        'disconnect all the stored connection ids'
        self.scatter.figure.canvas.mpl_disconnect(self.cidpress)
        self.scatter.figure.canvas.mpl_disconnect(self.cidrelease)
        self.scatter.figure.canvas.mpl_disconnect(self.cidmotion)

img = cv.imread("img1.png")
orig = img.copy()
img1=Image(img)
canny = img1.cannyEdgeDetection()
target = img1.findcontours(canny)
approx = img1.mapper(target)

final = img1.transform(approx,orig)
drs = []

xs,ys=formA(np.array(approx))
plt.imshow(img,zorder=0)
scatter = plt.scatter(xs,ys,zorder=1)
line, = plt.plot(xs,ys,zorder=1)
dr = DraggableRectangle(scatter,line,xs,ys)
dr.connect()
drs.append(dr)

plt.show()
