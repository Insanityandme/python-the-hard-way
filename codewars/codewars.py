def order(sentence):
    words_numbers = []
    words = sentence.split()

    words_numbers = [(w, int(c)) for w in words for c in w if c.isdigit()]

    new_sorted = sorted(words_numbers, cmp=lambda a, b: a[1]-b[1])
    new_words = map(lambda a: a[0], new_sorted)

    return ' '.join(new_words)

print order("is9 anus2 kuk3")
