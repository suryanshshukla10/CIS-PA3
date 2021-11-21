# The first task is to the the input of the data file

import matplotlib.pyplot as plt
import numpy as np
from numpy.lib.polynomial import polyfit
path = '/Users/suryanshshukla/Desktop/PA3/CIS-PA3/2021 PA 3-5 Student Data/'
a = np.loadtxt(
    path+'PA3-A-Debug-Answer.txt', skiprows=1)

body = np.loadtxt(path+'Problem3-BodyA.txt', skiprows=1)

file1 = np.loadtxt(path+'Problem3-BodyA.txt', skiprows=1)
file2 = np.loadtxt(path+'Problem3-BodyB.txt', skiprows=1)
# file3 = np.loadtxt(path+'Problem3MeshFile.sur')
