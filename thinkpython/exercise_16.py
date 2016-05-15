import datetime as dt


class Time(object):

    def __init__(self, day=None, hour=None, minute=None, second=None):
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '{}:{}:{}:{}'.format(int(self.day), int(self.hour),
                                    int(self.minute), int(self.second))


def convert_to_datetime(birthday):
    return dt.datetime.strptime(birthday, '%Y-%m-%d')


def current_date():
    return dt.datetime.today()


def current_birthday(birthday):
    birthday = convert_to_datetime(birthday)
    return birthday.replace(current_date().year)


def time_to_int(birthday):
    return birthday.total_seconds()


def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    hours, time.minute = divmod(minutes, 60)
    time.day, time.hour = divmod(hours, 24)
    return time


def age(birthday):
    timedelta = current_date() - convert_to_datetime(birthday)
    return timedelta.days / 365


def next_birthday(birthday):
    birthday = current_birthday(birthday)
    future_bday = birthday.replace(current_date().year + 1)
    timedelta = future_bday - current_date()
    return int_to_time(time_to_int(timedelta))


def double_day(b1, b2):
    b1 = convert_to_datetime(b1)
    b2 = convert_to_datetime(b2)
    


def main():
    print "YYYY-MM-DD Format"
    b1 = raw_input("Please give me your birthday: ")
    b2 = raw_input("Now give me a friends birthday: ")

    # Gets the current date and prints the day of the week.
    print current_date().strftime("%A")

    # Takes a birthday and prints the user's age and
    # the number of days, hours, minutes and seconds
    # until their next birthday.
    print age(b1)
    b1 = next_birthday(b1)
    print "Your next birthday is in: %d days, %d hours," % (b1.day, b1.hour)
    print "%d minutes, %d seconds." % (b1.minute, b1.second)


if __name__ == '__main__':
    main()
