# -----------------------------------
# Conversions
# -----------------------------------
def demo_conversions():
    '''Demonstrate type conversions using
    constructors
    '''
    i = int('1')
    f = float('1.0')
    f2 = float(1)
    i2 = int(1.0)
    s = set([1,2,3])
    return (i,f,f2,i2,s)


# -----------------------------------
# Common string functions
# -----------------------------------
def demo_strings(text):
    words = text.split()  # divide at any white space
    word_cnt = len(words) # number of elements in words
    sentences = text.split('.') # divide at period
    sentence_cnt = len(sentences) # number of sentences in text (assuming no '!' or '?' were used)
    new_text = ' '.join(words) # rebuild the text from words list.  All 1 line now
    all_up = text.upper()  # covert to all upper case letters
    all_low = text.lower() # covert to all lower case letters

# -----------------------------------
# printing
# -----------------------------------
def print_demos():
    # stay on same line
    for i in range(10):
        print(i, end = ' ')

    # go to next line
    print()

    # use a different separator than space
    print("Hello", "in", "there", sep = "! ")

# -----------------------------------
# simple loops
# -----------------------------------
def demo_list_loop():
    for i in ['a', 'b', 'c']:
        print(i)

def demo_range_loop():
    for i in range(10):
        print(i)

def demo_string_loop():
    for i in "qwerty":
        print(i)

# -----------------------------------
# processing 2 lists with indexes
# -----------------------------------
def process_two_lists():
    '''Handle 2 lists where each entry in one list
    has a corresponding member in the other list.
    This works when each list is the same length.
    instead of accessing the lists directly, use an
    index that is meaningful to both lists.  In the
    example below price[0] and change[0] are meant to
    be paired, so if i is 0, the code has access to
    both
    '''
    new_prices = []
    price = [23.99, 12.50, 39.01, 9.65]
    change = [0.10, 0.05, -0.09, 0.25]

    for i in range(len(price)):
        new_prices.append(price[i] + price[i] * change[i])
    return new_prices

# -----------------------------------
# Multi-dimensional lists and nested
# loops.
# -----------------------------------

grades = [
  [6, 9, 11],
  [3, 4, 10],
  [7, 8, 9],
  [5, 7, 10],
  [7, 9, 8]
]

def return_dimensions(table):
    ''' The dimensions of a 2 dimensional
    list are:
    len(table) == number of rows
    len(table[0]) == number of columns IF all
    inner lists are of same length
    '''
    return(len(table), len(table[0]))

def rows_and_cols(table):
    '''walk thru a table (2 dimensional list)
    and print it in tabular format.
    '''
    row_num = 0
    for row in table:
        print("row: ", row_num, end = ': ') # do something at start of each row
        for cell in row:
            print(cell, end = ' ')          # do something with each cell
        row_num += 1                        # do something at end of each row
        print()

def rows_and_cols_by_index(table):
    '''walk thru a multi-dimensional table using
    indexes.  The code below should have exactly the
    same effect as rows_and_cols() above.
    '''
    for row_index in range(len(table)):
        print("row: ", row_index, end = ': ')       # do something at start of each row
        col_width = len(table[row_index])           # equals the number of elements in the current row
        for col_index in range(col_width):
            print(table[row_index][col_index], end = ' ')   # do something with each cell
        print()                             # do something at end of each row

def create_card_deck():
    deck = []
    for rank in [2,3,4,5,6,7,8,9,10, 'J', 'Q', 'K', 'A']:
        for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
            card = (rank, suit)
            deck.append(card)
    return deck

def basic_while_loop(limit):
    i = 0
    while i < limit:
        print(i)
        i += 1

def infinite_loop():

    while True:
        print('Use ctrl-c to stop')

def until_str(a_list):
    '''sum up the entries of a list until a string
    is found. Demonstrate walking a list with while
    instead of a for loop
    '''
    index = 0
    total = 0
    while index < len(a_list):
        if type(a_list[index]) != str:
            total += a_list[index]
        else:
            break;
        index += 1
    return total

# -----------------------------------
# Dictionaries
# -----------------------------------
prices = {
    'apple' : 3.99,
    'potato' : 0.99,
    'carrot' : 1.50,
    'onion' : 2.50
}

def price_check(price_data):
    items = sorted(price_data.keys())
    print("select from:")
    for product in items:
        print(product)
    print()
        
    choice = ''
    while choice != 'STOP':
        choice = input("Enter an item: ")
        if choice != 'STOP':
            if choice in price_data:
                price = price_data[choice]
                print(f'price of {choice} is {price}')
            else:
                print(f'sorry, we have no {choice}')

def demo_dictionary_functions():
    has_apple = 'apple' in prices
    print(f'apple in prices: {has_apple}')

    # add an item to a dictionary
    prices['banana'] = 0.69

    # visit each item in a dictionary (1)
    for key in prices:
        print(key, prices[key], end = ' ')
    print()

    # visit each item in a dictionary (2)
    for key, val in prices.items():
        print(key, val, end = ' ')
    print()

# -----------------------------------
# sets
# -----------------------------------
def unique_words(text):
    words = text.split()
    u_words = set(words)
    return u_words

def demo_sets():
    data = "this is the test text and is the text we will test"
    a_set = unique_words(data)
    print(f'data contains {len(a_set)} unique words')
    print('About to add "magic" 10 times')
    for i in range(10):
        a_set.add('magic')
    print(f'Count is now: {len(a_set)}')

def demo_sets_2():
    '''Demonstrate set operations'''
    purchase_a = {'apple', 'banana', 'carrot'}
    purchase_b = {'apple', 'orange'}
    print('purchase_a:', purchase_a)
    print('purchase_b:', purchase_b)
    print(1, '  |  ', purchase_a | purchase_b)             # the combined set 
    print(2, 'union', purchase_a.union(purchase_b))        # same as 1

    print(3, '     &      ', purchase_a & purchase_b)             # common elements
    print(4, 'intersection', purchase_a.intersection(purchase_b))  # same as 4

    print(5, "'apple' in purchase_a:", 'apple' in purchase_a) # membership test
    print(6, ' ^ ', purchase_a ^ purchase_b)  # unique items from both sets
    print(7, 'a.difference(b)', purchase_a.difference(purchase_b))  # what does a have that b doesn't
    print(8, 'b.difference(a)', purchase_b.difference(purchase_a))   # what does b have that a doesn't


# -----------------------------------
# tuples
# -----------------------------------
def demo_tuples():
    '''Also see min_max() below for more
    use of tuples
    '''
    t = ('value 1', 'value 2')
    print(f't[0]: {t[0]} t[1]: {t[1]}')

    x, y = ('value 1', 'value 2')
    print(f'   x: {x}    y: {y}')
    try:
        t[1] = 'fail!'
    except TypeError:
        print('As expected, tuples are immutable!')

# -----------------------------------
# calling functions from other
# functions.
# -----------------------------------
def min_max(a_list):
    '''Return the lowest and the highest 
    value in the provided list, as a tuple.
    using sorted() instead of a_list.sort()
    allows us to avoid changing the input
    '''
    sorted_list = sorted(a_list)
    return (sorted_list[0], sorted_list[-1])

def demo_min_max():
    '''Show how min_max() works.
    Also demonstrates receiving 2 values
    back from a function
    '''
    min, max = min_max([1,6,12,2,7,5])
    print(f'min: {min} max: {max}')

    min, max = min_max(['car', 'house', 'cat', 'hat'])
    print(f'min: {min} max: {max}')

# -----------------------------------
# file I/O
# -----------------------------------
def read_a_file(file_name):
    '''read the lines of a file and write them
    to the screen. "end = '' " is used because the
    text lines already contain new-line ('\n')
    characters.
    '''
    try:
        with open(file_name, 'r') as in_file:
            all_lines = in_file.readlines()
        for line in all_lines:
            print(line, end = '')
    except OSError as e:
        print(f'Unable to read file: {e}')

def write_a_file(file_name, a_list):
    '''Writes the elements of the given list
    to the given file, 1 element per line.
    '''
    try:
        with open(file_name, 'w') as out_file:
            for token in a_list:
                out_file.write(str(token) + '\n')
    except:
        print('A problem occurred writing to the file')

# -----------------------------------
# compound conditions
# -----------------------------------
def demo_conditions(x, y, z):
    '''demonstrates tying conditions together with
    'and' and 'or'
    '''
    if (x == y) or (y == z) or (x == z):
        print('at least 2 are the same')
    else:
        print('all 3 are different')
    if (x == y) and (y == x):
        print('all are the same')

def demo_conditions_2(x, y, z):
    '''Same as above but with line continuation character'''
    if (x == y) or \
       (y == z) or \
       (x == z):
        print('at least 2 are the same')
    else:
        print('all 3 are different')
    if (x == y) and \
       (y == x):
        print('all are the same')

if __name__ == '__main__':
    demo_conversions()
    demo_strings('this is my test text')
    print_demos()
    demo_list_loop()
    demo_range_loop()
    demo_string_loop()
    process_two_lists()
    return_dimensions(grades)
    rows_and_cols(grades)
    rows_and_cols_by_index(grades)
    create_card_deck()
    basic_while_loop(5)
    until_str([1,2,3,4,'red',5,6])
    price_check(prices)
    demo_dictionary_functions()
    print(unique_words('this is where this is stopping'))
    demo_sets()
    demo_sets_2()
    demo_tuples()
    demo_min_max()
    read_a_file('review-examples.py')
    write_a_file('dvw-review-out.txt', [1, 'dog', 47])
    print()
    demo_conditions(1,2,3)
    demo_conditions(3,3,3)
    demo_conditions(2,2,3)
    demo_conditions_2(2,2,3)
