import cv2 as cv
import numpy as np
from fractions import Fraction
from matplotlib import pyplot as plt

class Image:
	def __init__(self,_image):
		self.image = _image#.astype(int)
		self.row = self.image.shape[0]
		self.col = self.image.shape[1]

	def beGray(self):
		self.image = cv.cvtColor(self.image,cv.COLOR_BGR2GRAY)
	def makeGray(self):
		imageGray = cv.cvtColor(self.image,cv.COLOR_BGR2GRAY)
		return imageGray
	
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
	
img = cv.imread('img1.png')


img1 = Image(img)
img1.convolution(5)
