heroes = ['Ironman', 'Thor', 'Hulk', 'Superman', 'Spiderman']
h3 = ['Dr. Strange', 'Cpt. America', 'Black Panther', 'Ant Man']

print(heroes + h3)

newheroes = heroes
newheroes[0] = 'Wonder Woman'
print(heroes)

heroes.insert(heroes.index('Thor'), h3[1])
print(heroes)

heroes.remove('Superman')
print(heroes)

h4 = heroes + h3
h4.sort()
print(h4)

h4.reverse()
print(h4)



