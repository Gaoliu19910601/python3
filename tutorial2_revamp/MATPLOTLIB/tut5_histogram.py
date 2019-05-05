
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.style.use('classic')

mean = 100
sd = 15
N = 1000
binsize=20

IQ = np.random.normal(mean, sd, N)

count, bin, extra = plt.hist(IQ, binsize, facecolor='blue', normed=False,  label='IQs')
plt.plot(bin[1:], count, label='series', color='r')
plt.xlabel('IQ')
plt.ylabel('Count/Fraction')
plt.title('IQ distribution')
# plt.xticks(bin)
plt.grid(True)
plt.legend()
plt.show()