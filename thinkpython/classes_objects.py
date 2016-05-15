import math
import copy


# User-defined types
class Point(object):
    """Represents a point in 2-D space."""


def print_point(p):
    print "(%g, %g)" % (p.x, p.y)


class Rect(object):
    """Represents a rectangle.

    attributes: width, height, corner
    """


def distance_between_points(p1, p2):
    """Computes the distance between two Point objects."""
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    dist = math.sqrt(dx**2 + dy**2)
    return dist


def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2.0
    p.y = rect.corner.y + rect.height/2.0
    return p


def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight


def move_rectangle(rect, dx, dy):
    """Move the rectangle object by modyfing its corner object.

    rect: Rectangle object.

    dx: change in x coordinate (can be negative).
    dy: change in y coordinate (can be negative).
    """
    rect.corner.x += dx
    rect.corner.y += dy


# Own version
def move_rectangle_copy1(rect, dx, dy):
    """Move the rectangle and return a new Rectangle object"""
    rect2 = copy.deepcopy(rect)
    rect2.corner.x += dx
    rect2.corner.y += dy
    return rect2


# Books version
def move_rectangle_copy2(rect, dx, dy):
    new = copy.deepcopy(rect)
    move_rectangle(new, dx, dy)
    return new


# Attributes
p = Point()
p.x = 2.0
p.y = 5.0
y = p.y
x = p.x

# Rectangles
box = Rect()
box.width = 200.0
box.height = 100.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

# Instances as return values
center = find_center(box)
print_point(center)

# Objects are mutable
grow_rectangle(box, 50, 100)
print box.width
print box.height

print box.corner.x
print box.corner.y
print_point(center)

move_rectangle(box, 20, 40)

print box.corner.x
print box.corner.y
center2 = find_center(box)
print_point(center2)

# Copying
p1 = Point()
p1.x = 3.0
p1.y = 4.0
# Shallow copy, does not copy embedded objects
p2 = copy.copy(p1)

box2 = copy.copy(box)
box2 is box  # False
box2.corner is box.corner  # True

# Deep copy copies not only the objects but also the objects it refers to,
# and the objects they refer to, and so on.
box3 = copy.deepcopy(box)
box3 is box  # False
box3.corner is box.corner  # False

# Debugging
p = Point()
print p.z  # AttributeError: Point instance has no attribute 'z'
# If you are not sure what type an object is, you can ask:
type(p)
# <type '__main__.Point'>
# If you are not sure whether an object has a particular attribute, you can use
# the built-in function hasattr:
hasattr(p, 'x')  # True
hasattr(p, 'z')  # True

# Glossary
# class: A user-defined type. A class definition creates a new class object.
# class object: An object that contains information
# about a user-defined type.
# The class object can be used to create instances of the type.
# instance: An object that belongs to a class.
# attribute: One of the named values associated with an object.
# embedded (object): An object that is stored
# as an attribute of another object.
# shallow copy: To copy the contents of an object,
# including any references
# to embedded objects; implemented by the copy function in the copy module.
# deep copy: To copy the contents of an object as well as any embedded objects,
# and any objects embedded in them, and so on;
# implemented by the deepcopy function in the
# copy module.
# object diagram: A diagram that shows objects,
# their attributes, and the values of the attributes.
