from matplotlib import pyplot as plt

import constants
import similarities
from Centroid import Centroid
from Point import Point
import numpy as np

from pltUtils import config_plt
from randomGenerators import  generate_random_number_of_centroids, colors, yPoints, xPoints

points = []

with open('data.txt') as f:
    lines = f.readlines()
    for line in lines:
        words = line.split()
        points.append(Point(float(words[0]), float(words[1])))
    if len(colors) == 0:
        colors = list(map(lambda l: constants.zones[int(l.split()[2])][2], lines))
if len(xPoints) == 0:
    xPoints = list(map(lambda p: p.x, points))
    yPoints = list(map(lambda p: p.y, points))