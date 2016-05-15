def add(a, b):
    print "ADDING: %d + %d" % (a ,b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING: %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING: %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING: %d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, Iq: %d)" % (age, height, weight, iq)

print "Here is a puzzle."

puzzle = add(age, subtract(height, multiply(weight, divide(iq, 2))))
# The formula in it's normal state
age + (height - weight * iq / 2)
(30+5) + (78-4) - (90*2) *  (100/2)/2

print "That becomes: ", puzzle, "can you do it by hand?"

print "Here is another puzzle."

# 60 + 5 * 25 - 3 / 104 - 4
# number1 = add(60, 5)
# number2 = subtract(25, 3)
# number3 = subtract(104, 4)
# puzzle_2 = divide(multiply(number1, number2), number3)

# 180 + 5 / 10 / 5 * 205 - 333 + 444 + 444
number1 = add(180, 5)
number2 = divide(10, 5)
number3 = subtract(205, 333)
number4 = add(444, 444)
puzzle_3 = multiply(divide(number1, number2), add(number3, number4))

print "That becomes: ", puzzle_3, "Jesus christ amazing."
