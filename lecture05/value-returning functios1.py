def get_name() :
    first = input('Enter your first name: ')
    last = input('Enter your last name: ')
    return first, last
first_name, last_name = get_name()
print('first name :', first_name, 'last name :', last_name)