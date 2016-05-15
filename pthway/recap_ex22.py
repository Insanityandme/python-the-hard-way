from sys import argv
import datetime

script, in_file, out_file = argv

print "calling on: %s, in_file: %s, out_file: %s)" % (script, in_file, out_file)

f = open(in_file, 'w+')
f2 = open(out_file, 'w+')

write_to_file = f.write(raw_input("Write something in here please: "))

f.seek(0)
read_file = f.read()
print "%s: %s"  % (in_file, read_file)

f2.write(read_file)
f2.seek(0)
read_file_2 = f2.read()
print "%s: %s" % (out_file, read_file)

d = datetime.date.today()
print str(d)
print repr(d)

print 5 > 2
print 5 < -2
print 5 >= 5
print 5 <= -2

string = "This is a string"
addition = 2+2
subtraction = 2-2
divison = 2/2
multiply = 2*2
modulus = 16 % 4

# print "addition: 2+2 = %d\n subtraction: 2/2 = %d\n divison: 2/2 = %d\n multiplication: 2*2 = %d\n modolus: 16 % 4 = %d" % (addition, subtraction, divison, multiply, modulus)
print "addition: 2+2 = %d\nsubtraction: 2-2 = %d\ndivsion: 2/2 = %d\nmultiplication: 2*2 = %d\nmodulus: 16 %% 4 = %d" % (addition, subtraction, divison, multiply, modulus)
print "16 % 4"
# print "\n, \t, \f, \a, \ooo, \v, \uxxxx, \Uxxxxxxxx, \xhh, \r, \\, \', \", \b" 

def add(arg1, arg2):
    print "ADDING: %d + %d" % (arg1, arg2)
    return arg1 + arg2

def subtract(arg1, arg2):
    print "SUBTRACTING: %d - %d" % (arg1, arg2)
    return arg1 - arg2

def multiply(arg1, arg2):
    print "MULTIPLYING: %d * %d" % (arg1, arg2)
    return arg1 * arg2

def division(arg1, arg2):
    print "DIVIDING: %d / %d" % (arg1, arg2)
    return arg1 / arg2

age = add(30, 5)
weight = subtract(78, 4)
height = multiply(90, 2)
poop_size = division(100, 2)

formatter = "%r\n%r\n%r\n%r"
print formatter % (age, weight, height, poop_size)

puzzle = add(multiply(age, weight), division(height, poop_size))

print puzzle

   

