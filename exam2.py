import cv2 as cv
import numpy as np
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
	
	def makePadding(self, pixBorder = 1, valPix = 0):
		self.beGray()
		newMatrix = [[]for i in range(int(self.row + (pixBorder*2)))]
		for i in range(self.row+(pixBorder*2)):
			for j in range(self.col+(pixBorder*2)):
				if(i == 0 or j == 0):
					newMatrix[i].append(valPix)
				elif(i == self.row+1 or j ==self.col+1):
					newMatrix[i].append(valPix)
				else:
					newMatrix[i].append(self.image[i-1,j-1])
		return newMatrix
	
	def GaussianFunc(self, x, y)
		return 

	def makeKernel(self, kernelSize):
		kernelMatrix = [[]for i in range(kernelSize)]
		for i in range(kernelSize):
			for j in range(kernelSize):
				kernelMatrix[i].append(self.GaussianFunc(i,j))
		return kernelMatrix

	def convolution(self, kernelSize = 3, valPix):
		self.makePadding(kernelSize,valpix)
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
img1.bePadding()
