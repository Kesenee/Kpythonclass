keep_going = 'y'

while keep_going =='y':
    sales = float(input('Enter the amount of sales:'))
    comm_rate = float(input('Enter the commission rate: '))

    commission = sales * comm_rate

    print('The commission is $' , \
    format(commission, ',.2f'), sep = '')

    keep_going = input('Do you want to calculate another' + \
                        'commission (Enter y for yes): ')
    

retail_price  = 'x'
while retail_price == 'x':
    wholesale_cost = float(input('Enter the amount of price:'))
    retail_price = wholesale_cost * 2.5
    print('retail_price: is $' , )
