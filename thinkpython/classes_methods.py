class Point(object):
    """Represents an object in 2-d space

    attributes: x, y
    """
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return '%.2d, %.2d' % (self.x, self.y)

    def __add__(self, other):
        if isinstance(other, Point):
            return self.add_point(other)
        else:
            return self.add_tuple(other)

    def __radd__(self, other):
        return self.__add__(other)

    def add_point(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return x, y

    def add_tuple(self, tuple):
        x, y = tuple
        x += self.x
        y += self.y
        return x, y


class Time(object):
    """Represents a time object.

    attributes: hour, minutes, seconds
    """
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    # def __add__(self, other):
    #   seconds = self.time_to_int() + other.time_to_int()
    #   return int_to_time(seconds)
    # Type-based dispatch
    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        return self.__add__(other)

    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()


def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


# Functions that can work with several types are called polymorphic.
# Polymorphism can facilitate code reuse.
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] = d[c]+1
    return d


def print_attributes(obj):
    for attr in obj.__dict__:
        print attr, getattr(obj, attr)


start = Time()
start.hour = 59
start.minute = 20
start.second = 20

point = Point()
p1 = Point(10, 20)
p2 = Point(20, 40)
point.x = 10
point.y = 20

print point
print p1 + p2

print start
end = start.increment(200)
print end

print start.time_to_int()

print end.is_after(start)

start = Time(9, 45)
end = Time(1, 35)
print start + end
print start + 1337
print 1337 + start

p3 = Point(1, 2)
p4 = Point(20, 5)
print p3 + p4
print p3 + (10, 5)

print print_attributes(p4)
