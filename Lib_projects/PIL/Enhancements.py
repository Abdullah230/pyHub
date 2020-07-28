# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 12:15:55 2020

@author: Abdullah
"""

from PIL import Image, ImageEnhance

img = Image.open('Brandon.jpg')

# To enhance the image sharpness, color , contrast or brightness, un comment the following lines
#enh = ImageEnhance.Sharpness(img)
#enh = ImageEnhance.Color(img)
#enh = ImageEnhance.Contrast(img)
#enh = ImageEnhance.Brightness(img)
factor = 2
enh.enhance(factor)

