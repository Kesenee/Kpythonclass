NUM_EMPLOYEES = 6

def main() :
    hours = [0]

    for index in range(NUM_EMPLOYEES) :
        print('Enter the hours worked by employees', \
              index + 1, ': ', sep='', end='')
        hours[index] = float(input())

    pay_rate = float(input('Enter the hourly pay rate'))

    for index in range(NUM_EMPLOYEES) :
        gross_pay = hours[index] * pay_rate
        print('Gross pay for eployee ', index + 1, ':$', \
              format(gross_pay, ',.2f'), sep='')
        
main ()