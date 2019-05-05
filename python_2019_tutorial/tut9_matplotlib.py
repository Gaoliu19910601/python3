import matplotlib.pyplot as plt
import numpy as np

# x = np.arange(0,100)
x = range(5)
# print(x)

y = [i**2 for i in x]

plt.figure(1)
plt.plot(x,[i*2 for i in x],'--b*')
plt.plot(x,[i*4 for i in x],':r^')
plt.plot(x,[i*8 for i in x],'-gd')
plt.grid(True)
plt.xlim([-1,6])
plt.ylim([-1,35])
# plt.axis([-1,5,-1, 40])
plt.xlabel('X value',fontweight='bold')
plt.ylabel('Y value',fontweight='bold')
plt.title('Diagram Sample',fontweight='bold')
plt.legend(['twice','4 times','8 times'])
# plt.savefig('sample_dia.png')
# plt.show()


histy = np.random.rand(10,10)

plt.figure(2)
plt.hist(histy,100)
plt.grid(True)
# plt.show()

plt.figure(3)
plt.bar([2.5,3.7,4.8],[35,56,87])
plt.grid(True)
# plt.show()


# Plotting bar charts for Dictionaries - it is possible
amar_dict = {'a':23, 'b':45, 'c':14, 'd':34, 'e':78}
print(amar_dict.keys())

plt.figure(4)
for i,keys in enumerate(amar_dict):
    plt.bar(i+1,amar_dict[keys])
plt.xticks([1,2,3,4,5],amar_dict.keys())
plt.grid(True)
# plt.show()


# plotting pie charts
x = [40,23,15,17,46,87,45,36]
labels = ['car','food','rent','bus','cloth','radio','shoe','TV']
plt.figure(5)
plt.figure(figsize=(3,3))
plt.pie(x,labels=labels)
# plt.show()

#plotting scatter plots
plt.figure(6)
x1 = np.random.rand(400)
y1 = np.random.rand(400)
plt.scatter(x1,y1)
plt.grid(True)
plt.show()