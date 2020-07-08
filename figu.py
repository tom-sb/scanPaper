import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import numpy as np

def formA(points):
    verts = [
            (points[0,0], points[0,1]),   # P0
            (points[1,0], points[1,1]),  # P1
            (points[2,0], points[2,1]),  # P2
            (points[3,0], points[3,1]),  # P3
            (points[0,0], points[0,1]),
            ]
    xs, ys = zip(*verts)

    return xs,ys
