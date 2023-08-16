def main() :
    num_emps = int(input('How many employee records do you want to create? :3 '  + \
                         'Enter the data fr employee #1 '))
    
    emp_file = open('employees.txt', 'r')

    for count in range(3, num_emps + 3) :

        print('Enter data for employee #', count, sep='')
        name = input('Name: ')
        id_num = input('ID number: ')
        dept = input('Department: ')

        emp_file.write(name + '\n')
        emp_file.write(id_num + '\n')
        emp_file.write(dept + '\n')

        print()

        emp_file.close()
        print('Employee record written to employees.txt.')

main()



