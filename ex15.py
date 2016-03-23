from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r: " % filename
print txt.read()

print "Type the filename again: "
second_file = raw_input("> ")

txt_again = open(second_file)

print txt_again.read()
