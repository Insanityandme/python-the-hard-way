class Time(object):
    """Represents the time of the day:

    attributes: hour, minute, second
    """
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __gt__(self, other):
        self = self.hour, self.minute, self.second
        other = other.hour, other.minute, other.second
        return (self > other)

    def __str__(self):
        return '{}:{}:{}'.format(self.hour, self.minute, self.second)

    def __cmp__(self, other):
        t1 = time_to_int(Time(self.hour, self.minute, self.second))
        t2 = time_to_int(Time(other.hour, other.minute, other.second))
        return cmp(t1, t2)


def print_time(time):
    print "%.2d:%.2d:%.2d" % (time.hour, time.minute, time.second)


# Function not necessary, implemented in the Time class
def is_after(t1, t2):
    # Own solution, sry outwitted by sebastian book
    # (t1) = t1.hour, t1.minute, t1.second
    # (t2) = t2.hour, t2.minute, t2.second
    return t2 > t1


# Pure function why?
# Because it does not modify any of the objects passed to it as arguments
# and it has no effect, like displaying a value or getting user input,
# other than returning a value.
def add_time(t1, t2):
    hour = t1.hour + t2.hour
    minute = t1.minute + t2.minute
    second = t1.second + t2.second
    if second >= 60:
        second -= 60
        minute += 1
    if minute >= 60:
        minute -= 60
        hour += 1
    return Time(hour, minute, second)


# This function is called a modifier, use this when you see a clear advantage.
# When you want to modify the object it gets as paramenters.
def increment(time, seconds):
    time.second += seconds

    if time.second >= 60:
        time.minute += time.second/60
        time.second = time.second % 60

        if time.minute >= 60:
            time.hour += time.minute/60
            time.minute = time.minute % 60

    return time


# A "pure" version of increment that creates and returns
# a new Time object rather than modifying the parameter
def increment_pure(time, seconds):
    hour = time.hour
    minute = time.minute
    second = time.second + seconds

    if second >= 60:
        minute += second/60
        second = second % 60

        if minute >= 60:
            hour += minute/60
            minute = minute % 60

    return Time(hour, minute, second)


# Planned development, (see http://en.wikipedia.org/wiki/Sexagesimal)!
def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


def improved_add_time(t1, t2):
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)


def improved_increment(time, seconds):
    seconds = time_to_int(time) + seconds
    return int_to_time(seconds)


def mul_time(time, number):
    seconds = time_to_int(time) * number
    return int_to_time(seconds)


def avg_time(time, miles):
    pace = time_to_int(mul_time(time, 2)) / miles
    return int_to_time(pace)


def main():
    time = Time(11, 59, 30)
    t1 = Time(10, 59, 30)
    t2 = Time(10, 58, 50)

    start = Time(1, 45, 0)
    duration = Time(1, 35, 0)

    done = add_time(start, duration)
    print_time(done)

    print_time(time)
    print_time(t1)
    print_time(t2)
    print is_after(t1, t2)
    print t2 > t1

    print increment(t1, 30)
    print increment(t1, 30)
    print increment_pure(time, 30)
    print increment_pure(time, 60)

    print time_to_int(time)
    print int_to_time(time_to_int(time))
    print improved_increment(time, 0)
    print mul_time(time, 2)
    print mul_time(time, 2)

    print avg_time(time, 100), "per mile"

    t3 = Time(10, 30, 30)
    t4 = Time(9, 20, 40)
    print cmp(t4, t3)

if __name__ == '__main__':
    main()
