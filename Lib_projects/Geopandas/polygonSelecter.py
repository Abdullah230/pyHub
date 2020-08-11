# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 06:33:40 2020

@author: Abdullah
"""

import geopandas as gpd
import pandas as pd
import numpy as np
from shapely.geometry import Polygon
from shapely.geometry import LineString
from shapely.geometry import Point
import matplotlib.pyplot as plt

###########################################################################

#Developers notes:
# Installing geopandas depreciates pyproj to 1.9, because of that the transform property 
# might not be available to the user in the same environemnt. The user might be using them
# to make transformations so that the coordinate systems might match. This transformation 
# should be done before installing geopanas and running the provided function

###########################################################################

def findIntersects(shapeFilePath, transmitterPointsFilePath, receiverPointsFilePath):
    gdf = gpd.read_file(shapeFilePath)
    gdf = gpd.GeoDataFrame(gdf['geometry'])

    temp = gdf[~gdf.is_valid]
    gdf = gdf[gdf.is_valid]
    temp = temp.buffer(0)
    temp = gpd.GeoDataFrame(temp, columns = ['geometry'])
    gdf = gdf.append(temp, ignore_index = True)
    gdf = gdf[~gdf.is_empty]

    begin = pd.read_csv(transmitterPointsFilePath)
    begin = begin[begin.columns[1:3]] # Getting the X and Y 
    bdf = pd.read_csv(receiverPointsFilePath)
    bdf = bdf[bdf.columns[1:3]] #again getting X and Y
    central = Point((begin.iloc[0]['Longitude'], begin.iloc[0]['Latitude']))
    lines = []
    for i in range(len(bdf)):
        pp = Point((bdf.iloc[i]['X'], bdf.iloc[i]['Y']))
        temp = LineString([(central.x,central.y),(pp.x,pp.y)])
        lines.append(temp)


    lines = gpd.GeoDataFrame(lines, columns = ['geometry'], crs = {'init':'epsg:4326'})
    minx = bdf['X'].min() - 0.001
    maxx = bdf['X'].max() + 0.001
    miny = bdf['Y'].min() - 0.001
    maxy = bdf['Y'].max() + 0.001
    maskP = Polygon([[minx, miny], [maxx, miny], [maxx, maxy], [minx, maxy], [minx, miny]])
    tgdf = gpd.GeoDataFrame([maskP], columns = ['geometry'], crs={'init': 'epsg:4326'})
    fgdf = gpd.overlay(gdf, tgdf, how='intersection')

    count = []
    for i in range(len(lines)):
        test = fgdf.intersects(lines.iloc[i][0])
        count.append(len(fgdf[test]))
        
    count = [j-1 for j in count]
    return count