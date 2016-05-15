# Commands to remember
# close - Closes the file. Like File->Save in your editor.
# read - Reads the contents of the file. You can assign the result to a variable.
# readline - Reads just one line of a text file.
# truncate - Empties the file. Watch out if you care about the file.
# write('stuff') - Writes "stuff" to the file.

# import the argv module that takes arguments from the command line
from sys import argv

# 
script, filename = argv

print "We're going to erase %r. " % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you don't want that, hit RETURN. "

# prompts you to continue if you press RETURN/ENTER or CTRL-C to close
raw_input("?")

# opens the file object specified at the command line
print "Opening the file..."
target = open(filename, 'w')

# Apparentely you don't need to truncate files 
# because using 'w' in the open function already does that for you.
# Empties the file.
# print "Truncating the file. Goodbye!"
# target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
all_lines = line1 + "\n" + line2 + "\n" + line3 + "\n"

print "Now I'm going to write these to the file."

# Writes stuff to the file in filename
target.write(all_lines)

print "Let me print that for you so you can see what is up."

target = open(filename)
print target.read()

raw_input("Feeling done?")

print "And finally, we close it."
target.close()
