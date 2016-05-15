people = 50
cars = 40
trucks = 15

# Checks if the the integer stored in cars is greater
# than the integer stored in people
# Returns true and executes the block of code.
if cars > people:
    print "We should take the cars."
# Allows for another conditional statement with the name of elif
# If the if function above returns false, this one will be checked,
# If this one is true then the block of code will be executed.
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if trucks > cars:
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."

if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."

if cars > people or trucks < cars:
    print "something is up!"
