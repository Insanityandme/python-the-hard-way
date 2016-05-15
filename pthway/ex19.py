# defines a function by the name cheese_and_crackers with two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# calls the cheese_and_crackers function with two arguments 20, 30
cheese_and_crackers(20, 30)

# store two values in variables
amount_of_cheese = 20
amount_of_crackers = 30

# call the function with the two variables as arguments above
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
