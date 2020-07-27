# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 12:48:34 2020

@author: Abdullah
"""

from PIL import Image, ImageFilter

img = Image.open('Brandon.jpg')

img


# To perform a gaussian blur uncomment the following line
# Gblur = img.filter(ImageFilter.GaussianBlur)


# To perform a box blur uncomment the follwoing line
# Bblur = img.filter(ImageFilter.BoxBlur(radius = 3))

# To perform an unsharp mask, uncomment the following line
# USmask = img.filter(ImageFilter.UnsharpMask(radius = 5, percent = 150, threshold = 3))

# To filter the image through a kernel, uncomment the following line
# A sample filterr is implemented as under
# Kmask = img.filter(ImageFilter.Kernel(size = (3,3), kernel = (-1,-1,-1,-1,8,-1,-1,-1,-1), scale = 3, offset = 0))

# To pass a mode filter uncomment the following line
# Mmask = img.filter(ImageFilter.ModeFilter(size = 2))