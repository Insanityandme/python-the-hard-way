# Imports the argv module so we can use additional arguments in the command line
from sys import argv

# script = argv[0],
# input_file = argv[1]
# the first one is the files name
# second one is the first argument, which is another file in this case!
script, input_file = argv

# a function taking one argument and returns 
# its content as a string using the read() function
def print_all(f):
    print f.read()

# Makes you point at the beginning of the file again, because 0
# It's important to note that its syntax is as follows:
# fp.seek(offset, from_what)
# where fp is the file pointer you're working with; 
# offset means how many positions you will move;
# from_what defines your point of reference
# 0: means your reference point is the beginning of the file
# 1: means your reference point is the current file position
# 2: means your reference point is the end of the file
def rewind(f):
    f.seek(0)

# prints your current line and prints out the contents of that line.
def print_a_line(line_count, f):
    print line_count, f.readline()

# opens the input_file of your choosing and stores it in current_file
current_file = open(input_file)

print "First let's print the whole file:\n"

# calls the function and print it's content
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# "rewinds" your point of reference back to the beginning of the file
rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

