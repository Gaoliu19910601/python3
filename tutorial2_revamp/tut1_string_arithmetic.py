
'''--------------------- STRING OPERATIONS--------------------------------'''

message = 'Hello World'
message2 = "amar's world"

print(message2)

print(len(message2)) # finds the length of the string

print(message[0:3]) # prints particular spaces of a string

print(message.lower()) # lowercase print

print(message.upper()) # upper case print

print(message.count('l')) # counts the no. of given arg in the variable

print(message.find('World')) # finds the index of the word in the variable

print(message.find('UNiverse')) # returns -1 if it doesnt find any

# Replacing words in a variable
new_message = message.replace('World','Universe')
print(new_message)


#------------------------- concatenating-----------------------------
greeting = 'Hey'
name = 'Amar'
new_message2 = greeting + ', ' + name + '. Welcome'
print(new_message2)


# This is more easy to read and elegant
new_message3 = '{}, {}. Welcome!'.format(greeting, name)
print(new_message3)
#-----------------------------------------------------------------

# help function useful to check the available function calls
print(help(str.replace)) # to check the replace function and its use


# dir function gives the attributes of the variable
#print(dir(name))


'''---------------------------ARITHMETIC OPERATIONS--------------------------------'''

print(3 ** 2) # exponent
print(5 // 2) # floor division
print(3 % 2) # modulus operator


num = 1
num +=1
print(num)

print(abs(-3)) # absolute value of a number

print(round(3.75)) # rounding of a float number
print(round(3.75,1)) # round to first digit after the decimel

print(num > 3.8) # conditional check true or false

num1 = '100'
num2 = '200'
print(num1 + num2)
print(int(num1) + int(num2)) # converting str to int to add the value


'''------------------------------------------------------------------------------'''