# Import the argv module so that we can get
# arguments from the command line.
from sys import argv

# script = argv[0], filename = argv[1]
# argv[0] is the name of the script and
# argv[1] is the first argument given,
# in this case, the file's name. 
script, filename = argv

# Opens a file, returning a file object 
# in this case we are storing it in the txt variable
txt = open(filename)

# Using print statement and the specifier %r 
# we print the filename given in the command line. 
print "Here's your file %r: " % filename

# Reads the file object called txt and returns its content as a string.
print txt.read()

# Reads a string from your input and stores it inside second_file
# > is added to simulate a prompt. 
print "Type the filename again: "
second_file = raw_input("> ")

# Stores the content of second_file and opens the file object.
txt_again = open(second_file)

# Reads the file object called txt_again and returns its content as a string.
print txt_again.read()

txt.close()
txt_again.close()

# The reason why I think raw_input is better is because you can get 
# instructions beforehand, telling you what you need to do. 

