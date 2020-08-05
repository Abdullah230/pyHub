# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 12:46:33 2020

@author: Abdullah
"""

import cv2
import glob
import matplotlib.pyplot as plt

train_img_dir = "imagePath"
files1 = glob.glob(train_img_dir + '*.jpg')

img = cv2.imread(files1[0])
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sift = cv2.xfeatures2d.SIFT_create()
keypoints, descriptors = sift.detectAndCompute(gray,None)
img=cv2.drawKeypoints(gray,keypoints,img,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
plt.imshow(img)