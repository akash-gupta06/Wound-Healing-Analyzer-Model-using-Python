#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 11:13:31 2024

@author: akash
"""




from matplotlib import pyplot as plt
from skimage import io , restoration
from skimage.filters.rank import entropy
from skimage.morphology import disk
import numpy as np
from skimage.color import rgb2gray

from skimage.filters import threshold_otsu 

import glob

time = 0
time_list = []
area_list = []

path ="/Users/akash/Desktop/Project- woundhealing/*.*"

files = sorted(glob.glob(path))

for file in files:
    img = io.imread(file)

    if img.ndim == 3:
        img = rgb2gray(img)
        
        
    if img.max() <= 1.0:  # Likely a normalized float image
        img = (img * 255).astype('uint8')

    entropy_image = entropy(img , disk(10))
    thresh = threshold_otsu(entropy_image)

    binary = entropy_image <= thresh
    scratch_area = np.sum(binary == True)
    #print(time , scratch_area)
    time_list.append(time)
    area_list.append(scratch_area)
    time += 1
         
print(time_list , area_list)

plt.plot(time_list , area_list , 'bo')

### print slope and intercepts

from scipy.stats import linregress 
slope, intercepts, r_value, p_value, std_err = linregress(time_list , area_list)

print("y= ", slope, "x", "+" , intercepts)
print("R\N{SUPERSCRIPT TWO} = " , r_value**2)




 



























