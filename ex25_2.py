# returns a list from a string
def list_of_words(string):
    splitted_string = string.split(' ')
    return splitted_string

# builds a new sorted list from an iterable.
# The argument can be a string as well as a list
# If it's a string it returns a list of sorted letters
# If it's a list, the actual list becomes sorted in alphabetical order
def sort_list_or_string(string_or_list):
    return sorted(string_or_list)

# IF you get the error 'str' object has no attribute 'pop'
# pop cannot be used on a string, but a list. 
# So you have to make it a list first ^_^
# That is why we have break_words(words), to split it up into a list. 
def print_first_word(list):
    pop = list.pop(0)
    print "this prints the first word in a list: %s" % pop

def print_last_word(list):
    pop = list.pop(-1)
    print "this prints the last word in a list: %s" % pop

# Sorts a string
def sort_sentence(sentence):
    words = list_of_words(sentence)
    return sort_list_or_string(words)

def print_first_and_last_word(list):
    print_first_word(list)
    print_last_word(list)

def print_first_and_last_sentence_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
    
sentence = "hi, how are you"
list = list_of_words(sentence)

print "This is the sentence: %s" % sentence
print "This is a sorted string: %s" % sort_list_or_string(sentence)
print "This is a sorted list: %s" % sort_list_or_string(list)

# print_first_word(list)
# print_last_word(list)

print_first_and_last_word(list)

# print_first_and_last_sentence_sorted(sentence)

# Beware of pop "popping" a word off if you plan to call 
# the functionc containing pop inside of another function
