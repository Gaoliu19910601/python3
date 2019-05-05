import numpy as np
import pandas as pd
#
#
# original = [1,2,3]
# a = np.array(original)
#
# print(original)
# print(a)
#
# b = np.array([[1,2,3],[5,6,7]])
#
# print(b)
#
# print(np.arange(10,50,5))
#
# c = np.linspace(0,100,10)
#
# d = np.zeros((5,5))
#
# print(c)
# print(d)
#
# e = np.ones(18)
#
# print(e)
#
# f = e.reshape(2,3,3) # 2 depth - 3x3(L*B) matrix - 3 Dimensional array
#
# print(f)
#
# g = f.ravel() # levels out the 3D to 1D
#
# print(g)
#
# h = np.arange(20)
#
# print(h)
#
# arr_slice = slice(1,10,2)
#
# print(h[arr_slice])
#
# i = np.array([[1,2,3],[4,5,6],[7,8,9]])
#
# print(i[0:2,0:3])
# print(i.shape)
# print(i.ndim)
#
# j = np.empty([3,2],dtype=int)
#
# print(j)
#
# l = np.array([[1,2,3],[3,4,5],[5,6,7]])
#
# k = np.savetxt('test.csv',l,delimiter=',')
#
# # m = np.loadtxt('test.txt')
# m = np.genfromtxt('test.csv',delimiter=',')
#
# print(m)



# Creating a series in pandas
n = np.array([11,23,54,76,35,85,35])
data_dict = {'a':2,"b":3,"c":4,'d':500,'e':600,'f':800,'g':400}

o = pd.Series(n)
o_dict = pd.Series(data_dict)

# print(o)
# print(o_dict[:])

# Creating a dataframe in pandas
listx = [2,5,3,7,4,8,3]
listx2 = [{'a':1,'b':11},{'a':2,"b":22},{'a':3,"b":33}]
listx3 = [{'a':1,'b':11},{'a':2,"b":22},{'a':3,"b":33},{'a':4,"b":44,'c':444}]

table = pd.DataFrame(listx)
table2 = pd.DataFrame(listx2,index=['Row-1','Row-2','Row-3'])
table3 = pd.DataFrame(listx3,index=['Amar','Dilip','Ramana','Hanu'])

# print(table)
# print(table2)
# print(table3)


series1 = pd.Series([70,45,85,56,67],index=['Maths','Chemistry','Physics','c++','Biology'])
series2 = pd.Series([95,64,35,68,79],index=['Maths','Chemistry','Physics','c++','Biology'])
table4 = pd.DataFrame({'Amar':series1,
                       'Deep':series2,
                       'Jim': pd.Series([73,35,45,54],index=['Maths','Chemistry','Physics','Biology'])})

print(table4)
print(table4.loc['Chemistry'])
print(table4.iloc[3])
#
jim_series = table4.pop('Jim')
print(table4)
print(jim_series)

table5 = pd.DataFrame({'ID-1': pd.Series([25,46,79],index=['FD-1','FD-2','FD-3']),
                       'ID-2': pd.Series([55,66,77],index=['FD-1','FD-2','FD-3'])})

table5['ID-3'] = pd.Series([15, 26, 37], index=['FD-1', 'FD-2', 'FD-3'])
table5['ID-4'] = pd.Series([66,77,88], index=['FD-1','FD-2','FD-3'])

row = pd.DataFrame([[11,23,45,54]],index=['FD-4'],columns=['ID-1','ID-2','ID-3','ID-4'])
table5 = table5.append(row)

# table5 = table5.drop('FD-3')

print(table5)

# table5.to_csv("pandas_example.csv")

table6 = pd.read_csv("pandas_example.csv")

# pd.read_excel(path to file)    #  used to import from excel file
# table6.to_excel(path to file)  #  used to export to excel file

print(table6)



