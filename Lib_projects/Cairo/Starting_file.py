# -*- coding: utf-8 -*-
"""
@author: Abdullah
@Email: abdullah.khan230@yahoo.com
@Github: https://github.com/Abdullah230
Created on Sun Jul 19 06:34:30 2020
"""
import math
import cairo


WIDTH, HEIGHT = 256, 256

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

# This scale is independent of the suface
# It scales the canvas we are drawing on, not the output pixels of the image
ctx.scale(256, 256)  # Normalizing the canvas

# This adds a Linear gradient
# The linear gradient slowly vanishes uptil the second stop appears
# It is necessary to add a second stop
pat = cairo.LinearGradient(1.0, 0.0, 1.0, 1.0)
pat.add_color_stop_rgba(1, 0, 0, 0, 0)  # First stop, 50% opacity
pat.add_color_stop_rgba(0, 0.9, 0.7, 0.2, 1)  # Last stop, 100% opacity


ctx.rectangle(0, 0, 1, 1)  # Rectangle(x0, y0, x1, y1)
ctx.set_source(pat)
ctx.fill()

ctx.translate(0.1, 0.1)  # Changing the current transformation matrix

ctx.move_to(0, 0)
# Arc(cx, cy, radius, start_angle, stop_angle)
# A line will always connect starting point (0,0) (Defined by move) to the start of arc
ctx.arc(0.1, 0.1, 0.1, -math.pi/2, 0)
ctx.line_to(0.4, 0.1)  # Line to (x,y)
# Curve(x1, y1, x2, y2, x3, y3)
ctx.curve_to(0.5, 0.2, 0.5, 0.4, 0.4, 0.8)
ctx.close_path()

ctx.set_source_rgb(0.3, 0.2, 0.5)  # Solid color
ctx.set_line_width(0.02)
ctx.stroke()

surface.write_to_png("example.png")  # Output to PNG