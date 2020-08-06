# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 14:29:46 2020

@author: Abdullah
"""

import cv2
import glob
import matplotlib.pyplot as plt

train_img_dir = "Path to folder"
files1 = glob.glob(train_img_dir + '*.*')

image = cv2.imread(files1[2])
gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hessianThreshold = 1000
surf = cv2.xfeatures2d.SURF_create(hessianThreshold)
keypoints, descriptors = surf.detectAndCompute(gray,None)
img = cv2.drawKeypoints(image, keypoints, None, (255,255,0), 4)
plt.imshow(img)