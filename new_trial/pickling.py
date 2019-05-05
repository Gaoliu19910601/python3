import pickle

dict1 = {'a':400,'b':200,'c':100}

list1 = [100,200,400]

print(dict1)
print(list1)

output = open('save.pkl','wb')

pickle.dump(dict1,output,pickle.HIGHEST_PROTOCOL)
pickle.dump(list1,output,pickle.HIGHEST_PROTOCOL)

output.close()

print('-----------')

inputFile = open('save.pkl','rb')

amar_dict2 = pickle.load(inputFile)
amar_list2 = pickle.load(inputFile)

print(amar_dict2)
print(amar_list2)