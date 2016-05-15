import random


def sort_by_length_random(words):
    t = []
    for word in words:
        t.append((len(word), word))

    def compare(a, b):
        return random.randint(-1, 1) if a[0] == b[0] else cmp(a, b)

    t.sort(cmp=compare, reverse=True)

    res = []
    for length, word in t:
        res.append(word)
    return res


def main():
    words = ['lol', 'lol', 'anus', 'penis', 'wat', 'lol', 'shoo', 'poop',
             'majs', 'bold', 'majs', 'penis', 'anus', 'shi', 'ha', 'moo']
    t = sort_by_length_random(words)
    for x in t:
        print x

if __name__ == '__main__':
    main()
