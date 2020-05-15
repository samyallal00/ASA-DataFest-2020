# -*- coding: utf-8 -*-

""" Author: Samy ALLAL - samyallal00@ucla.edu """
""" Author: Natsharee Paeng Pulkes - npulkes@ucla.edu """

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import matplotlib

#import tkinter
#matplotlib.use('tkAgg')

fig = 0

"""Samy's work starts here"""

# Read in the data from the worksheet
# NOTE: Change file path to the path of the csv file in your machine
wb = xlrd.open_workbook('work_dataset.xlsx')

sheet = wb.sheet_by_index(0)

# Read the data into a dictionnary of rows
dict_ = {}

for row in range(sheet.nrows):
    if row == 0:
        continue
    dict_[row] = [sheet.cell_value(row, col) for col in range(sheet.ncols) if col != 0]

# Read the labels of each row
cols = []
for row in range(sheet.nrows):
    if row == 0:
        continue
    cols.append(sheet.cell_value(row, 0))

# Set up the overall x-axis (months/year) and the labels common to the dataset
x = range(1, 7)
labels = ['Nov19', 'Dec19', 'Jan20', 'Feb20', 'Mar20', 'Apr20']

lbl = ['White', 'African American', 'Asian', 'Latino']




""" Function's implementations here, all calls to function at end of file"""

# General function to plot a graph
def make_plot(y_axis, title):
    # Determine the figure number and start plotting
    global fig
    plt.figure(fig, figsize=(15, 8))
    fig += 1

    # loop through the y axis data and their corresponding labels, and plot them
    for el, lb in zip(y_axis, lbl):
        y = el
        if y == 0:
            continue
        plt.plot(x, y[7:], label=lb)

    # Display useful information about the graph
    plt.xticks(x, labels)
    plt.xlabel('Time evolution between 2019 and 2020', fontsize=14)
    plt.ylabel('Percentage in %', fontsize=14)
    plt.title(title, fontsize=16)

    plt.legend()
    plt.grid(linewidth=0.25)


# Plot the employement rate graph
def unemploy_rate():
    y = [dict_.get(8), dict_.get(39), dict_.get(70), dict_.get(80)]
    title = 'Unemployement rate among different ethnic groups throughout time'

    make_plot(y, title)



# Plot the employement rate graph
def unemploy_male():
    y = [dict_.get(16), dict_.get(47), 0, dict_.get(88)]
    title = 'Unemployement rate among different ethnic groups throughout time (Male over 20yo)'

    make_plot(y, title)



# Plot the employement rate graph female
def unemploy_female():
    y = [dict_.get(23), dict_.get(54), 0, dict_.get(95)]
    title = 'Unemployement rate among different ethnic groups throughout time (Female over 20yo)'

    make_plot(y, title)

""" Samy's work ends here"""

""" All calls to functions. Description above."""

unemploy_rate()
unemploy_male()
unemploy_female()

"""Show all the graphs """
plt.show()



"""Extra Graphs: Type y if you would like to generate them. Anything else to quit"""

""" Natsharee's work starts here """
# Function to plot a graph with Dec2019 base (right before first COVID case)
# Set up the overall x-axis (months/year) and the labels common to the dataset
labels = ['Dec19', 'Jan20', 'Feb20', 'Mar20', 'Apr20']

lbl = ['White', 'African American', 'Asian', 'Latino']

#Function to draw graph
def make_plot_covidbase(y_axis, title):
  # Determine the figure number and start plotting
  global fig
  plt.figure(fig, figsize=(15, 8))
  fig += 1

  x = range(1, 6)
  # loop through the y axis data and their corresponding labels, and plot them
  for el, lb in zip(y_axis, lbl):
      y = el
      if y == 0:
        continue
      plt.plot(x, y, label=lb)
      #plt.annotate(y, xy=(x,y))

  # Display useful information about the graph
  plt.xticks(x, labels)
  plt.xlabel('Time evolution between Dec 2019 and April 2020', fontsize=14)
  plt.ylabel('Percentage in %', fontsize=14)
  plt.title(title, fontsize=16)


  plt.legend()
  plt.grid(linewidth=0.25)
  
  
  
# Plot the employement rate graph for different ethnicities compared to Dec 2019
def unemploy_rate_covidbase(w,aa,a,la): #added the inputs to play with different data. Can remove.
  y = [dict_.get(w), dict_.get(aa), dict_.get(a), dict_.get(la)]
  title = '% Change in unemployement rate for different ethnic groups compared to Dec 2019'
  
  covidbase_y = []
  for l in y:
        newl = [((x - l[-5]) / l[-5])*100 for x in l]
        covidbase_y.append(newl[-5:])

  make_plot_covidbase(covidbase_y, title)
  
  
  
# Plot the employement % change graph compared to Dec 2019
def lost_employ_covidbase():
  y = [dict_.get(5), dict_.get(36), dict_.get(67), dict_.get(77)]
  title = '% Change in Employed for different ethnic groups Compared to Dec 2019'
  
  covidbase_y = []
  for l in y:
        newl = [((x - l[-5])/ l[-5])*100 for x in l]
        covidbase_y.append(newl[-5:])

  make_plot_covidbase(covidbase_y, title)
  
  """Natsharee's work ends here """

try:
    x = 'q'
    x = input("Type y to continue. Or anything else to exit.\n")
    if(x != 'y'):
        exit(0)
    
except SyntaxError:
    pass



""" Calls to extra graphs"""

unemploy_rate_covidbase(8,39,70,80)
lost_employ_covidbase()


plt.show()
