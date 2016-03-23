# print "How old are you?",
# age = raw_input()
# print "How tall are you?",
# height = raw_input()
# print "How much do you weigh?",
# weight = raw_input()

# print "So, you're %s old, %s tall, %s heavy." % (age, height, weight)

# name = raw_input('Enter your name: ')
# print "Hi %s, Let us be friends!" % name

print (30 * '-')
print ("    H A R D Q U E S T I O N S")
print (30 * '-')
print ("1. What is the capital of Sweden?")
print ("2. Who shot kennedy?")
print ("3. What is 5+5?")
print (30 * '-')

# Robust error handling
# Only accepts int
# Wait for valid input in while...not
is_valid = 0

while not is_valid:
    try: 
        choice = int(raw_input('Enter your choice [1-3] : '))
        is_valid = 1 # set it to 1 to validate input and to terminate the while..not loop
    except ValueError, e:
        print "%s is not a valid integer." % e.args[0].split(": ")[1]

# Take action as per selected menu-options
if choice == 1:
    answer = raw_input('Give me your answer : ')
    if answer in ['Stockholm', 'stockholm']:
        print "Fuck yeah you got it!"
    else:
        print "Sorry, next time bby"
elif choice == 2:
    answer = raw_input('Give me your answer : ')
    if answer in ['none', '0', 'None']:
        print "Fuck yeah you got it!"
    else: 
        print "Sorry, next time bby"
elif choice == 3:
    answer = raw_input('Give me your answer : ')
    if answer in ['10']:
        print "Fuck yeah you got it!"
    else: 
        print "Sorry, next time bby"
else:
    print "Invalid number. Try again..."

