import doctest


def test_chapter1_interactive_shell():
    """
    Page XX:
    >>> 2 + 2
    4
    >>>

    >>> 2
    2

    Page XX:
    >>> 2 + 3 * 6
    20
    >>> (2 + 3) * 6
    30
    >>> 48565878 * 578453
    28093077826734
    >>> 2 ** 8
    256
    >>> 23 / 7
    3.2857142857142856
    >>> 23 // 7
    3
    >>> 23 % 7
    2
    >>> 2 + 2
    4
    >>> (5 - 1) * ((7 + 1) / (3 - 1))
    16.0

    Page XX:
    >>> spam = 40
    >>> spam
    40
    >>> eggs = 2
    >>> spam + eggs
    42
    >>> spam + eggs + spam
    82
    >>> spam = spam + 2
    >>> spam
    42

    >>> spam = 'Hello'
    >>> spam
    'Hello'
    >>> spam = 'Goodbye'
    >>> spam
    'Goodbye'

    Page XX:
    >>> str(0)
    '0'
    >>> str(-3.14)
    '-3.14'
    >>> int('42')
    42
    >>> int('-99')
    -99
    >>> int(1.25)
    1
    >>> int(1.99)
    1
    >>> float('3.14')
    3.14
    >>> float(10)
    10.0

    Page XX:
    >>> 42 == '42'
    False
    >>> 42 == 42.0
    True
    >>> 42.0 == 0042.000
    True

    Page XX:
    >>> type(42)
    <class 'int'>
    >>> type(42.0)
    <class 'float'>
    >>> type('forty two')
    <class 'str'>
    >>> name = 'Zophie'
    >>> type(name) # The name variable has a value of the string type.
    <class 'str'>
    >>> type(len(name)) # The len() function returns integer values.
    <class 'int'>

    >>> round(3.14)
    3
    >>> round(7.7)
    8
    >>> round(-2.2)
    -2

    >>> round(3.14, 1)
    3.1
    >>> round(7.7777, 3)
    7.778

    >>> abs(25)
    25
    >>> abs(-25)
    25
    >>> abs(-3.14)
    3.14
    >>> abs(0)
    0
    """

    # No pytest tests for chapter 1

def test_chapter2_if_else():
    """
    Page XX:

    >>> spam = True
    >>> spam
    True


    >>> 42 == 42
    True
    >>> 42 == 99
    False
    >>> 2 != 3
    True
    >>> 2 != 2
    False

    >>> 'hello' == 'hello'
    True
    >>> 'hello' == 'Hello'
    False
    >>> 'dog' != 'cat'
    True
    >>> True == True
    True
    >>> True != False
    True
    >>> 42 == 42.0
    True
    >>> 42 == '42'
    False

    >>> 42 < 100
    True
    >>> 42 > 100
    False
    >>> 42 < 42
    False
    >>> eggs = 42
    >>> eggs <= 42
    True
    >>> my_age = 29
    >>> my_age >= 10
    True

    >>> True and True
    True
    >>> True and False
    False

    >>> False or True
    True
    >>> False or False
    False

    >>> not True
    False
    >>> not not not not True
    True

    >>> (4 < 5) and (5 < 6)
    True
    >>> (4 < 5) and (9 < 6)
    False
    >>> (1 == 2) or (2 == 2)
    True

    >>> spam = 4
    >>> 2 + 2 == spam and not 2 + 2 == (spam + 1) and 2 * 2 == 2 + 2
    True
    """

    # TODO: Test the "hard drive capacity liar" program.

def test_chapter3_loops():
    """
    Page XX:
    >>> bool(0)
    False
    >>> bool(42)
    True
    >>> bool('Hello')
    True
    >>> bool('')
    False


    """

    # TODO: Test "An Annoying while Loop"

    # TODO: Test "A Short Program: Guess the Number"

    # TODO: Test "A Short Program: Rock, Paper, Scissors"


def test_chapter4_functions():
    """
    >>> raise Exception('This is the error message.')
    Traceback (most recent call last):
      File "<pyshell#191>", line 1, in <module>
        raise Exception('This is the error message.')
    Exception: This is the error message.
    """

    # NOTE: The example code in this chapter is as programs, not interactive shell examples.

    # TODO: Test "A Short Program: Zigzag"

    # TODO: Test "A Short Program: Spike"

def test_chapter5_debugging():
    """
>>> def box_print(symbol, width, height):
...     if len(symbol) != 1:
...         raise Exception('Symbol must be a single character string.')
...     if width <= 2:
...         raise Exception('Width must be greater than 2.')
...     if height <= 2:
...         raise Exception('Height must be greater than 2.')
...     print(symbol * width)
...     for i in range(height - 2):
...         print(symbol + (' ' * (width - 2)) + symbol)
...     print(symbol * width)

    >>> try:
    ...     box_print('*', 4, 4)
    ...     box_print('O', 20, 5)
    ...     box_print('x', 1, 3)
    ... except Exception as err:
    ...     print('An exception happened: ' + str(err))
    ****
    *  *
    *  *
    ****
    OOOOOOOOOOOOOOOOOOOO
    O                  O
    O                  O
    O                  O
    OOOOOOOOOOOOOOOOOOOO
    An exception happened: Width must be greater than 2.

    >>> try:
    ...     box_print('ZZ', 3, 3)
    ... except Exception as err:
    ...     print('An exception happened: ' + str(err))
    An exception happened: Symbol must be a single character string.


    >>> ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
    >>> ages.sort()
    >>> ages
    [15, 17, 22, 26, 47, 54, 57, 73, 80, 92]
    >>> assert ages[0] <= ages[-1] # Assert that the first age is <= the last age.

    >>> ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
    >>> ages.reverse()
    >>> ages
    [73, 47, 80, 17, 15, 22, 54, 92, 57, 26]
    >>> assert ages[0] <= ages[-1] # Assert that the first age is <= the last age.
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AssertionError



    """

    # TODO: Test "Debugging an Addition Program"


def test_chapter6_lists():
    """
    >>> [1, 2, 3] # A list of three integers.
    [1, 2, 3]
    >>> ['cat', 'bat', 'rat', 'elephant'] # A list of four strings.
    ['cat', 'bat', 'rat', 'elephant']
    >>> ['hello', 3.1415, True, None, 42] # A list of several values.
    ['hello', 3.1415, True, None, 42]
    >>> spam = ['cat', 'bat', 'rat', 'elephant']
    >>> spam
    ['cat', 'bat', 'rat', 'elephant']

    >>> spam = ['cat', 'bat', 'rat', 'elephant']
    >>> spam[0]
    'cat'
    >>> spam[1]
    'bat'
    >>> spam[2]
    'rat'
    >>> spam[3]
    'elephant'
    >>> ['cat', 'bat', 'rat', 'elephant'][3]
    'elephant'
    >>> 'Hello, ' + spam[0]
    'Hello, cat'
    >>> 'The ' + spam[1] + ' ate the ' + spam[0] + '.'
    'The bat ate the cat.'

    >>> spam = ['cat', 'bat', 'rat', 'elephant']
    >>> spam[10000]
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
            spam[10000]
    IndexError: list index out of range

    >>> spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
    >>> spam[0]
    ['cat', 'bat']
    >>> spam[0][1]
    'bat'
    >>> spam[1][4]
    50

    >>> spam = ['cat', 'bat', 'rat', 'elephant']
    >>> spam[-1] # Last index.
    'elephant'
    >>> spam[-3] # Third to last index.
    'bat'
    >>> 'The ' + spam[-1] + ' is afraid of the ' + spam[-3] + '.'
    'The elephant is afraid of the bat.'

    >>> spam = ['cat', 'bat', 'rat', 'elephant']
    >>> spam[0:4]
    ['cat', 'bat', 'rat', 'elephant']
    >>> spam[1:3]
    ['bat', 'rat']
    >>> spam[0:-1]
    ['cat', 'bat', 'rat']

    >>> spam = ['cat', 'bat', 'rat', 'elephant']
    >>> spam[:2]
    ['cat', 'bat']
    >>> spam[1:]
    ['bat', 'rat', 'elephant']
    >>> spam[:]
    ['cat', 'bat', 'rat', 'elephant']

    >>> spam = ['cat', 'dog', 'moose']
    >>> len(spam)
    3

    >>> spam = ['cat', 'bat', 'rat', 'elephant']
    >>> spam[1] = 'aardvark'
    >>> spam
    ['cat', 'aardvark', 'rat', 'elephant']
    >>> spam[2] = spam[1]
    >>> spam
    ['cat', 'aardvark', 'aardvark', 'elephant']
    >>> spam[-1] = 12345
    >>> spam
    ['cat', 'aardvark', 'aardvark', 12345]

    >>> [1, 2, 3] + ['A', 'B', 'C']
    [1, 2, 3, 'A', 'B', 'C']
    >>> ['X', 'Y', 'Z'] * 3
    ['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']
    >>> spam = [1, 2, 3]
    >>> spam = spam + ['A', 'B', 'C']
    >>> spam
    [1, 2, 3, 'A', 'B', 'C']


    >>> spam = ['cat', 'bat', 'rat', 'elephant']
    >>> del spam[2]
    >>> spam
    ['cat', 'bat', 'elephant']
    >>> del spam[2]
    >>> spam
    ['cat', 'bat']


    >>> supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
    >>> for i in range(len(supplies)):
    ...  print('Index ' + str(i) + ' in supplies is: ' + supplies[i])
    ...
    Index 0 in supplies is: pens
    Index 1 in supplies is: staplers
    Index 2 in supplies is: flamethrowers
    Index 3 in supplies is: binders


    >>> 'howdy' in ['hello', 'hi', 'howdy', 'heyas']
    True
    >>> spam = ['hello', 'hi', 'howdy', 'heyas']
    >>> 'cat' in spam
    False
    >>> 'howdy' not in spam
    False
    >>> 'cat' not in spam
    True


    >>> cat = ['fat', 'gray', 'loud']
    >>> size = cat[0]
    >>> color = cat[1]
    >>> disposition = cat[2]


    >>> cat = ['fat', 'gray', 'loud']
    >>> size, color, disposition = cat


    >>> cat = ['fat', 'gray', 'loud']
    >>> size, color, disposition, name = cat
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
        size, color, disposition, name = cat
    ValueError: not enough values to unpack (expected 4, got 3)

    >>> supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
    >>> for index, item in enumerate(supplies):
    ...  print('Index ' + str(index) + ' in supplies is: ' + item)
    ...
    Index 0 in supplies is: pens
    Index 1 in supplies is: staplers
    Index 2 in supplies is: flamethrowers
    Index 3 in supplies is: binders

    >>> spam = 42
    >>> spam = spam + 1
    >>> spam
    43

    >>> spam = 42
    >>> spam += 1
    >>> spam
    43

    >>> spam = 'Hello,'
    >>> spam += ' world!' # Same as spam = spam + 'world!'
    >>> spam
    'Hello, world!'
    >>> bacon = ['Zophie']
    >>> bacon *= 3 # Same as bacon = bacon * 3
    >>> bacon
    ['Zophie', 'Zophie', 'Zophie']


    >>> spam = ['hello', 'hi', 'howdy', 'heyas']
    >>> spam.index('hello')
    0
    >>> spam.index('heyas')
    3
    >>> spam.index('howdy howdy howdy')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
        spam.index('howdy howdy howdy')
    ValueError: 'howdy howdy howdy' is not in list


    >>> spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
    >>> spam.index('Pooka')
    1


    >>> spam = ['cat', 'dog', 'bat']
    >>> spam.append('moose')
    >>> spam
    ['cat', 'dog', 'bat', 'moose']


    >>> spam = ['cat', 'dog', 'bat']
    >>> spam.insert(1, 'chicken')
    >>> spam
    ['cat', 'chicken', 'dog', 'bat']

    >>> eggs = 'hello'
    >>> eggs.append('world')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
        eggs.append('world')
    AttributeError: 'str' object has no attribute 'append'
    >>> bacon = 42
    >>> bacon.insert(1, 'world')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
        bacon.insert(1, 'world')
    AttributeError: 'int' object has no attribute 'insert'


    >>> spam = ['cat', 'bat', 'rat', 'elephant']
    >>> spam.remove('bat')
    >>> spam
    ['cat', 'rat', 'elephant']


    >>> spam = ['cat', 'bat', 'rat', 'elephant']
    >>> spam.remove('chicken')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
        spam.remove('chicken')
    ValueError: list.remove(x): x not in list


    >>> spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
    >>> spam.remove('cat')
    >>> spam
    ['bat', 'rat', 'cat', 'hat', 'cat']

    >>> spam = [2, 5, 3.14, 1, -7]
    >>> spam.sort()
    >>> spam
    [-7, 1, 2, 3.14, 5]
    >>> spam = ['Ants', 'Cats', 'Dogs', 'Badgers', 'Elephants']
    >>> spam.sort()
    >>> spam
    ['Ants', 'Badgers', 'Cats', 'Dogs', 'Elephants']

    >>> spam.sort(reverse=True)
    >>> spam
    ['Elephants', 'Dogs', 'Cats', 'Badgers', 'Ants']

    >>> spam = [1, 3, 2, 4, 'Alice', 'Bob']
    >>> spam.sort()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
        spam.sort()
    TypeError: '<' not supported between instances of 'str' and 'int'

    >>> spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
    >>> spam.sort()
    >>> spam
    ['Alice', 'Bob', 'Carol', 'ants', 'badgers', 'cats']

    >>> spam = ['a', 'z', 'A', 'Z']
    >>> spam.sort(key=str.lower)
    >>> spam
    ['a', 'A', 'z', 'Z']

    >>> spam = ['cat', 'dog', 'moose']
    >>> spam.reverse()
    >>> spam
    ['moose', 'dog', 'cat']


    >>> spam = ['apples',
    ... 'oranges',
    ... 'bananas',
    ... 'cats']
    >>> print(spam[0]) # prints apples
    apples



    >>> spam = ['cat', 'dog']
    >>> if spam[0] == 'cat':
    ...  print('A cat is the first item.')
    ... else:
    ...  print('The first item is not a cat.')
    ...
    A cat is the first item.

    >>> spam = []
    >>> if len(spam) > 0 and spam[0] == 'cat':
    ...  print('A cat is the first item.')
    ... else:
    ...  print('The first item is not a cat.')
    ...
    The first item is not a cat.


    >>> name = 'Zophie'
    >>> name[0]
    'Z'
    >>> name[-2]
    'i'
    >>> name[0:4]
    'Zoph'
    >>> 'Zo' in name
    True
    >>> 'z' in name
    False
    >>> 'p' not in name
    False
    >>> for i in name:
    ...  print('* * * ' + i + ' * * *')
    ...
    * * * Z * * *
    * * * o * * *
    * * * p * * *
    * * * h * * *
    * * * i * * *
    * * * e * * *


    >>> name = 'Zophie a cat'
    >>> name[7] = 'the'
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
        name[7] = 'the'
    TypeError: 'str' object does not support item assignment

    >>> name = 'Zophie a cat'
    >>> new_name = name[0:7] + 'the' + name[8:12]
    >>> name
    'Zophie a cat'
    >>> new_name
    'Zophie the cat'

    >>> eggs = ['A', 'B', 'C']
    >>> eggs = [ 'x', 'y', 'z']
    >>> eggs
    ['x', 'y', 'z']

    >>> eggs = ['A', 'B', 'C']
    >>> del eggs[2]
    >>> del eggs[1]
    >>> del eggs[0]
    >>> eggs.append('x')
    >>> eggs.append('y')
    >>> eggs.append('z')
    >>> eggs
    ['x', 'y', 'z']

    >>> eggs = ('hello', 42, 0.5)
    >>> eggs[0]
    'hello'
    >>> eggs[1:3]
    (42, 0.5)
    >>> len(eggs)
    3

    >>> eggs = ('hello', 42, 0.5)
    >>> eggs[1] = 99
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
        eggs[1] = 99
    TypeError: 'tuple' object does not support item assignment

    >>> type(('hello',))
    <class 'tuple'>
    >>> type(('hello'))
    <class 'str'>

    >>> tuple(['cat', 'dog', 5])
    ('cat', 'dog', 5)
    >>> list(('cat', 'dog', 5))
    ['cat', 'dog', 5]
    >>> list('hello')
    ['h', 'e', 'l', 'l', 'o']

    >>> spam = 42
    >>> eggs = spam
    >>> spam = 100
    >>> spam
    100
    >>> eggs
    42

    >>> spam = [0, 1, 2, 3]
    >>> eggs = spam # The reference, not the list, is being copied.
    >>> eggs[1] = 'Hello!' # This changes the list value.
    >>> spam
    [0, 'Hello!', 2, 3]
    >>> eggs # The cheese variable refers to the same list.
    [0, 'Hello!', 2, 3]


    >>> def eggs(some_parameter):
    ...   some_parameter.append('Hello')
    ...
    >>> spam = [1, 2, 3]
    >>> eggs(spam)
    >>> print(spam) # Prints [1, 2, 3, 'Hello']
    [1, 2, 3, 'Hello']


    >>> import copy
    >>> spam = ['A', 'B', 'C']
    >>> cheese = copy.copy(spam) # This creates a duplicate copy of the list.
    >>> cheese[1] = 42 # Changes cheese.
    >>> spam # spam is unchanged.
    ['A', 'B', 'C']
    >>> cheese # cheese is changed.
    ['A', 42, 'C']


    """

    # TODO: Test the "Working with Lists" section's cat name list eample.

    # TODO: Test random functions

    # TODO: Test "A Short Program: Magic 8 Ball with a List"

    # TODO: Test "A Short Program: The Matrix Screensaver"

def test_chapter7_dictionaries():
    """
    >>> my_cat = {'size': 'fat', 'color': 'gray', 'age': 17}
    >>> my_cat['size']
    'fat'
    >>> 'My cat has ' + my_cat['color'] + ' fur.'
    'My cat has gray fur.'

    >>> spam = {12345: 'Luggage Combination', 42: 'The Answer'}
    >>> spam[12345]
    'Luggage Combination'
    >>> spam[42]
    'The Answer'
    >>> spam[0]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 0

    >>> spam = ['cats', 'dogs', 'moose']
    >>> bacon = ['dogs', 'moose', 'cats']
    >>> spam == bacon # Order of list items matters.
    False
    >>> eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
    >>> ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
    >>> eggs == ham # Order of dictionary key-values pairs doesn't matter.
    True

    >>> spam = {'name': 'Zophie', 'age': 7}
    >>> spam['color']
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
        spam['color']
    KeyError: 'color'


    >>> spam = {'color': 'red', 'age': 42}
    >>> for v in spam.values():
    ...  print(v)
    red
    42

    >>> for k in spam.keys():
    ...  print(k)
    color
    age
    >>> 'color' in spam.keys()
    True
    >>> 'age' not in spam.keys()
    False
    >>> 'red' in spam.values()
    True
    >>> for i in spam.items():
    ...  print(i)
    ('color', 'red')
    ('age', 42)

    >>> 'color' in spam
    True
    >>> 'color' in spam.keys()
    True

    >>> spam = {'color': 'red', 'age': 42}
    >>> spam.keys() # Returns a list-like dict_keys value.
    dict_keys(['color', 'age'])
    >>> list(spam.keys()) # Returns an actual list value.
    ['color', 'age']

    >>> spam = {'color': 'red', 'age': 42}
    >>> for k, v in spam.items():
    ...  print('Key: ' + str(k) + ' Value: ' + str(v))
    ...
    Key: color Value: red
    Key: age Value: 42


    >>> picnic_items = {'apples': 5, 'cups': 2}
    >>> 'I am bringing ' + str(picnic_items.get('cups', 0)) + ' cups.'
    'I am bringing 2 cups.'
    >>> 'I am bringing ' + str(picnic_items.get('eggs', 0)) + ' eggs.'
    'I am bringing 0 eggs.'


    >>> picnic_items = {'apples': 5, 'cups': 2}
    >>> 'I am bringing ' + str(picnic_items['eggs']) + ' eggs.'
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
        'I am bringing ' + str(picnic_items['eggs']) + ' eggs.'
    KeyError: 'eggs'

    >>> spam = {'name': 'Pooka', 'age': 5}
    >>> if 'color' not in spam:
    ...   spam['color'] = 'black'
    ...
    >>>


    >>> spam = {'name': 'Pooka', 'age': 5}
    >>> spam.setdefault('color', 'black') # Sets 'color' key to 'black'.
    'black'
    >>> spam
    {'name': 'Pooka', 'age': 5, 'color': 'black'}
    >>> spam.setdefault('color', 'white') # Does nothing.
    'black'
    >>> spam
    {'name': 'Pooka', 'age': 5, 'color': 'black'}


    >>> message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
    >>> count = {}
    >>> for character in message:
    ...   count.setdefault(character, 0)
    ...   count[character] = count[character] + 1
    ...
    0
    0
    0
    0
    0
    0
    1
    1
    2
    0
    0
    0
    0
    0
    1
    3
    0
    0
    0
    0
    4
    1
    2
    0
    5
    1
    0
    6
    0
    0
    1
    2
    1
    0
    7
    3
    1
    2
    8
    2
    1
    0
    9
    1
    2
    1
    2
    0
    1
    10
    1
    1
    2
    2
    11
    2
    3
    3
    3
    1
    4
    2
    1
    12
    4
    2
    5
    4
    5
    3
    4
    3
    0
    >>> print(count)
    {'I': 1, 't': 6, ' ': 13, 'w': 2, 'a': 4, 's': 3, 'b': 1, 'r': 5, 'i': 6, 'g': 2, 'h': 3, 'c': 3, 'o': 2, 'l': 3, 'd': 3, 'y': 1, 'n': 4, 'A': 1, 'p': 1, ',': 1, 'e': 5, 'k': 2, '.': 1}



    """

    # TODO: Test "A Short Program: Interactive Chess Board Simulator"

def test_chapter8_strings():
    r"""
    NOTE: Due to the nature of string literals, this will be tricky to test as a docstring with doctest.


    >>> spam = "That is Alice's cat."

    >>> spam = 'Say hi to Bob\'s mother.'

    >>> print("Hello there!\nHow are you?\nI\'m doing fine.")
    Hello there!
    How are you?
    I'm doing fine.



    >>> print(r'The file is in C:\Users\Alice\Desktop')
    The file is in C:\Users\Alice\Desktop

    >>> print('Hello...\n\n...world!') # Without a raw string.
    Hello...
    <BLANKLINE>
    ...world!
    >>> print(r'Hello...\n\n...world!') # With a raw string.
    Hello...\n\n...world!

    print('Dear Alice,\n\nCan you feed Eve's cat this weekend?\n\nSincerely,\nBob')
    Dear Alice,
    <BLANKLINE>
    Can you feed Eve's cat this weekend?
    <BLANKLINE>
    Sincerely,
    Bob

    >>> greeting = 'Hello, world!'
    >>> greeting[0]
    'H'
    >>> greeting [4]
    'o'
    >>> greeting[-1]
    '!'
    >>> greeting[0:5]
    'Hello'
    >>> greeting[:5]
    'Hello'
    >>> greeting[7:-1]
    'world'
    >>> greeting[7:]
    'world!'


    >>> greeting = 'Hello, world!'
    >>> greeting_slice = greeting[0:5]
    >>> greeting_slice
    'Hello'
    >>> greeting
    'Hello, world!'


    >>> 'Hello' in 'Hello, World'
    True
    >>> 'Hello' in 'Hello'
    True
    >>> 'HELLO' in 'Hello, World'
    False
    >>> '' in 'spam'
    True
    >>> 'cats' not in 'cats and dogs'
    False


    >>> name = 'Al'
    >>> age = 4000
    >>> 'Hello, my name is ' + name + '. I am ' + str(age) + ' years old.'
    'Hello, my name is Al. I am 4000 years old.'
    >>> 'In ten years I will be ' + str(age + 10)
    'In ten years I will be 4010'


    >>> name = 'Al'
    >>> age = 4000
    >>> f'My name is {name}. I am {age} years old.'
    'My name is Al. I am 4000 years old.'
    >>> f'In ten years I will be {age + 10}'
    'In ten years I will be 4010'


    >>> name = 'Zophie'
    >>> f'{name}'
    'Zophie'
    >>> f'{{name}}' # Use double curly braces to include literal curly braces.
    '{name}'


    >>> name = 'Al'
    >>> age = 4000
    >>> 'My name is %s. I am %s years old.' % (name, age)
    'My name is Al. I am 4000 years old.'
    >>> 'In ten years I will be %s' % (age + 10)
    'In ten years I will be 4010'


    >>> name = 'Al'
    >>> age = 4000
    >>> 'My name is {}. I am {} years old.'.format(name, age)
    'My name is Al. I am 4000 years old.'


    >>> name = 'Al'
    >>> age = 4000
    >>> '{1} years ago, {0} was born and named {0}.'.format(name, age)
    '4000 years ago, Al was born and named Al.'


    >>> spam = 'Hello, world!'
    >>> spam = spam.upper()
    >>> spam
    'HELLO, WORLD!'
    >>> spam = spam.lower()
    >>> spam
    'hello, world!'


    >>> spam = 'Hello, world!'
    >>> spam.islower()
    False
    >>> spam.isupper()
    False
    >>> 'HELLO'.isupper()
    True
    >>> 'abc12345'.islower()
    True
    >>> '12345'.islower()
    False
    >>> '12345'.isupper()
    False


    >>> 'Hello'.upper()
    'HELLO'
    >>> 'Hello'.upper().lower()
    'hello'
    >>> 'Hello'.upper().lower().upper()
    'HELLO'
    >>> 'HELLO'.lower()
    'hello'
    >>> 'HELLO'.lower().islower()
    True


    >>> 'hello'.isalpha()
    True
    >>> 'hello123'.isalpha()
    False
    >>> 'hello123'.isalnum()
    True
    >>> 'hello'.isalnum()
    True
    >>> '123'.isdecimal()
    True
    >>> ' '.isspace()
    True
    >>> 'This Is Title Case'.istitle()
    True


    >>> 'Hello, world!'.startswith('Hello')
    True
    >>> 'Hello, world!'.endswith('world!')
    True
    >>> 'abc123'.startswith('abcdef')
    False
    >>> 'abc123'.endswith('12')
    False
    >>> 'Hello, world!'.startswith('Hello, world!')
    True
    >>> 'Hello, world!'.endswith('Hello, world!')
    True


    >>> ', '.join(['cats', 'rats', 'bats'])
    'cats, rats, bats'
    >>> ' '.join(['My', 'name', 'is', 'Simon'])
    'My name is Simon'
    >>> 'ABC'.join(['My', 'name', 'is', 'Simon'])
    'MyABCnameABCisABCSimon'


    >>> 'My name is Simon'.split()
    ['My', 'name', 'is', 'Simon']


    >>> 'MyABCnameABCisABCSimon'.split('ABC')
    ['My', 'name', 'is', 'Simon']
    >>> 'My name is Simon'.split('m')
    ['My na', 'e is Si', 'on']


    >>> spam = '''Dear Alice,
    ... There is a milk bottle in the fridge
    ... that is labeled "Milk Experiment."
    ...
    ... Please do not drink it.
    ... Sincerely,
    ... Bob'''
    >>> spam.split('\n')
    ['Dear Alice,', 'There is a milk bottle in the fridge', 'that is labeled "Milk Experiment."', '', 'Please do not drink it.', 'Sincerely,', 'Bob']


    >>> 'Hello'.rjust(10)
    '     Hello'
    >>> 'Hello'.rjust(20)
    '               Hello'
    >>> 'Hello, World'.rjust(20)
    '        Hello, World'
    >>> 'Hello'.ljust(10)
    'Hello     '


    >>> 'Hello'.rjust(20, '*')
    '***************Hello'
    >>> 'Hello'.ljust(20, '-')
    'Hello---------------'


    >>> 'Hello'.center(20)
    '       Hello        '
    >>> 'Hello'.center(20, '=')
    '=======Hello========'


    >>> spam = '    Hello, World    '
    >>> spam.strip()
    'Hello, World'
    >>> spam.lstrip()
    'Hello, World    '
    >>> spam.rstrip()
    '    Hello, World'


    >>> spam = 'SpamSpamBaconSpamEggsSpamSpam'
    >>> spam.strip('ampS')
    'BaconSpamEggs'


    >>> ord('A')
    65
    >>> ord('4')
    52
    >>> ord('!')
    33
    >>> chr(65)
    'A'


    >>> ord('B')
    66
    >>> ord('A') < ord('B')
    True
    >>> chr(ord('A'))
    'A'
    >>> chr(ord('A') + 1)
    'B'



    >>> import pyperclip
    >>> pyperclip.copy('Hello, world!')
    >>> pyperclip.paste()
    'Hello, world!'


    """

    # TODO: Test "Project: Adding Bullets to Wiki Markup"

    # TODO: Test "A Short Program: Pig Latin"


def test_chapter9_regex():
    r"""

    NOTE: Some difficulties testing since regex strings are often raw strings.

    >>> def is_phone_number(text):
    ...     if len(text) != 12: # Phone numbers have exactly 12 characters.
    ...         return False
    ...     for i in range(0, 3): # The first three characters must be numbers.
    ...         if not text[i].isdecimal():
    ...             return False
    ...     if text[3] != '-': # The fourth character must be a dash.
    ...         return False
    ...     for i in range(4, 7): # The next three characters must be numbers.
    ...         if not text[i].isdecimal():
    ...             return False
    ...     if text[7] != '-': # The eighth character must be a dash.
    ...         return False
    ...     for i in range(8, 12): # The next four characters must be numbers.
    ...         if not text[i].isdecimal():
    ...             return False
    ...     return True
    ...
    >>> print('Is 415-555-4242 a phone number?', is_phone_number('415-555-4242'))
    Is 415-555-4242 a phone number? True
    >>> print(is_phone_number('415-555-4242'))
    True
    >>> print('Is Moshi moshi a phone number?', is_phone_number('Moshi moshi'))
    Is Moshi moshi a phone number? False
    >>> print(is_phone_number('Moshi moshi'))
    False


    >>> import re
    >>> phone_num_pattern_obj = re.compile(r'\d{3}-\d{3}-\d{4}')
    >>> match_obj = phone_num_pattern_obj.search('My number is 415-555-4242.')
    >>> match_obj.group()
    '415-555-4242'


    >>> import re
    >>> phone_re = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
    >>> mo = phone_re.search('My number is 415-555-4242.')
    >>> mo.group(1) # Returns the first group of the matched text.
    '415'
    >>> mo.group(2) # Returns the second group of the matched text.
    '555-4242'
    >>> mo.group(0) # Returns the full matched text.
    '415-555-4242'
    >>> mo.group() # Also returns the full matched text.
    '415-555-4242'


    >>> mo.groups()
    ('415', '555-4242')
    >>> area_code, main_number = mo.groups()
    >>> print(area_code)
    415
    >>> print(main_number)
    555-4242


    >>> pattern = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
    >>> mo = pattern.search('My phone number is (415) 555-4242.')
    >>> mo.group(1)
    '(415)'
    >>> mo.group(2)
    '555-4242'


    >>> import re
    >>> pattern = re.compile(r'Cat(erpillar|astrophe|ch|egory)')
    >>> match = pattern.search('Catch me if you can.')
    >>> match.group()
    'Catch'
    >>> match.group(1)
    'ch'


    >>> import re
    >>> pattern = re.compile(r'\d{3}-\d{3}-\d{4}') # This regex has no groups.
    >>> pattern.findall('Cell: 415-555-9999 Work: 212-555-0000')
    ['415-555-9999', '212-555-0000']



    >>> import re
    >>> pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})') # This regex has groups.
    >>> pattern.findall('Cell: 415-555-9999 Work: 212-555-0000')
    [('415', '555', '9999'), ('212', '555', '0000')]


    >>> import re
    >>> pattern = re.compile(r'\d{3}')
    >>> pattern.findall('1234')
    ['123']
    >>> pattern.findall('12345')
    ['123']
    >>> pattern.findall('123456')
    ['123', '456']


    >>> import re
    >>> vowel_pattern = re.compile(r'[aeiouAEIOU]')
    >>> vowel_pattern.findall('RoboCop eats BABY FOOD.')
    ['o', 'o', 'o', 'e', 'a', 'A', 'O', 'O']



    >>> import re
    >>> consonant_pattern = re.compile(r'[^aeiouAEIOU]')
    >>> consonant_pattern.findall('RoboCop eats BABY FOOD.')
    ['R', 'b', 'C', 'p', ' ', 't', 's', ' ', 'B', 'B', 'Y', ' ', 'F', 'D', '.']


    >>> import re
    >>> pattern = re.compile(r'\d+\s\w+')
    >>> pattern.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
    ['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6 geese', '5 rings', '4 birds', '3 hens', '2 doves', '1 partridge']


    >>> import re
    >>> at_re = re.compile(r'.at')
    >>> at_re.findall('The cat in the hat sat on the flat mat.')
    ['cat', 'hat', 'sat', 'lat', 'mat']


    >>> import re
    >>> pattern = re.compile(r'42!?')
    >>> pattern.search('42!')
    <re.Match object; span=(0, 3), match='42!'>
    >>> pattern.search('42')
    <re.Match object; span=(0, 2), match='42'>


    >>> import re
    >>> pattern = re.compile(r'42?!')
    >>> pattern.search('42!')
    <re.Match object; span=(0, 3), match='42!'>
    >>> pattern.search('4!')
    <re.Match object; span=(0, 2), match='4!'>
    >>> pattern.search('42') == None # No match.
    True



    >>> pattern = re.compile(r'(\d{3}-)?\d{3}-\d{4}')
    >>> match1 = pattern.search('My number is 415-555-4242')
    >>> match1.group()
    '415-555-4242'
    >>> match2 = pattern.search('My number is 555-4242')
    >>> match2.group()
    '555-4242'


    >>> import re
    >>> pattern = re.compile('Eggs( and spam)*')
    >>> pattern.search('Eggs')
    <re.Match object; span=(0, 4), match='Eggs'>
    >>> pattern.search('Eggs and spam')
    <re.Match object; span=(0, 13), match='Eggs and spam'>
    >>> pattern.search('Eggs and spam and spam')
    <re.Match object; span=(0, 22), match='Eggs and spam and spam'>
    >>> pattern.search('Eggs and spam and spam and spam')
    <re.Match object; span=(0, 31), match='Eggs and spam and spam and spam'>



    >>> pattern = re.compile('Eggs( and spam)+')
    >>> pattern.search('Eggs and spam')
    <re.Match object; span=(0, 13), match='Eggs and spam'>
    >>> pattern.search('Eggs and spam and spam')
    <re.Match object; span=(0, 22), match='Eggs and spam and spam'>
    >>> pattern.search('Eggs and spam and spam and spam')
    <re.Match object; span=(0, 31), match='Eggs and spam and spam and spam'>


    >>> import re
    >>> haRegex = re.compile(r'(Ha){3}')
    >>> match1 = haRegex.search('HaHaHa')
    >>> match1.group()
    'HaHaHa'
    >>> match = haRegex.search('HaHa')
    >>> match == None
    True

    >>> import re
    >>> greedy_pattern = re.compile(r'(Ha){3,5}')
    >>> match1 = greedy_pattern.search('HaHaHaHaHa')
    >>> match1.group()
    'HaHaHaHaHa'
    >>> lazy_pattern = re.compile(r'(Ha){3,5}?')
    >>> match2 = lazy_pattern.search('HaHaHaHaHa')
    >>> match2.group()
    'HaHaHa'

    >>> import re
    >>> name_pattern = re.compile(r'First Name: (.*) Last Name: (.*)')
    >>> name_match = name_pattern.search('First Name: Al Last Name: Sweigart')
    >>> name_match.group(1)
    'Al'
    >>> name_match.group(2)
    'Sweigart'


    >>> import re
    >>> lazy_pattern = re.compile(r'<.*?>')
    >>> match1 = lazy_pattern.search('<To serve man> for dinner.>')
    >>> match1.group()
    '<To serve man>'
    >>> greedy_re = re.compile(r'<.*>')
    >>> match2 = greedy_re.search('<To serve man> for dinner.>')
    >>> match2.group()
    '<To serve man> for dinner.>'

    >>> import re
    >>> no_newline_re = re.compile('.*')
    >>> no_newline_re.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
    'Serve the public trust.'
    >>> newline_re = re.compile('.*', re.DOTALL)
    >>> newline_re.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
    'Serve the public trust.\nProtect the innocent.\nUphold the law.'


    >>> import re
    >>> begins_with_hello = re.compile(r'^Hello')
    >>> begins_with_hello.search('Hello, world!')
    <re.Match object; span=(0, 5), match='Hello'>
    >>> begins_with_hello.search('He said "Hello."') == None
    True


    >>> import re
    >>> ends_with_number = re.compile(r'\d$')
    >>> ends_with_number.search('Your number is 42')
    <re.Match object; span=(16, 17), match='2'>
    >>> ends_with_number.search('Your number is forty two.') == None
    True



    >>> import re
    >>> whole_string_is_num = re.compile(r'^\d+$')
    >>> whole_string_is_num.search('1234567890')
    <re.Match object; span=(0, 10), match='1234567890'>
    >>> whole_string_is_num.search('12345xyz67890') == None
    True

    >>> import re
    >>> pattern = re.compile(r'\bcat.*?\b')
    >>> pattern.findall('The cat found a catapult catalog in the catacombs.')
    ['cat', 'catapult', 'catalog', 'catacombs']


    >>> import re
    >>> pattern = re.compile(r'\Bcat\B')
    >>> pattern.findall('certificate') # Match.
    ['cat']
    >>> pattern.findall('catastrophe') # No match.
    []


    >>> import re
    >>> pattern1 = re.compile('RoboCop')
    >>> pattern2 = re.compile('ROBOCOP')
    >>> pattern3 = re.compile('robOcop')
    >>> pattern4 = re.compile('RobocOp')

    >>> import re
    >>> pattern = re.compile(r'robocop', re.I)
    >>> pattern.search('RoboCop is part man, part machine, all cop.').group()
    'RoboCop'
    >>> pattern.search('ROBOCOP protects the innocent.').group()
    'ROBOCOP'
    >>> pattern.search('Have you seen robocop?').group()
    'robocop'

    >>> import re
    >>> agent_pattern = re.compile(r'Agent \w+')
    >>> agent_pattern.sub('CENSORED', 'Agent Alice contacted Agent Bob.')
    'CENSORED contacted CENSORED.'


    >>> import re
    >>> agent_pattern = re.compile(r'Agent (\w)\w*')
    >>> agent_pattern.sub(r'\1****', 'Agent Alice contacted Agent Bob.')
    'A**** contacted B****.'


    >>> some_regex = re.compile('foo', re.IGNORECASE | re.DOTALL)

    >>> some_regex = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)


    >>> from humre import *
    >>> phone_regex = exactly(3, DIGIT) + '-' + exactly(3, DIGIT) + '-' + exactly(4, DIGIT)
    >>> phone_regex
    '\\d{3}-\\d{3}-\\d{4}'


    >>> import re
    >>> pattern = re.compile(phone_regex)
    >>> pattern.search('My number is 415-555-4242')
    <re.Match object; span=(13, 25), match='415-555-4242'>

    """


def test_chapter10_read_write_files():
    r"""
    NOTE THAT THESE EXAMPLES MUST RUN ON WINDOWS ON AL'S COMPUTER

    >>> from pathlib import Path
    >>> Path('spam', 'bacon', 'eggs')
    WindowsPath('spam/bacon/eggs')
    >>> str(Path('spam', 'bacon', 'eggs'))
    'spam\\bacon\\eggs'


    >>> from pathlib import Path
    >>> my_files = ['accounts.txt', 'details.csv', 'invite.docx']
    >>> for filename in my_files:
    ...     print(Path(r'C:\Users\Al', filename))
    ...
    C:\Users\Al\accounts.txt
    C:\Users\Al\details.csv
    C:\Users\Al\invite.docx


    >>> from pathlib import Path
    >>> Path('spam') / 'bacon' / 'eggs'
    WindowsPath('spam/bacon/eggs')
    >>> Path('spam') / Path('bacon/eggs')
    WindowsPath('spam/bacon/eggs')
    >>> Path('spam') / Path('bacon', 'eggs')
    WindowsPath('spam/bacon/eggs')


    >>> 'spam' / 'bacon'
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: unsupported operand type(s) for /: 'str' and 'str'


    >>> from pathlib import Path
    >>> import os
    >>> os.chdir('C:/Users/Al/AppData/Local/Programs/Python/Python312')
    >>> Path.cwd()
    WindowsPath('C:/Users/Al/AppData/Local/Programs/Python/Python312')
    >>> os.chdir('C:\\Windows\\System32')
    >>> Path.cwd()
    WindowsPath('C:/Windows/System32')
    >>> os.chdir(Path(__file__).parent)



    >>> from pathlib import Path
    >>> Path.home()
    WindowsPath('C:/Users/Al')



    >>> from pathlib import Path
    >>> Path.cwd().is_absolute()
    True
    >>> Path('spam/bacon/eggs').is_absolute()
    False


    >>> from pathlib import Path
    >>> Path('my/relative/path')
    WindowsPath('my/relative/path')



    >>> from pathlib import Path
    >>> Path('my/relative/path')
    WindowsPath('my/relative/path')
    >>> Path.home() / Path('my/relative/path')
    WindowsPath('C:/Users/Al/my/relative/path')


    >>> from pathlib import Path
    >>> p = Path('C:/Users/Al/spam.txt')
    >>> p.anchor
    'C:\\'
    >>> p.parent
    WindowsPath('C:/Users/Al')
    >>> p.name
    'spam.txt'
    >>> p.stem
    'spam'
    >>> p.suffix
    '.txt'
    >>> p.drive
    'C:'

    >>> from pathlib import Path
    >>> p = Path('C:/Users/Al/spam.txt')
    >>> p.parts
    ('C:\\', 'Users', 'Al', 'spam.txt')
    >>> p.parts[3]
    'spam.txt'
    >>> p.parts[0:2]
    ('C:\\', 'Users')


    >>> import os
    >>> os.chdir(r'C:\Users\Al\Desktop')
    >>> from pathlib import Path
    >>> Path.cwd()
    WindowsPath('C:/Users/Al/Desktop')
    >>> Path.cwd().parents[0]
    WindowsPath('C:/Users/Al')
    >>> Path.cwd().parents[1]
    WindowsPath('C:/Users')
    >>> Path.cwd().parents[2]
    WindowsPath('C:/')
    >>> os.chdir(Path(__file__).parent)


    >>> from pathlib import Path
    >>> win_dir = Path('C:/Windows')
    >>> not_exists_dir = Path('C:/This/Folder/Does/Not/Exist')
    >>> calc_file_path = Path('C:/Windows/System32/calc.exe')
    >>> win_dir.exists()
    True
    >>> win_dir.is_dir()
    True
    >>> not_exists_dir.exists()
    False
    >>> calc_file_path.is_file()
    True
    >>> calc_file_path.is_dir()
    False



    >>> from pathlib import Path
    >>> p = Path('spam.txt')
    >>> p.write_text('Hello, world!')
    13
    >>> p.read_text()
    'Hello, world!'
    >>> import os;os.unlink('spam.txt')

    >>> p = Path.home() / 'hello.txt'
    >>> p.write_text('Hello, world!')
    13
    >>> from pathlib import Path
    >>> hello_file = open(Path.home() / 'hello.txt', encoding='UTF-8')

    >>> hello_content = hello_file.read()
    >>> hello_content
    'Hello, world!'

    >>> from pathlib import Path
    >>> p=(Path.home() / 'sonnet29.txt')
    >>> p.write_text("When, in disgrace with fortune and men's eyes,\nI all alone beweep my outcast state,\nAnd trouble deaf heaven with my bootless cries,\nAnd look upon myself and curse my fate,")
    171
    >>> sonnet_file = open(Path.home() / 'sonnet29.txt', encoding='UTF-8')
    >>> sonnet_file.readlines()
    ["When, in disgrace with fortune and men's eyes,\n", 'I all alone beweep my outcast state,\n', 'And trouble deaf heaven with my bootless cries,\n', 'And look upon myself and curse my fate,']
    >>> sonnet_file.close()
    >>> import os;os.unlink(Path.home() / 'sonnet29.txt')


    >>> bacon_file = open('bacon.txt', 'w', encoding='UTF-8')
    >>> bacon_file.write('Hello, world!\n')
    14
    >>> bacon_file.close()
    >>> bacon_file = open('bacon.txt', 'a', encoding='UTF-8')
    >>> bacon_file.write('Bacon is not a vegetable.')
    25
    >>> bacon_file.close()
    >>> bacon_file = open('bacon.txt', encoding='UTF-8')
    >>> content = bacon_file.read()
    >>> bacon_file.close()
    >>> print(content)
    Hello, world!
    Bacon is not a vegetable.
    >>> import os; os.unlink('bacon.txt')

    >>> import os;os.chdir(Path(__file__).parent)
    >>> file_obj = open('data.txt', 'w', encoding='utf-8')
    >>> file_obj.write('Hello, world!')
    13
    >>> file_obj.close()
    >>> file_obj = open('data.txt', encoding='utf-8')
    >>> content = file_obj.read()
    >>> file_obj.close()

    >>> with open('data.txt', 'w', encoding='UTF-8') as file_obj:
    ...   file_obj.write('Hello, world!')
    ...
    13
    >>> with open('data.txt', encoding='UTF-8') as file_obj:
    ...   content = file_obj.read()
    ...
    >>> import os;os.unlink('data.txt')

    >>> import os;os.chdir(Path(__file__).parent)
    >>> import shelve
    >>> shelf_file = shelve.open('mydata')
    >>> shelf_file['cats'] = ['Zophie', 'Pooka', 'Simon']
    >>> shelf_file.close()

    >>> shelf_file = shelve.open('mydata')
    >>> type(shelf_file)
    <class 'shelve.DbfilenameShelf'>
    >>> shelf_file['cats']
    ['Zophie', 'Pooka', 'Simon']
    >>> shelf_file.close()

    >>> shelf_file = shelve.open('mydata')
    >>> list(shelf_file.keys())
    ['cats']
    >>> list(shelf_file.values())
    [['Zophie', 'Pooka', 'Simon']]
    >>> shelf_file.close()

    >>> import os;os.unlink('mydata.bak');os.unlink('mydata.dat');os.unlink('mydata.dir')
"""

    # TODO: Test "Project: Generating Random Quiz Files"



def test_chapter11_organizing_files():
    r"""
    TODO: Too difficult to manage the files.

    """



def test_chapter12_deploying():
    """
    >>> import bext
    >>> bext.fg('red')
    >>> print('This text is red.')
    This text is red.
    >>> bext.bg('blue')
    >>> print('Red text on blue background is an ugly color scheme.')
    Red text on blue background is an ugly color scheme.
    >>> bext.fg('reset')
    >>> bext.bg('reset')
    >>> print('The text is normal again. Ah, much better.')
    The text is normal again. Ah, much better.


    """

    # TODO: Test "A Short Program: Snowstorm"


def test_chapter13_web_scraping():
    """

    >>> import bs4
    >>> with open('example3.html') as example_file:
    ...  example_soup = bs4.BeautifulSoup(example_file, 'html.parser')
    >>> type(example_soup)
    <class 'bs4.BeautifulSoup'>

    >>> import bs4
    >>> example_file = open('example3.html')
    >>> example_soup = bs4.BeautifulSoup(example_file.read(), 'html.parser')
    >>> elems = example_soup.select('#author')
    >>> type(elems) # elems is a list of Tag objects.
    <class 'bs4.element.ResultSet'>
    >>> len(elems)
    1
    >>> type(elems[0])
    <class 'bs4.element.Tag'>
    >>> str(elems[0]) # The Tag object as a string
    '<span id="author">Al Sweigart</span>'
    >>> elems[0].getText() # The inner text of the element.
    'Al Sweigart'
    >>> elems[0].attrs
    {'id': 'author'}

    >>> p_elems = example_soup.select('p')
    >>> str(p_elems[0])
    '<p>This &lt;p&gt; tag puts <b>content</b> into a <i>single</i> paragraph.</p>'
    >>> p_elems[0].getText()
    'This <p> tag puts content into a single paragraph.'
    >>> str(p_elems[1])
    '<p><a href="https://inventwithpython.com">This text is a link</a> to books by <span id="author">Al Sweigart</span>.</p>'
    >>> p_elems[1].getText()
    'This text is a link to books by Al Sweigart.'
    >>> str(p_elems[2])
    '<p><img alt="Close up of my cat Zophie." src="wow_such_zophie_thumb.webp"/></p>'
    >>> p_elems[2].getText()
    ''


    >>> import bs4
    >>> soup = bs4.BeautifulSoup(open('example3.html'), 'html.parser')
    >>> span_elem = soup.select('span')[0]
    >>> str(span_elem)
    '<span id="author">Al Sweigart</span>'
    >>> span_elem.get('id')
    'author'
    >>> span_elem.get('some_nonexistent_addr') == None
    True
    >>> span_elem.attrs
    {'id': 'author'}


    """

    # TODO: Test "Project: Running showmap.py with the webbrowser Module"



def test_chapter14_excel():
    """
    >>> import openpyxl
    >>> wb = openpyxl.load_workbook('example3.xlsx')
    >>> type(wb)
    <class 'openpyxl.workbook.workbook.Workbook'>



    >>> import openpyxl
    >>> wb = openpyxl.load_workbook('example3.xlsx')
    >>> wb.sheetnames # The workbook's sheets' names.
    ['Sheet1', 'Sheet2', 'Sheet3']
    >>> sheet = wb['Sheet3'] # Get a sheet from the workbook.
    >>> sheet
    <Worksheet "Sheet3">
    >>> type(sheet)
    <class 'openpyxl.worksheet.worksheet.Worksheet'>
    >>> sheet.title # Get the sheet's title as a string.
    'Sheet3'
    >>> another_sheet = wb.active # Get the active sheet.
    >>> another_sheet
    <Worksheet "Sheet1">



    >>> import openpyxl
    >>> wb = openpyxl.load_workbook('example3.xlsx')
    >>> sheet = wb['Sheet1'] # Get a sheet from the workbook.
    >>> sheet['A1'] # Get a cell from the sheet.
    <Cell 'Sheet1'.A1>
    >>> sheet['A1'].value # Get the value from the cell.
    datetime.datetime(2035, 4, 5, 13, 34, 2)
    >>> c = sheet['B1'] # Get another cell from the sheet.
    >>> c.value
    'Apples'
    >>> # Get the row, column, and value from the cell.
    >>> f'Row {c.row}, Column {c.column} is {c.value}'
    'Row 1, Column 2 is Apples'
    >>> f'Cell {c.coordinate} is {c.value}'
    'Cell B1 is Apples'
    >>> sheet['C1'].value
    73



    >>> sheet.cell(row=1, column=2)
    <Cell 'Sheet1'.B1>
    >>> sheet.cell(row=1, column=2).value
    'Apples'
    >>> for i in range(1, 8, 2): # Go through every other row.
    ...  print(i, sheet.cell(row=i, column=2).value)
    ...
    1 Apples
    3 Pears
    5 Apples
    7 Strawberries





    >>> import openpyxl
    >>> wb = openpyxl.load_workbook('example3.xlsx')
    >>> sheet = wb['Sheet1']
    >>> sheet.max_row # Get the highest row number.
    7
    >>> sheet.max_column # Get the highest column number.
    3


    >>> import openpyxl
    >>> from openpyxl.utils import get_column_letter, column_index_from_string
    >>> get_column_letter(1) # Translate column 1 to a letter.
    'A'
    >>> get_column_letter(2)
    'B'
    >>> get_column_letter(27)
    'AA'
    >>> get_column_letter(900)
    'AHP'
    >>> wb = openpyxl.load_workbook('example3.xlsx')
    >>> sheet = wb['Sheet1']
    >>> get_column_letter(sheet.max_column)
    'C'
    >>> column_index_from_string('A') # Get A's number.
    1
    >>> column_index_from_string('AA')
    27



    >>> import openpyxl
    >>> wb = openpyxl.load_workbook('example3.xlsx')
    >>> sheet = wb['Sheet1']
    >>> sheet['A1':'C3'] # Get cells A1 to C3.
    ((<Cell 'Sheet1'.A1>, <Cell 'Sheet1'.B1>, <Cell 'Sheet1'.C1>), (<Cell 'Sheet1'.A2>, <Cell 'Sheet1'.B2>, <Cell 'Sheet1'.C2>), (<Cell 'Sheet1'.A3>, <Cell 'Sheet1'.B3>, <Cell 'Sheet1'.C3>))
    >>> for row_of_cell_objects in sheet['A1':'C3']:
    ...  for cell_obj in row_of_cell_objects:
    ...   print(cell_obj.coordinate, cell_obj.value)
    ...  print('--- END OF ROW ---')
    ...
    A1 2035-04-05 13:34:02
    B1 Apples
    C1 73
    --- END OF ROW ---
    A2 2035-04-05 03:41:23
    B2 Cherries
    C2 85
    --- END OF ROW ---
    A3 2035-04-06 12:46:51
    B3 Pears
    C3 14
    --- END OF ROW ---



    >>> import openpyxl
    >>> wb = openpyxl.load_workbook('example3.xlsx')
    >>> sheet = wb['Sheet1']
    >>> list(sheet.columns)[1] # Get second column's cells.
    (<Cell 'Sheet1'.B1>, <Cell 'Sheet1'.B2>, <Cell 'Sheet1'.B3>, <Cell 'Sheet1'.B4>, <Cell 'Sheet1'.B5>, <Cell 'Sheet1'.B6>, <Cell 'Sheet1'.B7>)
    >>> for cell_obj in list(sheet.columns)[1]:
    ...  print(cell_obj.value)
    ...
    Apples
    Cherries
    Pears
    Oranges
    Apples
    Bananas
    Strawberries


    >>> import openpyxl
    >>> wb = openpyxl.Workbook() # Create a blank workbook.
    >>> wb.sheetnames # The workbook starts with one sheet.
    ['Sheet']
    >>> sheet = wb.active
    >>> sheet.title
    'Sheet'
    >>> sheet.title = 'Spam Bacon Eggs Sheet' # Change the title.
    >>> wb.sheetnames
    ['Spam Bacon Eggs Sheet']


    >>> import openpyxl
    >>> wb = openpyxl.load_workbook('example3.xlsx')
    >>> sheet = wb['Sheet1']
    >>> sheet.title = 'Spam Spam Spam'
    >>> wb.save('example3_copy.xlsx') # Save the workbook.

    >>> import os; os.unlink('example3_copy.xlsx')




    >>> import openpyxl
    >>> wb = openpyxl.Workbook()
    >>> wb.sheetnames
    ['Sheet']
    >>> wb.create_sheet() # Add a new sheet.
    <Worksheet "Sheet1">
    >>> wb.sheetnames
    ['Sheet', 'Sheet1']
    >>> # Create a new sheet at index 0.
    >>> wb.create_sheet(index=0, title='First Sheet')
    <Worksheet "First Sheet">
    >>> wb.sheetnames
    ['First Sheet', 'Sheet', 'Sheet1']
    >>> wb.create_sheet(index=2, title='Middle Sheet')
    <Worksheet "Middle Sheet">
    >>> wb.sheetnames
    ['First Sheet', 'Sheet', 'Middle Sheet', 'Sheet1']

    >>> wb.sheetnames
    ['First Sheet', 'Sheet', 'Middle Sheet', 'Sheet1']
    >>> del wb['Middle Sheet']
    >>> del wb['Sheet1']
    >>> wb.sheetnames
    ['First Sheet', 'Sheet']




    >>> import openpyxl
    >>> wb = openpyxl.Workbook()
    >>> sheet = wb['Sheet']
    >>> sheet['A1'] = 'Hello, world!' # Edit the cell's value.
    >>> sheet['A1'].value
    'Hello, world!'


    >>> import openpyxl
    >>> from openpyxl.styles import Font
    >>> wb = openpyxl.Workbook()
    >>> sheet = wb['Sheet']
    >>> italic_24_font = Font(size=24, italic=True)
    >>> sheet['A1'].font = italic_24_font
    >>> sheet['A1'] = 'Hello, world!'
    >>> wb.save('styles3.xlsx')


    >>> import openpyxl
    >>> from openpyxl.styles import Font
    >>> wb = openpyxl.Workbook()
    >>> sheet = wb['Sheet']
    >>> bold_font = Font(name='Times New Roman', bold=True)
    >>> sheet['A1'].font = bold_font
    >>> sheet['A1'] = 'Bold Times New Roman'
    >>> italic_font = Font(size=24, italic=True)
    >>> sheet['B3'].font = italic_font
    >>> sheet['B3'] = '24 pt Italic'
    >>> wb.save('styles3.xlsx')

    >>> import os;os.unlink('styles3.xlsx')




    >>> import openpyxl
    >>> wb = openpyxl.Workbook()
    >>> sheet = wb['Sheet']
    >>> sheet['A1'] = 200
    >>> sheet['A2'] = 300
    >>> sheet['A3'] = '=SUM(A1:A2)' # Set the formula.
    >>> wb.save('writeFormula3.xlsx')

    >>> # Be sure to open writeFormula.xlsx in Excel and save it first.
    >>> import openpyxl
    >>> wb = openpyxl.load_workbook('writeFormula3.xlsx') # Open without data_only.
    >>> wb.active['A3'].value # Get the formula string.
    '=SUM(A1:A2)'
    >>> wb = openpyxl.load_workbook('writeFormula3.xlsx', data_only=True) # Open with data_only.
    >>> wb.active['A3'].value # Get the formula result.


    NOTE: The previous thing would normally result in 500, but only if we open the workbook in excel and then saved it.


    >>> import os;os.unlink('writeFormula3.xlsx')




    >>> import openpyxl
    >>> wb = openpyxl.Workbook()
    >>> sheet = wb['Sheet']
    >>> sheet['A1'] = 'Tall row'
    >>> sheet['B2'] = 'Wide column'
    >>> sheet.row_dimensions[1].height = 70
    >>> sheet.column_dimensions['B'].width = 20
    >>> wb.save('dimensions3.xlsx')

    >>> import os;os.unlink('dimensions3.xlsx')



    >>> import openpyxl
    >>> wb = openpyxl.Workbook()
    >>> sheet = wb['Sheet']
    >>> sheet.merge_cells('A1:D3') # Merge all these cells.
    >>> sheet['A1'] = 'Twelve cells merged together.'
    >>> sheet.merge_cells('C5:D5') # Merge these two cells.
    >>> sheet['C5'] = 'Two merged cells.'
    >>> wb.save('merged3.xlsx')




    >>> import openpyxl
    >>> wb = openpyxl.load_workbook('merged3.xlsx')
    >>> sheet = wb['Sheet']
    >>> sheet.unmerge_cells('A1:D3') # Split these cells up.
    >>> sheet.unmerge_cells('C5:D5')
    >>> wb.save('unmerged3.xlsx')

    >>> import os;os.unlink('merged3.xlsx')
    >>> import os;os.unlink('unmerged3.xlsx')



    >>> import openpyxl
    >>> wb = openpyxl.load_workbook('produceSales.xlsx')
    >>> sheet = wb.active
    >>> sheet.freeze_panes = 'A2' # Freeze the rows above A2.
    >>> wb.save('freezeExample3.xlsx')

    >>> import os;os.unlink('freezeExample3.xlsx')



    >>> import openpyxl
    >>> wb = openpyxl.Workbook()
    >>> sheet = wb.active
    >>> for i in range(1, 11): # Create some data in column A.
    ...  sheet['A' + str(i)] = i * i
    ...
    >>> ref_obj = openpyxl.chart.Reference(sheet, min_col=1, min_row=1, max_col=1, max_row=10)
    >>> series_obj = openpyxl.chart.Series(ref_obj, title='First series')
    >>> chart_obj = openpyxl.chart.BarChart()
    >>> chart_obj.title = 'My Chart'
    >>> chart_obj.append(series_obj)
    >>> sheet.add_chart(chart_obj, 'C5')
    >>> wb.save('sampleChart3.xlsx')

    >>> import os;os.unlink('sampleChart3.xlsx')


    """

    # TODO: Test "Project: Updating a Spreadsheet"


def test_chapter15_sqlite():
    """

>>> import os
>>> if os.path.exists('example.db'): os.unlink('example.db') # TEST CLEAN UP

>>> import sqlite3
>>> conn = sqlite3.connect('example.db', isolation_level=None)
>>> conn.close() # TEST CLEAN UP

>>> import sqlite3
>>> conn = sqlite3.connect('example.db', isolation_level=None)
>>> DUMMY = conn.execute('CREATE TABLE IF NOT EXISTS cats (name TEXT NOT NULL, birthdate TEXT, fur TEXT, weight_kg REAL) STRICT')
>>> conn.close() # TEST CLEAN UP

>>> import sqlite3
>>> DUMMY = sqlite3.sqlite_version


>>> import sqlite3
>>> conn = sqlite3.connect('example.db', isolation_level=None)
>>> conn.execute('SELECT name FROM sqlite_schema WHERE type="table"').fetchall()
[('cats',)]

>>> conn.execute('PRAGMA TABLE_INFO(cats)').fetchall()
[(0, 'name', 'TEXT', 1, None, 0), (1, 'birthdate', 'TEXT', 0, None, 0), (2, 'fur', 'TEXT', 0, None, 0), (3, 'weight_kg', 'REAL', 0, None, 0)]
>>> conn.close() # TEST CLEAN UP


>>> import sqlite3
>>> conn = sqlite3.connect('example.db', isolation_level=None)
>>> DUMMY = conn.execute('CREATE TABLE IF NOT EXISTS cats (name TEXT NOT NULL, birthdate TEXT, fur TEXT, weight_kg REAL) STRICT')
>>> DUMMY = conn.execute('INSERT INTO cats VALUES ("Zophie", "2021-01-24", "black", 5.6)')


>>> cat_name = 'Zophie'
>>> cat_bday = '2021-01-24'
>>> fur_color = 'black'
>>> cat_weight = 5.6
>>> DUMMY = conn.execute(f'INSERT INTO cats VALUES ("{cat_name}", "{cat_bday}", "{fur_color}", {cat_weight})')

>>> conn.close()  # TEST CLEAN UP


>>> conn = sqlite3.connect('example.db', isolation_level=None) # TEST SETUP
>>> DUMMY = conn.execute('INSERT INTO cats VALUES ("Zophie", "2021-01-24", "black", 5.6)')

>>> conn.close()  # TEST CLEAN UP
>>> if os.path.exists('example.db'): os.unlink('example.db') # TEST CLEAN UP


>>> conn = sqlite3.connect('example.db', isolation_level=None) # TEST SETUP

>>> DUMMY = conn.execute('CREATE TABLE IF NOT EXISTS cats (name TEXT NOT NULL, birthdate TEXT, fur TEXT, weight_kg REAL) STRICT') # TEST SETUP
>>> DUMMY = conn.execute(f'INSERT INTO cats VALUES (?, ?, ?, ?)', [cat_name, cat_bday, fur_color, cat_weight])
>>> conn.close()  # TEST CLEAN UP


>>> import sqlite3
>>> conn = sqlite3.connect('example.db', isolation_level=None)

>>> conn.execute('SELECT * FROM cats').fetchall()
[('Zophie', '2021-01-24', 'black', 5.6)]

>>> conn.execute('SELECT rowid, name FROM cats').fetchall()
[(1, 'Zophie')]


>>> conn.close() # TEST CLEAN UP









    """




    # LEFT OFF: THIS HAS BUGS AND NEEDS FIXING:
    '''

>>> import shutil, os
>>> if os.path.exists('sweigartcats.db'): os.unlink('sweigartcats.db')
>>> shutil.copyfile('original-sweigartcats.db', 'sweigartcats.db')
'sweigartcats.db'



>>> import sqlite3
>>> conn = sqlite3.connect('sweigartcats.db', isolation_level=None)
>>> conn.execute('SELECT * FROM cats WHERE fur = "black"').fetchall()
[('Toby', '2021-05-17', 'black', 6.8), ('Thor', '2013-05-14', 'black', 5.2), ('Sassy', '2017-08-20', 'black', 7.5), ('Hope', '2016-05-22', 'black', 7.6)]

>>> import pprint
>>> matching_cats = conn.execute('SELECT * FROM cats WHERE fur = "black" OR birthdate >= "2024-01-01"').fetchall()

>>> conn.execute('SELECT rowid, name FROM cats WHERE name LIKE "%y"').fetchall()
[(5, 'Toby'), (11, 'Molly'), (12, 'Dusty'), (17, 'Mandy'), (18, 'Taffy'), (25, 'Rocky'), (27, 'Bobby'), (30, 'Misty'), (34, 'Mitsy'), (38, 'Colby'), (40, 'Riley'), (46, 'Ruby'), (65, 'Daisy'), (67, 'Crosby'), (72, 'Harry'), (77, 'Sassy'), (85, 'Lily'), (93, 'Spunky')]
>>> conn.execute('SELECT rowid, name FROM cats WHERE name LIKE "Ja%"').fetchall()
[(3, 'Jacob'), (49, 'Java'), (75, 'Jasmine'), (80, 'Jamison')]

>>> conn.execute('SELECT rowid, name FROM cats WHERE name LIKE "%ob%"').fetchall()
[(3, 'Jacob'), (5, 'Toby'), (27, 'Bobby')]


>>> conn.execute('SELECT rowid, name FROM cats WHERE name GLOB "*m*"').fetchall()
[(4, 'Gumdrop'), (9, 'Thomas'), (44, 'Sam'), (63, 'Cinnamon'), (75, 'Jasmine'), (79, 'Samantha'), (80, 'Jamison')]


>>> conn.close() # TEST CLEAN UP




>>> import sqlite3, pprint
>>> conn = sqlite3.connect('sweigartcats.db', isolation_level=None)
>>> DUMMY = conn.execute('SELECT * FROM cats ORDER BY fur').fetchall()

>>> cur = conn.execute('SELECT * FROM cats ORDER BY fur, birthdate')
>>> DUMMY = cur.fetchall()

>>> cur = conn.execute('SELECT * FROM cats ORDER BY fur ASC, birthdate DESC')
>>> DUMMY = cur.fetchall()

>>> conn.close() # TEST CLEAN UP




>>> import sqlite3
>>> conn = sqlite3.connect('sweigartcats.db', isolation_level=None)
>>> conn.execute('SELECT * FROM cats').fetchall()[:3] # This is inefficient.
[('Zophie', '2021-01-24', 'gray tabby', 5.6), ('Miguel', '2016-12-24', 'siamese', 6.2), ('Jacob', '2022-02-20', 'orange and white', 5.5)]

>>> conn.execute('SELECT * FROM cats LIMIT 3').fetchall()
[('Zophie', '2021-01-24', 'gray tabby', 5.6), ('Miguel', '2016-12-24', 'siamese', 6.2), ('Jacob', '2022-02-20', 'orange and white', 5.5)]

>>> conn.execute('SELECT * FROM cats WHERE fur="orange" ORDER BY birthdate LIMIT 4').fetchall()
[('Mittens', '2013-07-03', 'orange', 7.4), ('Piers', '2014-07-08', 'orange', 5.2), ('Misty', '2016-07-08', 'orange', 5.2), ('Blaze', '2023-01-16', 'orange', 7.4)]
>>> conn.close() # TEST CLEAN UP




>>> import sqlite3
>>> conn = sqlite3.connect('sweigartcats.db', isolation_level=None)
>>> DUMMY = conn.execute('CREATE INDEX idx_name ON cats (name)')
>>> DUMMY = conn.execute('CREATE INDEX idx_birthdate ON cats (birthdate)')


>>> conn.execute('SELECT name FROM sqlite_schema WHERE type = "index" AND tbl_name = "cats"').fetchall()
[('idx_name',), ('idx_birthdate',)]

>>> conn.execute('SELECT name FROM sqlite_schema WHERE type = "index" AND tbl_name = "cats"').fetchall()
[('idx_name',), ('idx_birthdate',)]
>>> DUMMY = conn.execute('DROP INDEX idx_name')
>>> conn.execute('SELECT name FROM sqlite_schema WHERE type = "index" AND tbl_name = "cats"').fetchall()
[('idx_birthdate',)]

>>> conn.close() # TEST CLEAN UP






>>> import sqlite3
>>> conn = sqlite3.connect('sweigartcats.db', isolation_level=None)
>>> conn.execute('SELECT * FROM cats WHERE rowid = 1').fetchall()
[('Zophie', '2021-01-24', 'black', 5.6)]
>>> conn.execute('UPDATE cats SET fur = "gray tabby" WHERE rowid = 1')
<sqlite3.Cursor object at 0x0000013EC121A040>
>>> conn.execute('SELECT * FROM cats WHERE rowid = 1').fetchall()
[('Zophie', '2021-01-24', 'gray tabby', 5.6)]


>>> conn.close() # TEST CLEAN UP


>>> os.unlink('sweigartcats.db')


# LEFT OFF - need to figure out what to do about hte Zophie entry at the start of sweigartcats.db
    '''



def test_chapter17_pdfword():
    """

    >>> import pypdf
    >>> writer = pypdf.PdfWriter()
    >>> writer.append('Recursion_Chapter1.pdf', (0, 5))
    >>> with open('first_five_pages.pdf', 'wb') as file:
    ...     writer.write(file)
    ...
    (False, <_io.BufferedWriter name='first_five_pages.pdf'>)

    >>> import os;os.unlink('first_five_pages.pdf')  # TEST CLEAN UP



    >>> list(range(0, 5)) # Passing (0, 5) makes append() copy these pages:
    [0, 1, 2, 3, 4]
    >>> list(range(0, 5, 2)) # Passing (0, 5, 2) makes append() copy these pages:
    [0, 2, 4]


    >>> import pypdf
    >>> writer = pypdf.PdfWriter()
    >>> writer.append('Recursion_Chapter1.pdf')
    >>> for i in range(len(writer.pages)):
    ...   DUMMY = writer.pages[i].rotate(90)
    ...
    >>> with open('rotated.pdf', 'wb') as file:
    ...   writer.write(file)
    ...
    (False, <_io.BufferedWriter name='rotated.pdf'>)

    >>> import os;os.unlink('rotated.pdf')  # TEST CLEAN UP




    >>> import pypdf
    >>> writer = pypdf.PdfWriter()
    >>> writer.append('Recursion_Chapter1.pdf')
    >>> DUMMY = writer.add_blank_page()
    >>> writer.insert_blank_page(index=2)
    {'/Type': '/Page', '/Parent': NullObject, '/Resources': {}, '/MediaBox': RectangleObject([0.0, 0.0, 546, 708])}
    >>> with open('with_blanks.pdf', 'wb') as file:
    ...   writer.write(file) # Save the writer object to a PDFfile.
    ...
    (False, <_io.BufferedWriter name='with_blanks.pdf'>)


    >>> import os;os.unlink('with_blanks.pdf')  # TEST CLEAN UP




    >>> import pypdf
    >>> writer = pypdf.PdfWriter()
    >>> writer.append('Recursion_Chapter1.pdf')
    >>> watermark_page = pypdf.PdfReader('watermark.pdf').pages[0]
    >>> for page in writer.pages:
    ...     page.merge_page(watermark_page, over=False)
    ...
    >>> with open('with_watermark.pdf', 'wb') as file:
    ...     writer.write(file)
    ...
    (False, <_io.BufferedWriter name='with_watermark.pdf'>)


    >>> import os;os.unlink('with_watermark.pdf')  # TEST CLEAN UP





"""

if __name__ == '__main__':
    doctest.testmod()

