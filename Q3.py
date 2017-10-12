# Q3 from tutorial 7 assignment 
#Authors: Janice Love and Melissa Stephens
#Date: October 11, 2017 

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

#read in data
data = pd.read_csv("data.txt", sep = ",", header = 0)

inFile = open("data.txt", sep = ",")

#create lists storing observations of each region 
north = 0
south = 0
east = 0
west = 0 

#for loop to count number of observations for each region 
for i in range(0,len(data),1):
    if data.region[i] == "north":
        north = north + 1
    elif data.region[i] == "south":
        south = south + 1
    elif data.region[i] == "west":
        west = west + 1
    elif data.region[i] == "east":
        east = east + 1

north_sum = 0
south_sum = 0
east_sum = 0
west_sum = 0 
        
#for loop to calculate sum of observations per region 
for i in range(0, len(data),1):
    if data.region[i] == "north":
        north_sum = north_sum + data.observations[i]
    elif data.region[i] == "south":
        south_sum = south_sum + data.observations[i]
    elif data.region[i] == "east":
        east_sum = east_sum + data.observations[i]
    elif data.region[i] == "west": 
        west_sum = west_sum + data.observations[i]

#calculate the average 
north_ave = north_sum / north
south_ave = south_sum / south
east_ave = east_sum / east
west_ave = west_ave / west 



#barplot of the means of the four populations 
objects = ('north', 'south', 'east', 'west')
y_pos = np.arange(len(objects))
averages = [north_ave, south_ave, east_ave, west_ave]


