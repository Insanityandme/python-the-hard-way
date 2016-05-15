# Defines what a Parent is, with three functions:
# override, implicit and altered.
class Parent(object):
    
    # defines a method that prints out PARENT override
    def override(self):
        print "PARENT override()"

    # defines a method that prints out PARENT implicit()
    # this does not override anything because the Child class has no method
    # called implicit, therefor inherits this one.
    def implicit(self):
        print "PARENT implicit()"

    # defines a method that alters this method inside of the Child class
    # the super function gets the Parent version and calls it. 
    # So you'd use this to alter the behavior before or after the Parent
    # class's version runs.
    def altered(self):
        print "PARENT altered()"


class Child(Parent):

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE altered()"
        super(Child, self).altered()
        print "CHILD, AFTER altered()"


dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
