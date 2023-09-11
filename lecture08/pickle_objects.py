import pickle

def main():
    again = 'y'

    output_file = open('info.dat', 'wb')

    while again.lower() == 'y' :
        # Get data about a person and save it.
        save_data(output_file)

        again = input('Enter more data? (y/n): ')

    output_file.close()
