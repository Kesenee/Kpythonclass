phonebook = {'Anirach': '777-1111', 'MIckey': '777-2222', 'Donald': '777-3333'}

print(phonebook)

print(phonebook['MIckey'])
print(phonebook.get('Donald'))

key = 'Pluto'
if key in phonebook:
    print(phonebook['Pluto'])
else :
    print(key + ' not in phonebook')

phonebook['Simpson'] = '777-4567'
phonebook['Pluto'] = '777-4444'
phonebook['Mickey'] = '777-2122'

print(phonebook)

del phonebook['Simpson']
print(phonebook)