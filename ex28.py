# Returns True
print True and True 

# Returns False
print False and True

# Returns False
print 1 == 1 and 2 == 1

# Returns True
print "test" == "test"

# Returns True
print 1 == 1 and 2 != 1

# Returns True
print True and 1 == 1

# Returns False
print "test" == "testing"

# Returns False
print 1 != 0 and 2 == 1

# Returns True
print "test" != "testing"

# Returns False
print "test" == 1

# Returns True
print not(True and False)

# Returns False
print not(1 == 1 and 0 != 1)

# Returns True 
print not(10 == 1 or 1000 == 4000)

# Returns False
print not(1 != 10 or 3 == 4)

# Returns True
print not("testing" == "testing" and "Zed" == "Cool Guy")

# Returns True 
print 1 == 1 and (not("testing" == 1 or 1 == 0))

# Returns False 
print "chunky" == "bacon" and (not(3 == 4 or 3 == 3))

# Returns False
print 3 == 3 and (not("testing" == "testing" or "Python" == "Fun"))


