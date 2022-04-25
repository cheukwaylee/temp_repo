# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 12:01:01 2022

@author: CW
"""

import os
from glob import glob
 
from PIL import Image
import numpy as np
    

filename = "C:\\Users\\CW\\Desktop\\thesis_ws\\Snipaste_2022-04-22_12-06-05"
img = Image.open(filename+".png")
img = img.convert('RGBA')
pixdata = img.load()
pixdata_ = pixdata

for y in range(img.size[1]):
    for x in range(img.size[0]):
        if all(pixdata[x, y][i] > 240 for i in range(4)):
            #pixdata[x, y] = 255, 255, 255, 0
            pixdata_[x, y] = 0, 255, 255, 255
        else:
            pixdata_[x, y] = pixdata[x, y]

img.save(filename+"_post.png")