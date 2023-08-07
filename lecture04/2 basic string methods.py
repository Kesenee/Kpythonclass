filename = input('Enter the filename :')
if filename.endswith('.txt') :
    print('That is name of a text file.')
elif filename.endswith ('.py') :
    print('That is the name of a python source file')
elif filename.endswith('.doc') :
    print('That is the name of a word processing document.')
else:
    print('Unknow file type.')

