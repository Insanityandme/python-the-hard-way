import random

HANGMANPICS = ["""
  ----------
  |/       |
  |
  |
  |
  |
  |
__|__""", 
"""
  ----------
  |/       |
  |       ( )
  |
  |
  |
  |
__|__""", 
"""
  ----------
  |/       |
  |       ( )
  |       \|
  |
  |
  |
__|__""", 
"""
  ----------
  |/       |
  |       ( )
  |       \|/
  |        
  |
  |
__|__""", 
"""
  ----------
  |/       |
  |       ( )
  |       \|/
  |        |
  |        
  |
__|__""", 
"""
  ----------
  |/       |
  |       ( )
  |       \|/
  |        |
  |       /
  |
__|__""", 
"""
  ----------
  |/       |
  |       ( )
  |       \|/
  |        |
  |       / \\
  |
__|__"""]

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def get_random_word(wordlist):
    return random.choice(wordlist)

def display_board(HANGMANPICS, missedletters, correctletters, secretword):
    print HANGMANPICS[len(missedletters)]

    print 'Missed letters: ', ', '.join(missedletters)

    blanks = "_" * len(secretword)

    for i in range(len(secretword)):
            if secretword[i] in correctletters:
                blanks = blanks[:i] + secretword[i] + blanks[i+1:]

    print ''.join(blanks)

def get_guess(alreadyguessed):
    while True:
        guess = raw_input("Guess a letter: ")
        guess = guess.lower()
        if len(guess) != 1:
            print "Please enter a single letter"
        elif guess in alreadyguessed:
            print "You've already guessed this"
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print "That's not a letter, please enter a letter."
        else: 
            return guess

def play_again():
    input = raw_input("Do you wanna play again? Yes or no? ")
    return input.lower().startswith('y')

print "H A N G M A N"
missedletters = ''
correctletters = ''
secretword = get_random_word(words)
game_is_done = False

while True:
    display_board(HANGMANPICS, missedletters, correctletters, secretword)

    guess = get_guess(missedletters + correctletters)

    if guess in secretword:
        correctletters = correctletters + guess

        found_all_letters = True
        for i in range(len(secretword)):
            if secretword[i] not in correctletters:
                print correctletters
                found_all_letters = False
                break
        if found_all_letters:
            print "Yes! The secret word is: %s! You have won!" % secretword
            game_is_done = True
    else: 
        missedletters = missedletters + guess

        if len(missedletters) == len(HANGMANPICS) - 1:
            display_board(HANGMANPICS, missedletters, correctletters, secretword)
            print "You have run out of guesses!\n After %s missed guesses and %s correct guesses, the word was %s" % (str(len(missedletters)), str(len(correctletters)), secretword)
            game_is_done = True

    if game_is_done:
        if play_again():
            missedletters = ''
            correctletters = ''
            game_is_done = False
            secretword = get_random_word(words)
        else: 
            break
