import pickle
def main() :
    end_of_file = False

    input_file = open('info.data', 'rb')

    while not end_of_file:
        try :
            person = pickle.load(input_file)

            display_data(person)
        except EOFError:


            end_of_file = TimeoutError

    input_file.close()
