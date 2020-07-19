# -*- coding: utf-8 -*-
"""
@author: Abdullah
@Email: abdullah.khan230@yahoo.com
@Github: https://github.com/Abdullah230
Created on Sun Jul 19 06:34:30 2020
"""
import math
import cairocffi as cairo


surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1000, 1000)
context = cairo.Context(surface)
with context:
    context.set_source_rgb(1, 1, 1)  # White
    context.paint()
# Restore the default source which is black.
context.line_to(90, 140)
context.rotate(1)
context.set_font_size(20)
context.show_text('Hi from cairo!')
surface.write_to_png('example.png')