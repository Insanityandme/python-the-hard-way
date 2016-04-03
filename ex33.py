# def loop(stop, increment):
#    i = 0
#    numbers = []
#
 #   while i < stop:
 #       print "At the top of i is %d" % i
  #      numbers.append(i)
#
 #       i = i + increment
#
 #       print "Numbers now: ", numbers
  #      print "At the bottom of i is %d" % i
#
 #   for num in numbers:
  #      print num 
#
# print loop(6, 1)

def loop2(start, stop, increment):
    numbers = []

    for i in range(start, stop, increment):
        print "Adding %d to the list." % i
        numbers.append(i)
        print "Numbers now: ", numbers
        print "At the bottom of i is %d" % i

    for num in numbers:
        print num

loop2(0, 6, 1)
