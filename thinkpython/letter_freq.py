

def most_frequent(string):
    dict = {}
    for letter in string:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1
    t = dict.items()
    t.sort(key=lambda x: x[1], reverse=True)
    return t


def main():
    t = most_frequent('hellooooo')
    for key, value in t:
        print "%s: %d" % (key, value)

if __name__ == '__main__':
    main()
