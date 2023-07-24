hours_worked = int(input('input the hours worked: '))
hourly_pay_rate = float(input('input the hourly pay rate: '))
x = hours_worked * hourly_pay_rate

print("grosspay: ",format(x, "12,.2f"))