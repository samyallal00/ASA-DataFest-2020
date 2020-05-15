# Adam Young youngcadam@g.ucla.edu
#
#
#
# Datafest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import tkinter

matplotlib.use('tkAgg')
# for coloring graphs
colors = sns.color_palette("hls", 3)



# load dataset
bad_data = ['', '?']
data = pd.read_csv('data_1.csv', na_values=bad_data)



# partition data based on those working, working (in-person), smart-working, not working, not working with pay, and not working without pay
working = data[(data['WORK UNTIL CLOSURE'] == 1) | (data['SMART WORKING'] == 1) | (data['BASIC NECESSITY WORK'] == 1)]
ip_working = data[(data['WORK UNTIL CLOSURE'] == 1) | (data['BASIC NECESSITY WORK'] == 1)]
smart_working = data[data['SMART WORKING'] == 1]
not_working = data[(data['NOT WORKING NOT PAYED'] == 1) | (data['NOT WORKING BUT PAYED'] == 1) ]
not_working_but_payed = data[data['NOT WORKING BUT PAYED'] == 1]
not_working_not_payed = data[data['NOT WORKING NOT PAYED'] == 1]



# box plot Measuring WORK LIFE CHANGE (this verifies the dataset is somewhat reliable)
y1 = working['WORK LIFE CHANGE']
y2 = ip_working['WORK LIFE CHANGE']
y3 = smart_working['WORK LIFE CHANGE']
y4 = not_working['WORK LIFE CHANGE']
y5 = not_working_but_payed['WORK LIFE CHANGE']
y6 = not_working_not_payed['WORK LIFE CHANGE']
vec1 = [y1, y2, y3]
vec2 = [y4, y5, y6]
labels1 = ['Overall', 'From Workplace', 'From Home']
labels2 = ['Overall', 'Paid', 'Not Paid']
fig, axs = plt.subplots(1, 2)
axs[0].set_title('Employed: In-Person vs Working From Home')
axs[1].set_title('Unemployed: Paid vs Unpaid')
bplot1 = axs[0].boxplot(vec1, labels=labels1, notch=True, patch_artist=True)
bplot2 = axs[1].boxplot(vec2, labels=labels2, notch=True, patch_artist=True)
for bplot in (bplot1, bplot2):
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)
for ax in axs:
    ax.yaxis.grid(True)
    ax.set_ylabel('Work-life Change (1-10)')
plt.suptitle('Work-life Change in Working and Non-working populations')
# plt.show()



# box plot for NEED SUPPORT (this shows unemployed people may have a greater need for psychological support)
y1 = working['NEED SUPPORT']
y2 = ip_working['NEED SUPPORT']
y3 = smart_working['NEED SUPPORT']
y4 = not_working['NEED SUPPORT']
y5 = not_working_but_payed['NEED SUPPORT']
y6 = not_working_not_payed['NEED SUPPORT']
vec1 = [y1, y2, y3]
vec2 = [y4, y5, y6]
labels1 = ['Overall', 'From Workplace', 'From Home']
labels2 = ['Overall', 'Paid', 'Not Paid']
fig, axs = plt.subplots(1, 2)
axs[0].set_title('Employed: In-Person vs Working From Home')
axs[1].set_title('Unemployed: Paid vs Unpaid')
bplot1 = axs[0].boxplot(vec1, labels=labels1, notch=True, patch_artist=True)
bplot2 = axs[1].boxplot(vec2, labels=labels2, notch=True, patch_artist=True)
for bplot in (bplot1, bplot2):
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)
for ax in axs:
    ax.yaxis.grid(True)
    ax.set_ylabel('Measure of Agreement')
plt.suptitle('Responses to, "To face the current situation, psychological counselling/support would be helpful"')
# plt.show()




# z-test for unemployed vs employed workers mean response to survey question:
# "To face the current situation, psychological counselling/support would be help"  1 Strongly Disagree - 5 Strongly Agree
from statsmodels.stats.weightstats import ztest

mod = ztest(y4, y1)
print('z-test results')
print('test statistic: %f' %(mod[0]))
print('p-value: %f' %(mod[1])) 	 # p = 0.021451 small so we can reject null hypothesis and conclude unemployed people agree more

plt.show()
