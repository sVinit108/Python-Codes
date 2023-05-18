def readfile(filename):
    try:
        with open(f'{filename}','r') as f:
            print(f.read())
    except FileNotFoundError as e:
        print('Sorry')
        print(f'The File {filename} not found')
readfile('1.txt')
readfile('2.txt')
readfile('3.txt')
readfile('4.txt')