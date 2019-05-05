import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl

a = ['classic','default','seaborn','grayscale','dark_background','ggplot']
i=1 # 0 - classic and 1 - default

mpl.style.use(a[i])

distro = ['ArchLinux','Ubuntu','Debian','Fedora','LinuxMint','X-Ubuntu','K-Ubuntu','Gentoo','openSUSE','Other']

colors = ['red','blue','green','cyan','chocolate','beige','yellow','purple','orange','grey']

values = [881,697,308,268,209,117,99,97,58,356]

Explodes = np.zeros(10)
Explodes[1] = 0.1
Explodes[4] = 0.4
Explodes[8] = 0.6

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}% ({v:d})'.format(p=pct,v=val)
    return my_autopct





plt.figure(1)
# plt.axes(aspect=1) # To get a perfect circle for the pie (before the pie function)
plt.axis([-1.5,1.5,-1.5,1.5])

plt.pie(values,
        labels=distro,      # prints the given labels
        colors=colors,      # prints the given colors
        radius = 1.0,       # increase the size of pie
        autopct = make_autopct(values), # custom tailored
        # autopct='%2.2f%%',  # input percentage automatically
        pctdistance=0.6,    # distance between centre and display %
        startangle=90,      # mention the start angle
        labeldistance=1.1,  # distance between label and pie
        counterclock=False, # default is true, changes orientation
        explode=Explodes,   # removes the selected chunk
        shadow=True,        # Shadows the pie
        frame=True          # Creates a frame for the figure but require plt.axis
        )

plt.title('PIE CHART: Linux Distro popularity')
plt.axis('equal') # To get a perfect circle for the pie (after the pie function)
plt.show()