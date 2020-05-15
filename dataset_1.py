# -*- coding: utf-8 -*-

""" Author: Samy ALLAL - samyallal00@ucla.edu """

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

#import tkinter
#matplotlib.use('tkAgg')

fig = 0

# Upload the Data set here, and load the data
# NOTE: Change file path to the path of the csv file in your machine
bad_data = ['', '?']
data = pd.read_csv('data_1.csv', na_values=bad_data)

# the data info is for reference, helps know the different features we have
print(data.info())

""" Functions' implementations here, all calls to functions at the end of file"""

# Display genders statistics
def gender_in():
    # make a male list and a female list from the data
    male = data[data['BE MALE'] == 1]
    female = data[data['BE MALE'] == 0]
    other = data[data['BE MALE'] == 'NA']

    # set up the x and y axis accordingly
    x = [1, 2, 3]
    y = [len(male), len(female), len(other)]

    total = len(male) + len(female) + len(other)

    # and throw everything at plt to plot
    global fig
    plt.figure(fig)
    fig += 1

    plt.xticks(x, ['Male', 'Female', 'Other'])

    # display the value of each bar
    plt.ylim(top=1800)
    for index, value in enumerate(y):
        plt.text(index + 0.85, value + 35, str(round(value / total * 100, 2)) + "%", fontsize=12)

    # Highlight the max value in the graph
    color_ = []
    for val in y:
        if val == max(y):
            color_.append('orange')
        else:
            color_.append('red')

    # display useful information about the graph
    plt.grid(linewidth=0.25)
    plt.ylabel('Number of individuals')
    plt.title('Gender repartition of participants', fontsize=13)

    plt.bar(x, y, color=color_)



# Display age of individuals
def age_in():
    # get all ages in the dataset, store in ages and make age bins to cut
    data['AGE'] = pd.to_numeric(data['AGE'])
    ages = pd.DataFrame({'age': data['AGE']})
    bin = [9, 19, 29, 39, 49, 59, 69, 79, 89]

    # assign all ages in their specific subset
    groups = ages.groupby(pd.cut(ages.age, bin)).count()

    # set up the x and y axis, flatten the list of lists into a list
    x = range(1, 9)
    y = [item for sublist in groups.values.tolist() for item in sublist]

    total = sum(y)
    # and throw everything at plt to plot
    global fig
    plt.figure(fig)
    fig += 1

    plt.xticks(x, ['9-18', '19-28', '29-38', '39-48', '49-58', '59-68', '69-78', '79-88'])

    # display the value of each bar
    plt.ylim(top=900)
    for index, value in enumerate(y):
        plt.text(index + 0.6, value + 20, str(round(value / total * 100, 2)) + "%")

    # Highlight the max value in the graph
    color_ = []
    for val in y:
        if val == max(y):
            color_.append('orange')
        else:
            color_.append('blue')

    # display useful information about graph
    plt.grid(linewidth=0.25)
    plt.xlabel('Age groups')
    plt.ylabel('Number of individuals')
    plt.title('Age repartition of participants')
    plt.bar(x, y, color=color_)



# Display the percentage of the population at risk
def risk_age():
    at_risk = data[data['RISK AGE'] == 1]
    no_risk = data[data['RISK AGE'] == 0]

    x = [len(at_risk), len(no_risk)]
    labels_ = ['Higher risk (age >= 60)', 'Lower risk (age < 60)']
    explode_ = [0.1, 0]

    global fig
    plt.figure(fig)
    fig += 1

    plt.title('Percentage of population at higher risk vs. at lower risk (based on age)')
    plt.pie(x, labels=labels_, autopct='%1.1f%%', explode=explode_, shadow=True)



# Display professional status of individuals
def status_in():
    # useful variables (efficiency and readability)
    unemp_num = len(data[data['BE HOUSEWIFE'] == 1]) + len(data[data['BE UNEMPLOYED'] == 1])
    employee_num = len(data[data['BE PRIVATE COMPANY EMPLOYEE'] == 1] + data[data['BE PUBLIC EMPLOYEE'] == 1] +
                       data[data['BE FREELANCE'] == 1])
    retired_num = len(data[data['BE RETIRED'] == 1])
    student_num = len(data[data['BE STUDENT'] == 1])

    # set up the x and y axis accordingly
    x = range(1, 5)
    y = [employee_num, student_num, unemp_num, retired_num]

    total = sum(y)
    # and throw everything at plt to plot
    global fig
    plt.figure(fig)
    fig += 1

    plt.xticks(x, ['Employed', 'Student', 'Unemployed', 'Retired'])

    # display the value of each bar
    plt.ylim(top=1500)
    for index, value in enumerate(y):
        plt.text(index + 0.75, value + 20, str(round(value / total * 100, 2)) + "%", fontsize=12)

    # Highlight the max value in the graph
    color_ = []
    for val in y:
        if val == max(y):
            color_.append('orange')
        else:
            color_.append('green')

    plt.xlabel('Professional status')
    plt.ylabel('Number of individuals')
    plt.title('Professional status of participants')

    plt.grid(linewidth=0.25)
    plt.bar(x, y, color=color_)



# Display different effects of Covid-19 on participants, and changes in their lives
def covid_effects():
    # get the mean of various columns
    freedom = data['FREEDOM LIMITATION'].mean()
    work = data['WORK LIFE CHANGE'].mean()
    emotion = data['EMOTIONAL LIFE CHANGE'].mean()
    fam = data['FAMILY LIFE CHANGE'].mean()
    social = data['SOCIAL LIFE CHANGE'].mean()
    general = data['GENERAL LIFE CHANGE'].mean()

    # set up the x and y axis accordingly
    x = range(1, 7)
    y = [freedom, social, work, emotion, fam, general]

    # throw all to plt to plot
    global fig
    plt.figure(fig, figsize=(12, 6))
    fig += 1

    plt.xticks(x, ['Freedom', 'Work Life', 'Emotional Life', 'Family Life', 'Social Life', 'In general'])
    plt.tick_params(labelsize=12, pad=16)

    plt.grid(linewidth=0.25)
    plt.ylim(top=10)

    # this loop to show the numbers on the bar graph
    for index, value in enumerate(y):
        plt.text(index + 0.9, value + 0.5, str(round(value, 2)))

    # display info of graph, and plot
    plt.title('Effects of Covid-19 on participants, and changes in their lives', fontsize=16)
    plt.xlabel('Aspects of life changes', labelpad=24, fontsize=16)
    plt.ylabel('Scale of change (out of 10)', labelpad=24, fontsize=16)
    plt.bar(x, y, width=0.5, color=['orange', 'red', 'green', 'cyan', 'blue', 'purple'])


""" All calls to functions, description is provided above"""
gender_in()
age_in()
risk_age()
status_in()
covid_effects()


""" Plot and show all the graphs"""
plt.show()






""" Extra Graphs: type y if you would like to generate them, press anything else to exit."""

# General function to make pie charts based on the column feature passed as param
def make_pie(feature, title, angle):
    # Useful variable, combining data in three groups
    low = len(data[data[feature] == 1]) + len(data[data[feature] == 2])
    mod = len(data[data[feature] == 3])
    hi = len(data[data[feature] == 4]) + len(data[data[feature] == 5])

    # set up the list of groups and their labels
    y = [low, mod, hi]

    labels_ = ['A little to none', 'Moderate', 'Somewhat to very']
    explode_ = [0, 0, 0.1]

    # and throw everything at plt to plot
    global fig
    plt.figure(fig)
    fig += 1

    plt.axis('equal')
    plt.title(title)
    plt.pie(y, labels=labels_, autopct='%1.1f%%', explode=explode_, shadow=True, startangle=angle)

# Display percentage of participants that pay more attention to physical symptoms
def sympt_attent():
    # set up the parameters
    feature = 'ATTENTION TO SYMPTOMS'
    title = 'Percentage of participants that pay more attention to physical symptoms'
    angle = 120

    # make the pie accordingly
    make_pie(feature, title, angle)

# Percentage of participants that see the situation as a growth opportunity
def growth_opp():
    feature = 'GROWTH OPPORTUNITY'
    title = 'Percentage of participants that see the situation as a growth opportunity'
    angle = 160

    make_pie(feature, title, angle)

# Participant’s attitudes to the future COVID19 emergency’s resolution
def future_pred():
    # Separate the data into groups, store in variables
    day = data[data['ATTITUDES TO FUTURE'] == 1]
    month = data[data['ATTITUDES TO FUTURE'] == 2]
    many_mo = data[data['ATTITUDES TO FUTURE'] == 3]
    until_vac = data[data['ATTITUDES TO FUTURE'] == 4]

    # Set up the x and y coordinates accordingly
    x = range(1, 5)
    y = [len(day), len(month), len(many_mo), len(until_vac)]

    total = sum(y)
    # Throw at plt to plot
    global fig
    plt.figure(fig)
    fig += 1

    # Highlights the max value with a specific color
    color_ = []
    for val in y:
        if val == max(y):
            color_.append('orange')
        else:
            color_.append('blue')

    # Display the numbers for each bar
    plt.xlim(right=1550)
    for index, value in enumerate(y):
        plt.text(value + 10, index + 1, str(round(value / total * 100, 2)) + "%", fontsize=11)

    # Add some useful information about the graph
    plt.yticks(x, ['Within 1 day', 'Within 1 month', 'Within several months', 'Until vaccine found'])
    plt.grid(linewidth=0.25)

    plt.title('Participant’s attitudes to the future COVID19 emergency’s resolution')
    plt.xlabel('# of participants')
    plt.barh(x, y, color=color_)




try:
    x = 'q'
    x = input("Type y to continue. Or anything else to exit.\n")
    if(x != 'y'):
        exit(0)
    
except SyntaxError:
    pass


sympt_attent()
growth_opp()
future_pred()

plt.show()
