
import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl


range_vals = np.linspace(0, 100, 11)

count1 = np.random.rand(10)*4.0
count2 = -np.random.rand(10)*8.0
count3 = np.random.rand(10)*2.0
count4 = np.random.rand(10)*5.0
errors = np.ones(10)*0.5
bar_width = 4.0



a = ['classic', 'default']

i=0 # 0 - classic and 1 - default


mpl.style.use(a[i])



groups = ['group1', 'group2', 'group3', 'group4', 'group5', 'group6', 'group7', 'group8', 'group9', 'group10']



if i==0:
    mid_vals = (range_vals[0:-1] + range_vals[1:]) * 0.5 - bar_width * 0.5  # to compensate for the bar width increase fucking up the centre in classic rendering
    plt.barh(mid_vals-bar_width*0.0,  count1,  left=count3, height=bar_width-1.0,  facecolor='chocolate',  align='center',  label='sample bar1',  xerr=errors)
    plt.barh(mid_vals-bar_width*0.0,  count3,  height=bar_width,  facecolor='red',  align='center',  label='sample bar3',  xerr=errors)
    plt.barh(mid_vals+bar_width*0.0,  count4,  left=count3+count1,  height=bar_width-2.0,  facecolor='green',   align='center', label='sample bar4',  xerr=errors)
    # plt.xticks(mid_vals + bar_width * 0.5, groups, rotation='45')
    plt.grid(True)
    plt.xlabel('Range')
    plt.ylabel('Count')
    plt.legend()
    plt.show()

else:
    mid_vals = (range_vals[0:-1] + range_vals[1:]) * 0.5
    plt.barh(mid_vals-bar_width*0.0,  count1,  left=count3,  height=bar_width-0.5,  facecolor='chocolate',  align='center',  label='sample bar1',  xerr=errors)
    plt.barh(mid_vals-bar_width*0.0,  count2,  height=bar_width,  facecolor='aquamarine',  align='center',  label='sample bar2',  xerr=errors)
    plt.barh(mid_vals-bar_width*0.0,  count3,  height=bar_width,  facecolor='red',  align='center',  label='sample bar3',  xerr=errors)
    plt.barh(mid_vals+bar_width*0.0,  count4,  left=count3+count1, height=bar_width-1.0,  facecolor='green',   align='center', label='sample bar4',  xerr=errors)

    plt.yticks(mid_vals, groups, rotation='0')

    # plt.grid(True)
    plt.ylabel('Range')
    plt.xlabel('Count')
    plt.legend()
    plt.show()





