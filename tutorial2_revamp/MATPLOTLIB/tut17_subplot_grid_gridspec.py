import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gs
import matplotlib as mpl
a = ['classic','default','seaborn','grayscale','dark_background','ggplot']
i=1 # 0 - classic and 1 - default

mpl.style.use(a[i])


#====================== SUBPLOT2GRID FUNCTION ============================

# get the handle
fig = plt.figure(1)

ax1 = plt.subplot2grid((3, 3), (0, 0), rowspan=1,colspan=3)
ax2 = plt.subplot2grid((3, 3), (1, 0), rowspan=1,colspan=2)
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2,colspan=1)
ax4 = plt.subplot2grid((3, 3), (2, 0), rowspan=1,colspan=1)
ax5 = plt.subplot2grid((3, 3), (2, 1), rowspan=1,colspan=1)

ax1.text(0.5,0.5,'ax1',ha='center',va='center')
ax2.text(0.5,0.5,'ax2',ha='center',va='center')
ax3.text(0.5,0.5,'ax3',ha='center',va='center')
ax4.text(0.5,0.5,'ax4',ha='center',va='center')
ax5.text(0.5,0.5,'ax5',ha='center',va='center')

plt.suptitle('Subplotting using grid')
plt.tight_layout()
# plt.show()



#======================== GRIDSPEC format =============================

fig2 = plt.figure(2)

gs1 = gs.GridSpec(3, 3)

ax6 = fig2.add_subplot(gs1[0,0:3])
ax7 = fig2.add_subplot(gs1[1,0:2])
ax8 = fig2.add_subplot(gs1[1:3,2])
ax9 = fig2.add_subplot(gs1[2,0])
ax10 = fig2.add_subplot(gs1[2,1])


ax6.text(0.5,0.5,'ax6',ha='center',va='center')
ax7.text(0.5,0.5,'ax7',ha='center',va='center')
ax8.text(0.5,0.5,'ax8',ha='center',va='center')
ax9.text(0.5,0.5,'ax9',ha='center',va='center')
ax10.text(0.5,0.5,'ax10',ha='center',va='center')

plt.suptitle('Subplotting using gridSpec')
plt.tight_layout()
# plt.show()



#======================== Using multiple GRIDSPEC =============================

fig3 = plt.figure(3)

gs2 = gs.GridSpec(3, 3)
gs2.update(left=0.05,right=0.48,hspace=0.05)

ax11 = fig3.add_subplot(gs2[0:2,0:3])
ax12 = fig3.add_subplot(gs2[2,0:2])
ax13 = fig3.add_subplot(gs2[2,2])

ax11.text(0.5,0.5,'ax11',ha='center',va='center')
ax12.text(0.5,0.5,'ax12',ha='center',va='center')
ax13.text(0.5,0.5,'ax13',ha='center',va='center')

gs3 = gs.GridSpec(3, 3)
gs3.update(left=0.55,right=0.98,hspace=0.05)

ax14 = fig3.add_subplot(gs3[0:2,0:3])
ax15 = fig3.add_subplot(gs3[2,0:2])
ax16 = fig3.add_subplot(gs3[2,2])

ax14.text(0.5,0.5,'ax14',ha='center',va='center')
ax15.text(0.5,0.5,'ax15',ha='center',va='center')
ax16.text(0.5,0.5,'ax16',ha='center',va='center')

plt.tight_layout()
plt.suptitle('Subplotting using Multiple gridSpec')

plt.show()
