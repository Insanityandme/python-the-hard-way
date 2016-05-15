from sys import exit

def and_operator(a, b, c, d):
    """(a and b) is true

    If both the operands are true then conditions becomes true
    """
    if (a == c) and (b == d):
        print "They're both true!"
    else: 
        print "It ain't true!"

def if_in_operator(a, b, match):
    """ if (a, b) matches the third argument the block of code executes

    syntax: if match in (a, b)

    """
    if match in (a, b):
        print "%s is in here!" % match
        print "Executing whatever you put in this block."
    elif a or b != match:
        print "Sorry, no execution"

def if_not_in_operator(a, b, match):
    """ if (a, b) does not match the third argument the block of code executes
    
    syntax: if match not in (a, b) 
    """

    if match not in (a, b):
        print "There's not a %s in here!" % match
        print "Executing whatever you put in here."
    elif a or b == match:
        print "Nothing is executed!"


def with_statement():
    """Simple use of with statement. It's handy when two related operations which 
    you'd like to execute as a pair, with a block of code in between.
    The classic example is opening a file, manipulating the file, then closing it: 
    
    syntax: with expression [as variable]: with-block

    """
    with open('output.txt', 'w') as f:
        f.write('Hi there!')

    print "Example syntax: with open('output.txt', 'w') as f: \n f.write('Hi there!')"


def assert_equal(a, b, c):
    """ An assertion is a sanity-check that you can turn on or off when you are done 
    with your testing of the program.

    If the expression is True then it passes, if it's False Python raises an AssertError Exception

    syntax: assert Expression[, Arguments] ([] means it's optional)

    here, if a + b == c then it passes, if not an AssertError Exception is raised.
    """
    assert a + b == c, "We've got an error here, woops."

def kelvin_to_fahrenheit(Temperature):
    """The assert statement is similar to throwing an exception if a given condition isn't true.
    An important difference is that assert statements get ignored if you compile your code with the
    optimization option. 
    This can be useful if you want to thoroughly test your code, then release and optimized version when
    you're happy that none of your assertion cases fail - when optimization is on, the __debug__
    variable becomes False and the conditions will stop getting evaluated. This feature can also catch
    you out if you're relying on the asserts and don't realise they've dissapeared. 

    In this example assert is raised when the temperature is colder than absolute zero, which isn't possible.
    """

    assert (Temperature >= 0), "Colder than absolute zero!"
    return ((Temperature-273)*1.8)+32

def break_statement_letters(letterInput):
    """It terminates the current loop and resumes execution at the next statement, 
    just like the traditional break statement in C.

    The break statement can be used in both for and while loops. 

    This example has a Python being compared to the input you've given and
    terminates the loop at the given letter you wrote. 
    
    """
    for letter in 'Python':
        if letter == letterInput:
            break
        print 'Current Letter: ', letter

def break_statement_with_while(number):
    """This example uses a While loop to print out the numbers up til 5,
    at that point the break statements terminates the loop.
    """ 
    while number > 0:
        print 'Current variable: ', number
        number -= 1
        if number == 5:
            break
    print "Good bye!"

class Customer(object):
    """A very basic example of a Class, not to be used in the real world really.
    
    A customer of ABC Bank with a checking account. Customers have the
    following properties:

    Attributes:
    name: A string representing the customer's name.
    balance: A float tracking the current balance of the customer's account.
    """

    def __init__(self, name, balance=0.0):
        """Return a Customer object whose name is *name* and starting
        balance is *balance*."""
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount*
        dollars."""
        if amount > self.balance:
            raise RunTimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        """Return the balance remaining after depositing *amount*
        dollars."""
        self.balance += amount
        return self.balance

    def balance(self):
        return self.balance

from abc import ABCMeta, abstractmethod

class Vehicle(object):
    """A vehicle for sale by Jeffco Car Dealership.

    Attributes:
        wheels: An integer representing the number of wheels the vehicle has.
        miles: The integral number of miles driven on the vehicle.
        make: The make of the vehicle as a string.
        model: The model of the vehicle as a string.
        year: The integral year the vehicle was built.
        sold_on: The date the vehicle was sold.
    """

    __metaclass__ = ABCMeta

    base_sale_price = 0
    wheels = 0

    def __init__(self,  miles, make, model, year, sold_on):
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on

    def sale_price(self):
        """Returns the sale price for this vehicle as a float amount."""
        if self.sold_on is not None:
            return 0.0 # Already sold
        return 5000.0 * self.wheels

    def purchase_price(self):
        """Returns the price for which we would pay to purchase the vehicle."""
        if self.sold_on is None:
            return 0.0 # Not yet sold
        return self.base_sale_price - (0.10 * self.miles)

    @abstractmethod
    def vehicle_type():
        """Returns a string representing the type of vehicle this is."""
        pass

class Car(Vehicle):
    """A car for sale by Jeffco Car Dealership."""

    base_sale_price = 8000
    wheels = 4

    def vehicle_type(self):
        """Returns a string representing the type of vehicle it is."""
        return 'car'

class Truck(Vehicle):
    """A truck for sale by Jeffco Car Dealership."""

    base_sale_price = 10000
    wheels = 4

    def vehicle_type(self):
        """Returns a string representing the type of vehicle it is."""
        return 'truck'

def continue_statement(letterInput):
    """This is a control flow statement that causes the program to immediately skip
    the processing of the rest of the body of the loop, for the current iteration.
    But the loop still carries on running for its remaining iterations.

    In this example you pass a string and compare it to the word Django,
    if the letter you passed contains any letter in Django the loop continues
    with the iteration of the next loop, in a sense skipping the one letter you chose.

    It can be used to avoid very deeply nested code. 
    """
    
    for letter in 'Django':
        if letter == letterInput:
            continue
        print 'Current letter: ', letter

def continue_statement_2(start, stop):
    """I still haven't found a really good real world example of using the continue statement
    more than @ stackoverflow: http://stackoverflow.com/questions/8420705/example-use-of-continue-statement-in-python
    """

    for num in range(start, stop):
        if num % 2 == 0:
            print "Found an even number", num
            continue
        print "Found a number", num

def del_variable_in_list(targetList, targetDictionary):
    """Deletion of a name removes the binding of that name from the local or global namespace 

    You use it to remove a list element

    Use the remove() method to specify what you want removed and del to specify at what place you want something removed. 
    """
    list = [1, 2, 3, 4]
    print "Before deletion", list
    del list[targetList]
    print "After deletion", list

    dictionary = {'version1': '2.7', 'version2': '3.4'}
    print "Before deletion", dictionary
    del dictionary[targetDictionary]
    print "After deletion", dictionary

def exception_example(filename):
    """This example tries to open a file where you do not
    have written permission, so it raises an exception.
    """

    try: 
        fh = open(filename, "r")
        fh.write("This is my test file for exception handling!")
    except IOError:
        print "Error: can\'t fin'd file or read data"
    else:
        print "Written content in the file successfully!"
        fh.close()

    

def exception_print_object(some_object):
    """LBYL = Look before you leap. This coding style explicitly tests for pre-conditions before making calls or lookups.
    EAFP = Easier to ask for forgiveness than permission. This common Python coding style assumes the existence of valid keys
    and attributes and catches exceptions if the assumption proves false.
    
    Check if the object is printable...
    """
    try:
        printable = str(some_object)
        print(printable)
    except TypeError:
        print "Unprintable Object"

def exception_print_object_2(some_object):

    try:
        printable = str(some_object)
    except TypeError:
        print "Unprintable Object"
    else:
        print(printable)

def exec_example(loops):
    """The exec function (which was a statement in Python 2) is used for executing a dynamically 
    created statement or program:

    program = 'i for i in range(3):\n        print "Python is Cool"'
    exec(program)
    """
    program = 'for i in range(loops):\n print "Python is Cool"'
    exec(program)

"""http://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python
To understand what yield does, you must understand what generators are, 
and before generators come iterables.
"""
def iterables(mylist):
    """Iterables: when you create a list, you can read its items one by one. Read its items
    one by one is called iteration.
    mylist is an iterable. When you use a list comprehension, you create a list, and so an iterable:
    """
    for i in mylist:
        print i
    
def iterables_2():
    """Everything you can use "for ... in" on is an iterable, lists, strings, files...
    These iterables are handy because you can read them as much as you wish, but you store all the 
    values in memory and this is not always what you want when you have a lot of values.
    """
    mylist = [x*x for x in range(3)]
    for i in mylist:
        print i

def generators():
    """Generators: generators are iterators, but you can only iterate over them once. It's because they do not store
    all the values in memory, they generate the values on the fly.
    (this shouldn't be a function, now it can be reused, it's the same as the iterables_2)

    It is just the same except you used () instead of []. BUT, you cannot perform for i in mygenerator
    a second time since generators can only be used once: they calculate 0, then forget about it and
    calculate 1, and end calculating 4, one by one.
    """
    mygenerator = (x*x for x in range(3))
    for i in mygenerator:
        print i

def create_generator():
    """Yield: Yield is a keyword that is used like return, except the function will return a generator

    Here it's a useless example, but it's handy when you know your function will return a huge set of
    values that you will only use once.
    To master yield, you must understand that when you call the function, the code you have written
    in the function body does not run. The function only returns the generator object, this is a bit tricky :-)

    example use:
    mygenerator = create_generator()
    mygenerator
    for i in mygenerator:
        print i
    """
    mylist = range(3)
    for i in mylist:
        yield i * i


import itertools

def yield_horse_race():
    """itertools, your best friend
    The itertools module contains special functions to manipulate iterables.
    Ever wish to duplicate a generator? Chain two generators? Group values in a nested list with a one liner?
    Map / Zip without creating another list?

    Then just import itertools.

    An example? Let's see the possible orders of arrival for a 4 horse race:
    """
    horses = [1,2,3,4]
    races = itertools.permutations(horses)
    for i in races:
        print i

def yield_func_without_yield():
    """When you see a function with yield statments, apply this easy trick
    to understand what will happen:
    1. Insert a result = [] at the start of the function.
    2. Replace each yield expr with result.append(expr).
    3. Insert a line return result at the bottom of the function.
    4. Yay - no more yield statements! Read and figure out code.
    5. Compare function to original definition.
    """
    result = []

    mylist = range(3)
    for i in mylist:
        result.append(i * i)

    return result

def yield_counter(maximum):
    """Here's a simple counter that increments by 1 and allows changing the value of the internal counter.
    """
    i = 0
    while i < maximum:
        val = (yield i)
        if val is not None:
            i = val
        else:
            i += 1

import sys
# Lambda functions, anonymous functions which can only take one expression. 
# Lambda functions could be hard to see the reason to use, but potentially, they are functions
# that are going to be used only once - called from only one place in your application.
lambda_multiply = lambda x: x*x
lambda_sum = lambda x,y: x + y
lambda_out = lambda *x: sys.stdout.write(" ".join(map(str,x)))


    


    
