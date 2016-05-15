def get_count(words):
    try:
        dict = {}
        v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        c = ['b', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'x', 'y', 'z', 'B', 'D', 'F', 'G',
                     'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 
                     'U', 'V', 'X', 'Y', 'Z']
        vowel_count = [words.count(vowel) for vowel in v if vowel in words]
        cons_count = [words.count(consonant) for consonant in c if consonant in words]
        dict['vowels'] = sum(vowel_count)
        dict['consonants'] = sum(cons_count)


    except TypeError:
        print "oops"

    print dict


get_count()
