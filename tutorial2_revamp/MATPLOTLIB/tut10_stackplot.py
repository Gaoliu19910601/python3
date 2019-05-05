
import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl


a = ['classic', 'default']

i=1 # 0 - classic and 1 - default

mpl.style.use(a[i])




lim1 = 1
lim2 = 10
N = 6

x = np.linspace(2005, 2010, N)

# np.random.seed(128987) # to have a consistent randomization

expense1 = np.random.randint(lim1, lim2, N)
expense2 = np.random.randint(lim1, lim2, N)
expense3 = np.random.randint(lim1, lim2, N)
expense4 = np.random.randint(lim1, lim2, N)
expense5 = np.random.randint(lim1, lim2, N)
expense6 = np.random.randint(lim1, lim2, N)

print(expense1)

expenses = [expense1, expense2, expense3, expense4, expense5, expense6]

colors = ['red', 'green', 'chocolate', 'cyan', 'yellow', 'blue']

labels = ['a', 'b', 'c', 'd', 'e', 'f']


plt.figure(1)
plt.stackplot(x, expenses, colors=colors, labels = labels)
plt.xlabel('Year')
plt.ylabel('Expenses')
plt.legend()
plt.grid(True)
plt.show()
