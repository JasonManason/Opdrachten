#Jason de Mey, Klas AI V1B, Blok C, Structured Programming

#===============================================Opdracht 1, Pyramide:===================================================
def pyramid():
    '''Vraagt naar de grootte van de te maken pyramide en creëert deze in twee richtingen. (Naar links en rechts)
    Via for-loops.'''
    try:
        size = int(input('How big do you want the pyramid to be?\n'))
        direction = input('Do you want it to face to the left or to the right?\nType "Left" or "Right": ').capitalize()

        if direction == 'Right': #<=pyramid facing right
            for j in range(1, size + 1): #<= upper half
                print('*' * j)

            for i in range(size - 1, 0, -1): #<= lower half
                print('*' * i)

        elif direction == 'Left': # <= reversed pyramid
            for i in range(size, 0, -1):
                print(i * ' ' + ((size + 1) - i) * '*') #<= upper half

            for i in range(size - 1, 0, -1):
                print(((size + 1) - i) * ' ' + (i * '*')) #<= lower half

    except ValueError:
        print('Value error, please check and replace the input values.')


def while_pyramid():
    '''Vraagt naar de grootte van de te maken pyramide en creëert deze in twee richtingen. (Naar links en rechts)
    Via while-loops.'''
    try:
        size = int(input('How big do you want the pyramid to be?\n'))
        direction = input('Do you want it to face to the left or to the right?\nType "Left" or "Right": ').capitalize()
        i, j = 1, 1

        if direction == 'Right': #<=pyramid facing right
            while i <= size:
                print('*' * i) #<= upper half
                i += 1
            while j <= size:
                print('*' * (size - j)) #<= lower half
                j += 1

        elif direction == 'Left': # <= reversed pyramid
            while i <= size:
                print(((size + 1) - i) * ' ' + (i * '*')) #<= upper half
                i += 1
            while j <= size:
                print((j + 1) * ' ' + (size - j) * '*') #<= lower half
                j += 1

    except ValueError:
        print('Value error, please check and replace the input values.')


def choose_loop():
    '''Vraagt welke manier van loopen je wilt gebruiken voor de pyramide en roept dan de juiste functie aan.'''
    option = input('Choose a way to loop.\nType "While" or "For".\n').capitalize()

    if option == 'While':
        while_pyramid()
    elif option == 'For':
        pyramid()
    else:
        print('Please run the program again and type in a valid option.')

#choose_loop() # <= comment uit om meteen andere opdracht te runnen.


#================================================Opdracht 2, Tekstcheck:================================================
def compare_string_characters():
    '''Geeft eerste index terug waarop twee strings een verschillende waarde hebben. Spaties tellen niet mee.'''
    text_1 = input('Please enter a sentence.\n').capitalize()
    text_2 = input('Please enter another sentence to compare with the last.\n').capitalize()

    for i in text_1:
        if text_1.index(i) == text_2.index(i):
            index = (text_1.index(i) + 1)

    return print(f'The difference is in character {index}.')

#print(compare_string_characters()) # <= comment uit om meteen andere opdracht te runnen.


#================================================Opdracht 3, Lijstcheck:================================================
def count():
    '''Berekent hoevaak getal x in een lijst voorkomt.'''


#================================================Opdracht 4, Palindroom:================================================

def palindroom(woord):
    '''Checkt of input een palindroom is d.m.v. string slicing.'''
    return woord == woord[::-1] # => -1 = stapgrootte vanaf achteraan

#print(palindroom('lepel')) #<= comment uit om meteen andere opdracht te runnen.