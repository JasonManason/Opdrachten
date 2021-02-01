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
def count(lst, x):
    '''Berekent hoevaak getal x in een lijst voorkomt.'''
    return lst.count(x)

#print(count([1, -12, 0, 4, 33, 600, 43, -16, 4], 4)) # <= comment uit om meteen andere opdracht te runnen.


def verschil(lst):
    '''Berekent grootste verschil tussen 2 opeenvolgende getallen in lst.'''
    new_lst = []
    for i in range(0, len(lst)):
        verschil = lst[i] - lst[i - 1]

        new_lst.append(verschil)

    return max(new_lst)

#print(verschil([1, -12, 0, 4, 33, 600, 43, -16, 4]))# <= comment uit om meteen andere opdracht te runnen.


def binair(lst):
    '''Checkt of aantal meegegeven eenen groter is dan het aantal meegegeven aantal nullen,
    zolang er niet meer dan 12 nullen zijn. Returnt True/False.'''
    if lst.count(0) >= lst.count(1) or lst.count(0) >= 12:
        return False
    else:
        return True

#print(binair([0,1,1,1,1,0,0,1,1,1,0,0,1,0,1])) # <= comment uit om meteen andere opdracht te runnen.


#================================================Opdracht 4, Palindroom:================================================
def palindroom(woord):
    '''Checkt of input een palindroom is d.m.v. string slicing.'''
    return woord == woord[::-1] # => -1 = stapgrootte vanaf achteraan

#print(palindroom('lepel')) # => comment uit om meteen andere opdracht te runnen.


#=================================================Opdracht 5, Sorteren:=================================================
def sorteren(lst):
    '''Sorteert lijst met cijfers.'''
    lst_sorted = []
    for i in lst:
        lst_sorted.append(i)

    for item in lst_sorted:
        position = lst_sorted.index(item)

        while position > 0:  # anders begin je weer achteraan list.

            if item < lst_sorted[position - 1]:
                lst_sorted[position - 1], lst_sorted[position] = lst_sorted[position], lst_sorted[
                    position - 1]  # swap variabelen
            position -= 1

    return lst_sorted

#print(sorteren([1, 6, -12, 498, 6, 8, 4, 13, 55])) # => comment uit om meteen andere opdracht te runnen.


#================================================Opdracht 6, Gemiddelde:================================================
def gemiddelde(lst):
    '''Berekent gemiddelde waarde van input lijst met cijfers.'''
    return sum(lst) / len(lst)

#print(gemiddelde([1, 6, -12, 498, 6, 8, 4, 13, 55])) # <= comment uit om meteen andere opdracht te runnen.


def gemiddelde_lists(lst):
    '''Berekent gemiddelde van input lijst met lijsten met cijfers.'''
    new = []
    for l in lst:
        new.append(gemiddelde(l))
    new = gemiddelde(new)

    return new

#print(gemiddelde_lists([[1, 6, -12, 498, 6, 8, 4, 13, 55], [0 ,8 ,34 ,12 ,-45 ,89 ,-16], [-10 ,-17 ,-1 ,4 ,7 ,12]])) # <= comment uit om meteen andere opdracht te runnen.


#==================================================Opdracht 7, Random:==================================================
def willekeurig():
    '''Laat gebruiker gokken uit lijst met cijfers tot antwoord goed is. Antwoord is willekeurig.'''
    #lst = [] #<= willekeurige cijfers in lst

    #<= user input()?

    #check if input in lst: return True of False

#willekeurig()


#================================================Opdracht 10, Fibonaci:=================================================
def fibonacci(n, v0=0, v1=1):
    '''Geeft de index terug van "fn" in de Fibonacci van "n".'''
    #return fibonacci(n - 1) + fibonacci(n - 2) if n > 1 else (0, 1) [n] # <= roept zichzelf 2x aan = slomer, creeert boom.

    return fibonacci(n - 1, v1, v0 + v1) if n > 1 else (v0, v1)[n] # <= tot "n" klein genoeg is

#print(fibonacci(9)) # <= comment uit om meteen andere opdracht te runnen.