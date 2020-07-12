from matplotlib import pyplot as plt
from tools import formA,knn
import cv2 as cv
import numpy as np
from exam2 import Image

class LineBuilder:
    def __init__(self, line,_x,_y,img1):
        self.line = line
        self.xs = _x 
        self.ys = _y
        self.img1 = img1
        self.eventkey=''
    def connect(self):
        "conectar todos los eventos"
        self.cidpress = self.line.figure.canvas.mpl_connect(
                'button_press_event',self.on_press)
        self.keypress = self.line.figure.canvas.mpl_connect(
                'key_press_event',self.key_press)

    def key_press(self, event):
    
        self.eventkey=event.key
        if self.eventkey == 'enter':
            points = np.column_stack((self.xs,self.ys))
            approx = np.array(points,dtype=np.float32)
            imgfinal = self.img1.transform(approx[:4,:4]);
            self.xs=[]
            self.ys=[]
            self.line.set_data([],[])
            plt.imshow(imgfinal)
            self.line.figure.canvas.draw()

    def on_press(self, event):

        if event.inaxes != self.line.axes: return
        if self.eventkey == 'enter': return
        eventx, eventy = event.xdata, event.ydata
        self.left_button(eventx,eventy)

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

