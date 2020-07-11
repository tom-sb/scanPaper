from matplotlib import pyplot as plt
from figu import formA,knn
import cv2 as cv
import numpy as np
from exam2 import Image

class LineBuilder:
    def __init__(self, line,_x,_y,img1):
        self.line = line
        self.xs = x 
        self.ys = y
        self.img1 = img1
    def connect(self):
        "conectar todos los eventos"
        self.cidpress = self.line.figure.canvas.mpl_connect(
                'button_press_event',self.on_press)
    
    def on_press(self, event):

        if event.inaxes != self.line.axes: return
        eventx, eventy = event.xdata, event.ydata
        if event.button == 1:
            self.left_button(eventx,eventy)
        else:
            approx = np.column_stack((self.xs,self.ys))
            approx = np.array(approx,dtype=np.float32)
            imgfinal = self.img1.transform(approx[:4,:4]);
            plt.imshow(imgfinal)
            #self.disconnect()

    def left_button(self,eventx,eventy):
        #vecino cercano a el evento
        kv = knn(zip(self.xs,self.ys),(eventx,eventy))

        if kv[1] == 0:
            self.xs[4] = eventx
            self.ys[4] = eventy
        self.xs[kv[1]] = eventx
        self.ys[kv[1]] = eventy

        self.line.set_data(self.xs, self.ys)
        self.line.figure.canvas.draw()

    def disconnect(self):
        self.line.figure.canvas.mpl_disconnect(self.cidpress)

img = cv.imread('img1.png')
orig = img.copy()
img1 = Image(img)
canny = img1.cannyEdgeDetection()
target = img1.findcontours(canny)
approx = img1.mapper(target)

x,y = formA(np.array(approx))
plt.imshow(img,zorder=0)
line, = plt.plot(x,y,'.-')

linebuilder = LineBuilder(line,x,y,img1)
linebuilder.connect()

plt.show()

