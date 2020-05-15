# -*- coding: utf-8 -*-

""" Author: Samy ALLAL - samyallal00@ucla.edu """

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


#import tkinter
#matplotlib.use('tkAgg')

fig = 0

# Upload the Data set here, and load the data
# NOTE: Change file path to the path of the csv file in your machine
bad_data = ['', '?', 'NaN']
data = pd.read_csv('data_3.csv', na_values=bad_data)

# the data info is for reference, helps know the different features we have
print(data.info())


# Display genders statistics
def gender_in():
    # make a male list and a female list from the data
    male = data[data['gender'] == 'Male']
    female = data[data['gender'] == 'Female']
    other = data[data['gender'] == 'Other']

    # set up the x and y axis accordingly
    x = [1, 2, 3]
    y = [len(male), len(female), len(other)]

    total = sum(y)
    # and throw everything at plt to plot
    global fig
    plt.figure(fig)
    fig += 1

    plt.xticks(x, ['Male', 'Female', 'other'])

    # display the value of each bar
    plt.ylim(top=2000)
    for index, value in enumerate(y):
        plt.text(index + 0.85, value + 35, str(round(value / total * 100, 2)) + '%', fontsize=12)

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
    plt.title('Gender repartition of participants')

    plt.bar(x, y, color=color_)


# Display age of individuals
def age_in():
    # get all ages in the dataset, store in ages and make age bins to cut
    data['age'] = pd.to_numeric(data['age'].iloc[2:])
    ages = pd.DataFrame({'age': data['age']})
    bin = [9, 19, 29, 39, 49, 59, 69, 79, 89]

    # assign all ages in their specific subset
    groups = ages.groupby(pd.cut(2020 - ages.age, bin)).count()

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
    plt.ylim(top=950)
    for index, value in enumerate(y):
        plt.text(index + 0.6, value + 20, str(round(value / total * 100, 2)) + '%')

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



# Display Health level of individuals
def health_in():
    # useful variables (efficiency and readability)
    excellent = len(data[data['health'] == 'Excellent'])
    good = len(data[data['health'] == 'Good'])
    fair = len(data[data['health'] == 'Fair'])
    poor = len(data[data['health'] == 'Poor'])

    # set up the x and y axis accordingly
    x = range(1, 5)
    y = [poor, fair, good, excellent]

    total = sum(y)
    # and throw everything at plt to plot
    global fig
    plt.figure(fig)
    fig += 1

    plt.xticks(x, ['Poor', 'Fair', 'Good', 'Excellent'])

    # display the value of each bar
    plt.ylim(top=2100)
    for index, value in enumerate(y):
        plt.text(index + 0.75, value + 30, str(round(value / total * 100, 2)) + '%', fontsize=12)

    # Highlight the max value in the graph
    color_ = []
    for val in y:
        if val == max(y):
            color_.append('orange')
        else:
            color_.append('green')

    plt.xlabel('Health condition')
    plt.ylabel('Number of individuals')
    plt.title('Health condition of participants')

    plt.grid(linewidth=0.25)
    plt.bar(x, y, color=color_)



# 'Aspects of life changes'
def behav_in():
    # get the mean of various columns
    home = pd.to_numeric(data['SelfReported_Behavio_1'].iloc[2:]).mean()
    no_gath = pd.to_numeric(data['SelfReported_Behavio_2'].iloc[2:]).mean()
    wash_hand = pd.to_numeric(data['SelfReported_Behavio_3'].iloc[2:]).mean()
    distance = pd.to_numeric(data['SelfReported_Behavio_4'].iloc[2:]).mean()
    inform_peop = pd.to_numeric(data['SelfReported_Behavio_5'].iloc[2:]).mean()

    # set up the x and y axis accordingly
    x = range(1, 6)
    y = [home, no_gath, wash_hand, distance, inform_peop]

    # throw all to plt to plot
    global fig
    plt.figure(fig, figsize=(12, 6))
    fig += 1

    plt.xticks(x, ['Stayed at home', 'No gatherings', 'Wash hands regularly', 'Social Distancing',
                   'Informs people when sick'])
    plt.tick_params(labelsize=12, pad=16)

    plt.grid(linewidth=0.25)
    plt.ylim(top=100)

    # this loop to show the numbers on the bar graph
    for index, value in enumerate(y):
        plt.text(index + 0.9, value + 1.5, str(round(value, 2)) + '%', fontsize=11)

    # display info of graph, and plot
    plt.title('Effects of Covid-19 on participants\' habits, and daily life', fontsize=16)
    plt.xlabel('Aspects of life changes', labelpad=24, fontsize=16)
    plt.ylabel('Scale of change (in %)', labelpad=24, fontsize=16)
    plt.bar(x, y, width=0.5, color=['orange', 'green', 'cyan', 'blue', 'purple'])


# General function to make bar charts about similar aspects (1-5 questions)
def make_barh(feature, title, kwargs):
    one = len(data[data[feature] == kwargs[0]])
    two = len(data[data[feature] == kwargs[1]])
    three = len(data[data[feature] == kwargs[2]])
    four = len(data[data[feature] == kwargs[3]])
    five = len(data[data[feature] == kwargs[4]])

    x = range(1, 6)
    y = [one, two, three, four, five]

    total = sum(y)

    # Plot
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
    plt.xlim(right=1750)
    for index, value in enumerate(y):
        plt.text(value + 10, index + 1, str(round(value / total * 100, 2)) + '%', fontsize=11)

    # Add some useful information about the graph
    plt.yticks(x, ['Strongly Disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly Agree'])
    plt.grid(linewidth=0.25)

    plt.title(title)
    plt.xlabel('Number of participants')
    plt.barh(x, y, color=color_)


# Mental Health and well being of participants
def curr_circum1():
    feature = 'anxiety_1'
    title = 'Being nervous when thinking about current circumstances'

    kwargs = ['Does not apply at all', 'Somewhat does not apply', 'Neither applies nor does not apply',
              'Somewhat applies', 'Strongly applies']

    make_barh(feature, title, kwargs)



# Mental Health and well being of participants
def curr_circum2():
    feature = 'anxiety_2'
    title = 'Being calm and relaxed'

    kwargs = ['Does not apply at all', 'Somewhat does not apply', 'Neither applies nor does not apply',
              'Somewhat applies', 'Strongly applies']

    make_barh(feature, title, kwargs)



# Mental Health and well being of participants
def curr_circum3():
    feature = 'anxiety_3'
    title = 'Being worried about their health'

    kwargs = ['Does not apply at all', 'Somewhat does not apply', 'Neither applies nor does not apply',
              'Somewhat applies', 'Strongly applies']

    make_barh(feature, title, kwargs)



# Mental Health and well being of participants
def curr_circum4():
    feature = 'anxiety_4'
    title = 'Being worried about the health of family members'

    kwargs = ['Does not apply at all', 'Somewhat does not apply', 'Neither applies nor does not apply',
              'Somewhat applies', 'Strongly applies']

    make_barh(feature, title, kwargs)



# Reasons to go out
def reason_out():
    # Convert to list, easy to work with
    list_ = data['Q25'].iloc[2:].tolist()

    # These two loops will clean the data
    new_list = []
    for elt in list_:
        split_ = str(elt).split(',')
        for item in split_:
            new_list.append(item)

    new_list2 = []
    for elt in new_list:
        split_ = str(elt).split(' / ')
        for item in split_:
            new_list2.append(item)

    # List cleaned and ready to work with
    list_ = new_list2

    # Get all the different variables
    work = [w for w in list_ if w == 'Going to work']
    freedom = [f for f in list_ if f == 'Exercising my freedom']
    pet = [p for p in list_ if p == 'Walking a pet']
    hospital = [h for h in list_ if h == 'Going to the hospital']
    meds = [m for m in list_ if m == 'receiving medical treatement']
    tired = [t for t in list_ if t == 'Getting tired of being inside of the house']
    sport = [s for s in list_ if s == 'Doing physical activity (e.g. exercising']
    pharm = [p for p in list_ if p == 'Going to the pharmacy']
    food = [f for f in list_ if f == 'Procuring food for yourself or family']
    friend = [f for f in list_ if f == 'Meeting friends or relatives']
    fam = [f for f in list_ if f == 'Taking care or dependents']
    bs = [b for b in list_ if b == 'Getting some adrenaline (from breaking the law)']
    bored = [b for b in list_ if b == 'Getting bored']
    other = [o for o in list_ if o == 'Other (specify):']

    # Set up the x and y axis, and their labels
    x = range(1, 15)
    y = [len(food), len(pharm), len(work), len(pet), len(sport), len(hospital), len(tired),
         len(freedom), len(friend), len(bored), len(bs), len(fam), len(meds), len(other)]
    y = y[::-1]

    total = sum(y)
    labels = ['Other', 'receiving medical treatement', 'Taking care or dependents',
              'Getting some adrenaline (from breaking the law)', 'Getting bored',
              'Meeting friends or relatives', 'Exercising my freedom',
              'Getting tired of being inside of the house', 'Going to the hospital',
              'Doing physical activity', 'Walking a pet', 'Going to work',
              'Going to the pharmacy', 'Procuring food for yourself or family']

    # Plot
    plt.figure(8, figsize=(10, 12))
    plt.yticks(x, labels)

    # Highlights the max value with a specific color
    color_ = []
    for val in y:
        if val == max(y):
            color_.append('orange')
        else:
            color_.append('blue')

    # Display the numbers for each bar
    plt.xlim(right=2000)
    for index, value in enumerate(y):
        plt.text(value + 10, index + 1, str(round(value / total * 100, 2)) + '%', fontsize=11)

    # Throw all to plt to plot
    plt.grid(linewidth=0.25)

    plt.title('Participant’s attitudes to the future COVID19 emergency’s resolution')
    plt.xlabel('Number of participants')
    plt.barh(x, y, color=color_)




""" All calls to functions. Description above."""
gender_in()
age_in()
health_in()
behav_in()
curr_circum1()
curr_circum2()
curr_circum3()
curr_circum4()
reason_out()

# This shows all the graphs each in a different window
plt.show()
