import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import numpy as np

def formA(points):
    verts = [
            (points[0][0], points[0][1]),   # P0
            (points[1][0], points[1][1]),  # P1
            (points[2][0], points[2][1]),  # P2
            (points[3][0], points[3][1]),  # P3
            (points[0][0], points[0][1]),
            ]
    xs, ys = zip(*verts)

    return np.array(xs),np.array(ys)

def distance(pt1,pt2):
    suma=0
    for i in range(2):
        suma+=pow(pt2[i]-pt1[i],2)

    return np.sqrt(suma)

def take_second(elem):
    return elem[1]

def knn(puntos,punto):
    vdis = []
    c = 0
    for p in puntos:
        vdis.append((distance(p,punto),c))
        c+=1
    vdis.sort()
    return vdis[0]
