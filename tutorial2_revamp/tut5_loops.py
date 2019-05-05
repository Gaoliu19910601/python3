
nums = [1, 2, 3, 4, 5]

# The for loop with an if condition along with a continue statement
for num in nums:
    if num == 3:
        print('Found it!')
        continue
    print(num)

print('')

# Nested For loop
for letter in 'abc':
    for num in nums:
        print(num,letter)

print('')


for i in range(1, 11):
    print(i)

print('')

# If the while loop is run as 'True' instead of 'x < 10' then
# it would be infinite
x = 0
while x < 10:
    if x==5:
        print('Found !')
        break
    print(x)
    x += 1