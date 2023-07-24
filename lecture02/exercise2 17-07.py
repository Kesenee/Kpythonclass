score_1 = int(input('Enter the score for test 1:'))
score_2 = int(input('Enter the score for test 2:'))
score_3 = int(input('Enter the score for test 3:'))
average = (score_1 + score_2 + score_3)/3
print('the average score is ',average )
if average > 95:
    print('Congratulation')
    print('that is a great average')