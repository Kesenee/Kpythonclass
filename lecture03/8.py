# Get a test score.
score = int(input('Entera test score:'))
#make sure it is not less than 0 or greater than 100.
while score < 0 or score > 100 :
    print('Enter: The score cannot be negative')
    print('or greater than 100.')
    score = int(input('Enter the correct score:'))
