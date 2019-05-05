
import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl




range_vals = np.linspace(0, 100, 11)

count1 = np.random.rand(10)*4.0
count2 = -np.random.rand(10)*8.0
count3 = np.random.rand(10)*2.0
count4 = np.random.rand(10)*5.0
errors = np.ones(10)*0.5
bar_width = 2.0

a = ['classic', 'default']

i=0 # 0 - classic and 1 - default

mpl.style.use(a[i])

groups = ['group1', 'group2', 'group3', 'group4', 'group5', 'group6', 'group7', 'group8', 'group9', 'group10']


if i==0:
    mid_vals = (range_vals[0:-1] + range_vals[1:]) * 0.5 - bar_width * 0.5  # to compensate for the bar width increase fucking up the centre in classic rendering
    plt.bar(mid_vals-bar_width*1.0,  count1,  width=bar_width,  facecolor='chocolate',  label='sample bar1',  yerr=errors)
    plt.bar(mid_vals-bar_width*0.0,  count2,  width=bar_width,  facecolor='aquamarine',  label='sample bar2',  yerr=errors)
    plt.bar(mid_vals-bar_width*0.0,  count3,  width=bar_width,  facecolor='red',  label='sample bar3',  yerr=errors)
    plt.bar(mid_vals+bar_width*1.0,  count4,  width=bar_width,  facecolor='green',  label='sample bar4',  yerr=errors)
    plt.xticks(mid_vals + bar_width * 0.5, groups,rotation='45')
    plt.grid(True)
    plt.xlabel('Range')
    plt.ylabel('Count')
    plt.legend()
    plt.show()

else:
    mid_vals = (range_vals[0:-1] + range_vals[1:]) * 0.5
    plt.bar(mid_vals-bar_width*1.0, count1, width=bar_width, facecolor='chocolate', label='sample bar1', yerr=errors)
    plt.bar(mid_vals-bar_width*0.0, count2, width=bar_width, facecolor='aquamarine', label='sample bar2', yerr=errors)
    plt.bar(mid_vals-bar_width*0.0, count3, width=bar_width, facecolor='red', label='sample bar3', yerr=errors)
    plt.bar(mid_vals+bar_width*1.0, count3, width=bar_width, facecolor='green', label='sample bar4', yerr=errors)
    plt.xticks(mid_vals,groups,rotation='45')

    plt.grid(True)
    plt.xlabel('Range')
    plt.ylabel('Count')
    plt.legend()
    plt.show()




