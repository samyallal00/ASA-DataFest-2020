# -*- coding: utf-8 -*-

""" Author: Samy ALLAL - samyallal00@ucla.edu """

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

#import tkinter
#matplotlib.use('tkAgg')

# Upload the Data set here, and load the data
# NOTE: Change file path to the path of the csv file in your machine
bad_data = ['', '?']
data = pd.read_csv('personal.csv', na_values=bad_data)

# the data info is for reference, helps know the different features we have
print(data.info())

# Rename the columns to make it easier to use
data = data.rename(columns=({'What is the best age group that you identify with?': 'age'}))
data = data.rename(columns=({'Tell us about your status? Reminder: Survey is anonymous': 'status'}))
data = data.rename(columns=({'Have you been affected by Covid-19?': 'affected'}))
data = data.rename(columns=({
    'In a scale from 1 (being lowest, horrible) to 10 (being the highest, fantastic), how would you rate your personal well being 5 months ago (before the outbreak)?': 'being_before'}))
data = data.rename(columns=({
    'In a scale from 1 (being lowest, horrible) to 10 (being the highest, fantastic), how would you rate your personal well being now ?': 'being_now'}))
data = data.rename(columns=({
    'In a scale from 1 (being lowest, horrible) to 10 (being the highest, fantastic), how would you predict your personal well being 5 months from now?': 'being_future'}))
data = data.rename(columns=({
    'If you are currently experiencing high level of stress due to the pandemic, what would you say is the biggest factor causing your stress?': 'factor'}))

# Keep only relevant columns for our analysis
cols = ['age', 'status', 'affected', 'being_before', 'being_now', 'being_future', 'factor']

new_data = data[cols]
data = new_data

# the data info is for reference, helps know the different features we have
print(data.info())


# Display age of individuals
def age_in():
    # main data for the age repartition
    teen = data[data['age'] == '17-21']
    young = data[data['age'] == '22-27']
    mid = data[data['age'] == '28-35']
    mid2 = data[data['age'] == '35-50']
    old = data[data['age'] == '51 +']

    # set up the x and y axis accordingly
    x = range(1, 6)
    y = [len(teen), len(young), len(mid), len(mid2), len(old)]

    total = sum(y)
    # and plot
    plt.figure(0)
    plt.xticks(x, ['Age: 17-21', 'Age: 22-27', 'Age: 28-35', 'Age: 36-50', 'Age: 51+'])

    # display the value of each bar
    for index, value in enumerate(y):
        plt.text(index + 0.7, value + 2, str(round(value / total * 100, 2)) + '%', fontsize=12)

    # Highlight the max value in the graph
    color_ = []
    for val in y:
        if val == max(y):
            color_.append('orange')
        else:
            color_.append('blue')

    plt.ylim(top=100)

    # display useful information about graph
    plt.grid(linewidth=0.25)
    plt.xlabel('Age groups', fontsize=12)
    plt.ylabel('Number of individuals', fontsize=12)
    plt.title('Age repartition of participants', fontsize=13)
    plt.bar(x, y, color=color_)



# Display professional status of individuals
def status_in():
    # useful variables (efficiency and readability)
    student = len(data[data['status'] == 'Student'])
    employee = len(data[data['status'] == 'Worker'])
    retired = len(data[data['status'] == 'Retired'])
    lost = len(data[data['status'] == 'Lost job'])
    frontline = len(data[data['status'] == 'Frontline worker'])

    # set up the x and y axis accordingly
    x = range(1, 6)
    y = [student, employee, retired, lost, frontline]

    total = sum(y)
    # and throw everything at plt to plot
    plt.figure(1)
    plt.xticks(x, ['Student', 'Worker', 'Retired', 'Lost job', 'Frontline worker'])

    # display the value of each bar
    for index, value in enumerate(y):
        plt.text(index + 0.7, value + 2, str(round(value / total * 100, 2)) + '%', fontsize=12)

    # Highlight the max value in the graph
    color_ = []
    for val in y:
        if val == max(y):
            color_.append('orange')
        else:
            color_.append('green')

    plt.ylim(top=122)
    plt.xlabel('Professional status')
    plt.ylabel('Number of individuals')
    plt.title('Professional status of participants')

    plt.grid(linewidth=0.25)
    plt.bar(x, y, color=color_)


# Display the percentage of the population affected
def affected():
    # Main data
    at_risk = data[data['affected'] == 'Yes']
    no_risk = data[data['affected'] == 'No']

    # Labels and percentages
    x = [len(at_risk), len(no_risk)]
    labels_ = ['Affected', 'Not affected']
    explode_ = [0.1, 0]

    # Plot
    plt.figure(2)
    plt.title('Percentage of population affected by COVID-19')
    plt.pie(x, labels=labels_, autopct='%1.1f%%', explode=explode_, shadow=True, startangle=45)



# Comparison between the participants' well-being before, now and after
def well_being():
    # Main data, y-axis for the three different times
    list_bef = new_data.groupby('age')['being_before'].mean().tolist()
    list_now = new_data.groupby('age')['being_now'].mean().tolist()
    list_aft = teen_bef = new_data.groupby('age')['being_future'].mean().tolist()

    # set up the x-axis, labels
    x = range(1, 6)

    # Plot everything
    plt.figure(3, figsize=(10, 8))
    plt.xticks(x, ['17 to 21', '22 to 27', '28 to 35', '36 to 50', '51 and above'])

    plt.ylim(top=11)

    # Three bars for three times before, now and after
    plt.bar([a - 0.25 for a in x], list_bef, label='Before (5 months ago)', width=-0.25)
    plt.bar([a for a in x], list_now, label='Now', width=0.25)
    plt.bar([a + 0.25 for a in x], list_aft, label='After 5 months ~ prediction', width=0.25)

    # Display the numbers for each bar
    for index, value in enumerate(list_bef):
        plt.text(index + 0.65, value + 0.2, str(round(value, 2)), fontsize=11)

    for index, value in enumerate(list_now):
        plt.text(index + 0.9, value + 0.2, str(round(value, 2)), fontsize=11)

    for index, value in enumerate(list_aft):
        plt.text(index + 1.15, value + 0.2, str(round(value, 2)), fontsize=11)

    # Display some useful information
    plt.grid(linewidth=0.25)
    plt.legend(fontsize=14)
    plt.xlabel('Age', fontsize=16)
    plt.ylabel('Personal well being estimation (scale 10)', fontsize=14)
    plt.title('Personal well being throughout time', fontsize=14)



# Display the common factors
def stress_factors():
    # Rename the data inside the factor column for ease of use
    dict_replace = {'Social distancing and staying at home for a long period of time.': 'Social Distancing',
                    'The virus itself.': 'The virus', 'Remote work/ Remote education.': 'Remote work, Remote Learning',
                    'Watching the news and daily statistics about the ongoing situation.': 'News, daily statistics',
                    'Financial insecurity.': 'Financial insecurity'}

    data['factor'] = data['factor'].replace(dict_replace)

    # Set up the data (main data)
    social = data[data['factor'] == 'Social Distancing']
    virus = data[data['factor'] == 'The virus']
    remote = data[data['factor'] == 'Remote work, Remote Learning']
    news = data[data['factor'] == 'News, daily statistics']
    finance = data[data['factor'] == 'Financial insecurity']

    # set up the x and y axis
    x = range(1, 6)
    y = [len(virus), len(news), len(finance), len(remote), len(social)]

    total = sum(y)
    # Plot
    plt.figure(4)

    # Highlights the max value with a specific color
    color_ = []
    for val in y:
        if val == max(y):
            color_.append('orange')
        else:
            color_.append('blue')

    # Display the numbers for each bar
    for index, value in enumerate(y):
        plt.text(value + 1, index + 1, str(round(value / total * 100, 2)) + '%', fontsize=11)

    # Add some useful information about the graph
    plt.yticks(x, ['The virus itself', 'News, daily statistics', 'Financial insecurity', 'Remote work, Remote Learning',
                   'Social distancing, Stay-Home'])
    plt.xlim(right=50)
    plt.grid(linewidth=0.25)

    plt.title('Most common factors causing stress')
    plt.xlabel('Number of participants')
    plt.barh(x, y, color=color_)



"""All function calls. Description above."""
age_in()
status_in()
affected()
well_being()
stress_factors()

"""Show everything"""
plt.show()
