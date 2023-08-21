def main() :
    
    total = 0.0

    try:
        infile = open('sale_data.txt', 'r')

        for line in infile:
            amount = float(line)
            total += amount

        infile.close()

        print(format(total, '2.f'))

    except IOError:
        print('An error occured trying to read the file.')

    except ValueError:
        print('Non-numeric data found in the file.')

    except:
        print('An error occured.')

main()