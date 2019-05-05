import numpy as np
import pandas as pd

amar = pd.Series(np.arange(1,101))
deep = pd.Series(np.arange(101,201))

amar1 = pd.DataFrame({'amar':amar,'deep':deep})

# print(amar1)
# print(amar1.head())
# print(amar1.tail())

odd_even = pd.DataFrame({'even':pd.Series(np.arange(0,100,2)),
                         'odd':pd.Series(np.arange(1,100,2))})

# print(odd_even.sum())

sample1 = pd.DataFrame(np.random.rand(4,5),columns=['col-1','col-2','col-3','col-4','col-5'],
                       index=['row-1','row-2','row-3','row-4'])


# Not sure why we need this rather than print(sample1)
# for key,values in sample1.iteritems():
#     print('KEY:',key)
#     print('VALUE:',values)

# print(sample1)

#-----------A really good and comprehensive Example-------------#

world_cup = {'Team':['West Indies','West Indies','India','Australia','Pakistan','Sri Lanka','Australia','Australia','Australia','India','Australia'],
             'Rank':[7,7,2,1,6,4,1,1,1,2,1],
             'Year':[1975,1979,1983,1987,1992,1996,1999,2003,2007,2011,2015],
             'Points': [865, 395, 586,452,567,342,875,234,357,144,647]}

chokers = {'Team':['Zimbabwe','South Africa','Nepal'],
           'Rank':[5,4,3],
           'Year':[1998,1983,1994],
           'Points':[865,395,586],
           'High':[256,220,265]}

wc = pd.DataFrame(world_cup)
chok = pd.DataFrame(chokers)

print(wc.groupby(['Team','Rank']).groups)

# print(wc)

# print(wc.groupby('Team').get_group('India'))
#
# for name,group in wc.groupby(['Team']):
#     print('Group Name: {}'.format(name))
#     print(group)
#     print("===================================")

# total = pd.concat([wc,chok],sort=False)

# print(total)


#------------------ Another Example -------------------#

a = pd.DataFrame({'key':['K0','K1','K2','K3','K4'],
                     'A':['A0','A1','A2','A3','A4'],
                     'B':['B0','B1','B2','B3','B4']})


b = pd.DataFrame({'key':['K0','K1','K2','K3','K6'],
                     'C':['C0','C1','C2','C3','C6'],
                     'D':['D0','D1','D2','D3','D6']})

# print(pd.concat([a,b],axis=0))

# print(pd.merge(a,b,on='key',how='left'))
# print(pd.merge(a,b,on='key',how='right'))
# print(pd.merge(a,b,on='key',how='outer'))
# print(pd.merge(a,b,on='key',how='inner'))

# print(pd.merge(b,a,on='key',how='left'))
# print(pd.merge(b,a,on='key',how='right'))
# print(pd.merge(b,a,on='key',how='outer'))
# print(pd.merge(b,a,on='key',how='inner'))