# get the user's name , age, and icome.
name =input('What ir your name? ')
age = int(input('What is your age? '))
income = float(input('What ie your income? '))

# display the data
print('Here is the data you entered')
print('Name:' ,name)
print('Age:' ,age)
print('Income:' ,format(income, '12,.2f'))