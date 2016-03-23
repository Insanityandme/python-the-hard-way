from sys import argv

script, first, second, third, fourth = argv

fourth = raw_input("What is your fourth variable? ")

# argv is supplied with data that you specify before running the program
# raw_input() is a python function, i.e. something that your program can do.
# The command line - where you the type python command in order to run your program -
# is a completely seperate thing from the program itself.
print "All together your script is called %r, first variable %r, second %r, third %r, and lastly fourth %r)" % (script, first, second, third, fourth)

