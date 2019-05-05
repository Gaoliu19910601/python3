import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt

pd.set_option('display.max_columns',10)
# pd.set_option('display.max_rows',10)
# pd.set_option('display.max_colwidth',10)
# pd.set_option('display.width',10)

data = pd.read_csv('titanic.csv')

# print(data['Fare'])
# print(data['Survived'])
# print(data['Sex'])
# print(data['Age'])



# sys.exit()


# print(data.isnull().sum()) # to check NaN values in any column

###------- To remove NaN values from Age if any found ------###

age_wrangled = data[pd.notnull(data['Age'])]

# print('# of passengers in age wrangled data: {} \n'.format(age_wrangled.index))

# print(age_wrangled.head(10))

#-------------------Effect of Gender on Survival---------------------------------------#

gender_data = data.groupby('Sex',as_index=False)


gender_mean_data = gender_data.mean() # get mean of all columns w.r.t Sex

# gender_mean_data.to_csv('example1.txt')

# print(gender_mean_data)



total_nos = gender_data['Name'].count()
total_nos.columns = ['Sex','Total'] # To change the column title

# print(total_nos)

del total_nos['Sex'] # To prevent overwrite of 'Sex' in line 57 (add func)

# print(total_nos)


total_survived = gender_data['Survived'].sum()

# print(total_survived)

del total_survived['Sex'] # To prevent overwrite of 'Sex' in line 57 (add func)

# print(total_survived)


compare_survival_rate = total_nos.add(total_survived,fill_value=0)

# print(compare_survival_rate)
# print('Total survival rate: {}'.format(data['Survived'].mean()))


compare_survival_rate.plot.bar(color=['limegreen','dodgerblue'])
plt.title('Effect of Gender on Survival',fontweight='bold')
plt.xlabel('Gender',fontweight='bold')
plt.ylabel('No. of people',fontweight='bold')
plt.xticks([0,1],['Female','Male'])

survived_labels = compare_survival_rate.loc[0]['Survived'],compare_survival_rate.loc[1]['Survived']
total_labels = compare_survival_rate.loc[0]['Total'],compare_survival_rate.loc[1]['Total']

plt.text(-0.12, 200, compare_survival_rate.loc[0]['Survived'],
     horizontalalignment='center',
     verticalalignment='center',fontweight='bold',color='w')

plt.text(0.12, 290, compare_survival_rate.loc[0]['Total'],
     horizontalalignment='center',
     verticalalignment='center',fontweight='bold',color='w')

plt.text(0.89, 90, compare_survival_rate.loc[1]['Survived'],
     horizontalalignment='center',
     verticalalignment='center',fontweight='bold',color='w')

plt.text(1.12, 550, compare_survival_rate.loc[1]['Total'],
     horizontalalignment='center',
     verticalalignment='center',fontweight='bold',color='w')

# plt.show()

#----------- Effect of Age and class on Survival--------------#

survival_data = data.groupby('Survived',as_index=False)

# print(survival_data['Age'].count())

# print(survival_data.mean()) # We can observe that younger people with higher class and having less siblings and more parents/children survived

# print(survival_data['Pclass'].count())

children_data = data[data['Age'] <= 18.0]
adult_data = data[data['Age'] > 18.0]

# print(children_data['Age'])


children_list = [children_data['Pclass'].count(),children_data['Survived'].sum()]
adult_list = [adult_data['Pclass'].count(),adult_data['Survived'].sum()]
total_list = [children_list,adult_list]

# print(children_list)
# print(adult_list)
# print(total_list)

Age_stats = pd.DataFrame([children_list,
                         adult_list],columns=['Total','Survived'],
                         index=['Children','Adult'])

# Age_stats['Survival %'] = pd.Series([children_list[1]*100.0/children_list[0],
#                             adult_list[1]*100.0/adult_list[0]],index=['Children','Adult'])

# print(Age_stats)

Age_stats.plot.bar(color=['limegreen','dodgerblue'])
plt.xlabel('Age',fontweight='bold')
plt.ylabel('No. of people',fontweight='bold')
plt.title('Effect of Age on Survival',fontweight='bold')

plt.text(-0.12, 136, children_list[0],
     horizontalalignment='center',
     verticalalignment='center',fontweight='bold',color='w')

plt.text(0.12, 58, children_list[1],
     horizontalalignment='center',
     verticalalignment='center',fontweight='bold',color='w')

plt.text(0.89, 689, adult_list[0],
     horizontalalignment='center',
     verticalalignment='center',fontweight='bold',color='w')

plt.text(1.12, 234, adult_list[1],
     horizontalalignment='center',
     verticalalignment='center',fontweight='bold',color='w')

# plt.show()

# print(children_data.mean()['Survived'])

Survival_age = [children_data.mean()['Survived'],
                adult_data.mean()['Survived']]

plt.figure(3)
plt.bar([0,1],Survival_age,align='center',color=['limegreen','dodgerblue'])
plt.xlabel('Age',fontweight='bold')
plt.ylabel('Survival rate',fontweight='bold')
plt.title('Survival rate due to Age',fontweight='bold')
plt.xticks([0,1],['Children','Adult'])

plt.text(0, Survival_age[0]-0.03, round(Survival_age[0],4),
     horizontalalignment='center',
     verticalalignment='center',fontweight='bold',color='w')

plt.text(1, Survival_age[1]-0.03, round(Survival_age[1],4),
     horizontalalignment='center',
     verticalalignment='center',fontweight='bold',color='w')

# plt.show()

plt.figure(4)
data['Age'].plot.hist(bins=range(100),color='dodgerblue',  edgecolor='black', linewidth=1.0,alpha=0.6)
plt.axvline(data['Age'].mean() ,color='r', linestyle='dashed', linewidth=1.2)
plt.xlabel('Age',fontweight='bold')
plt.ylabel('No of Passengers',fontweight='bold')
plt.title('Age distribution of all passengers',fontweight='bold')
plt.text(data['Age'].mean()+13,37,'Mean: {}'.format(round(data['Age'].mean(),2)),
         horizontalalignment='center',
     verticalalignment='center',color='r')
# plt.grid(True)
# plt.show()


plt.figure(5)
survival_data['Age'].plot.hist(bins=range(100),color='limegreen',  edgecolor='black', linewidth=1.0,alpha=1.0)
# plt.axvline(survival_data['Age'].mean() ,color='r', linestyle='dashed', linewidth=1.2)
plt.xlabel('Age',fontweight='bold')
plt.ylabel('No of Passengers',fontweight='bold')
plt.ylim([0,40])
plt.title('Age distribution based on survival',fontweight='bold')
# plt.text(survival_data['Age'].mean()+13,37,
#          'Mean: {}'.format(round(survival_data['Age'].mean(),2)),
#          horizontalalignment='center',
#      verticalalignment='center',color='r')
# plt.grid(True)
# plt.show()
#
survived_stats = survival_data['Age'].describe()

# print(survived_stats)

alive_data = data[data['Survived'] == 1]
died_data = data[data['Survived'] == 0]


plt.figure(6)
alive_data['Age'].plot.hist(bins=range(100),color='red',  edgecolor='black', linewidth=1.0, alpha=0.7)
plt.xlabel('Age',fontweight='bold')
plt.ylabel('No of Passengers',fontweight='bold')
plt.ylim([0,40])
plt.title('Survived people Age distribution',fontweight='bold')
# plt.show()

plt.figure(7)
died_data['Age'].plot.hist(bins=range(100),color='m',  edgecolor='black', linewidth=1.0, alpha=0.7)
plt.xlabel('Age',fontweight='bold')
plt.ylabel('No of Passengers',fontweight='bold')
plt.ylim([0,40])
plt.title('Dead people Age distribution',fontweight='bold')
# plt.show()


###---------------------------------------------------------------###

age_data = data.groupby('Age',as_index=False)

age_mean_data = age_data.mean()

# print(age_mean_data)

age_list = age_mean_data['Age'].tolist()

no_passengers = age_data.count()['Name']
print(no_passengers)

# sys.exit()

plt.figure(8)
scatter_ex = plt.scatter(age_mean_data['Age'],age_mean_data['Survived'],s=80,alpha=0.9,c=no_passengers,cmap='RdYlGn',edgecolors='none',vmin=0,vmax=30)
plt.colorbar(scatter_ex,label='No. of passengers')
plt.title('Effect of Age on Survival rate')
plt.xlabel('Age')
plt.ylabel('Survival Rate')
# plt.show()
