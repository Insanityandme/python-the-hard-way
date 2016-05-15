# this is simply a variable that stores the string value of "binary"
binary = "binary"

# same as above
do_not = "don't"

# x is assigned a string, inside of it we use the specifier %d to include 10 into the string.
x = "there are %d types of people." % 10

# similar to x BUT this time % takes two arguments, binary and do_not. %d for decimals, %s for strings.
# Strings and Unicode objects have one unique built-in operation: the % operator (modulo). 
# Also known as the string formatting or interpolation operator. 
y = "Those who know %s and those who %s." % (binary, do_not)

# Example of more complex string formatting 
z = '%(language)s has %(number)03d quote types'  % {"language": "Python", "number": 2}

# Spits out the content that the variable x and y using the print statement
print x
print y

# %r specifier converts the string using repr().
print "I said: %r." % x
# %s specifier uses str()
print "I also said: '%s'." % y

# Boolean value stored in hilarious
hilarious = False
# again, using the specifier %r (repr()), I don't quite understand why %s isn't used though. 
joke_evaluation = "Isn't that joke so funny?! %r"

# spits the values using two variables.
print joke_evaluation % hilarious

# Again storing or "holding" a string value inside of w + e 
w = "This is the left side of..."
e = "a string with a right side."

# Printing both out of here. 
print w + e

print "\t"

print "### MORE COMPLEX EXAMPLES, READ COMMENTS TO UNDERSTAND"
# for some objects such as integers, they yield the same results, 
# but repr() is special in that (for types where this is possible) 
# it conventionally returns a result that is valid python syntax,
# which could be used to unambigously recreate the object it represents.
# here's an example, using a date: 
import datetime
d = datetime.date.today()
print str(d)
print repr(d)

# Example of more complex string formatting 
z = '%(language)s has %(number)03d quote types'  % {"language": "Python", "number": 2}
print z
