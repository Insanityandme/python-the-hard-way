# A parameter name that begins with * gathers arguments into a tuple.
# The complement of gather is scatter, ex:
# t = (7, 3)
# divmod(t) returns error, expected 1 argument.
# but if you scatter the tuple, it works:
# divmot(*t)
# returns (2, 1)


def sumall(*args):
    return sum(args)


print sumall(1, 2, 3, 4, 5)
