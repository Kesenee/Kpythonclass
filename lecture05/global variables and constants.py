number = 0

def main() :
    global number
    number = int(input('Enter a nmber: '))
    show_number()

def show_number() :
    print('The number you entered is', number)

main()