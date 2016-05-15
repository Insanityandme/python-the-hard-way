from sys import exit
from time import sleep
import random

def hangman():
    hangman_top = """  H A N G M A N
  -------------
  |/          |\n"""
    hangman_middle = "  |\n"
    hangman_middle_2 = "  |\n"
    hangman_middle_3 = "  |\n"
    hangman_middle_4 = "  |\n"
    hangman_end = """  |
__|__"""

    #secret_words = ['hamburger', 'libanese', 'masculine', 'moose', 'anus', 'contemporary', 'hate', 'heart', 'disease', 'inflammation', 'love']
    words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()
    secret_word = random.choice(words)

    space = ['_']
    field = space * len(secret_word)

    wrong_counter = 0
    wrong_list = []

    print hangman_top, hangman_middle, hangman_middle_2, hangman_middle_3, hangman_middle_4, hangman_end
    print "Missed letters:", ', '.join(wrong_list)
    print ''.join(field)
    
    while True:
        guess = raw_input("Guess a letter: ")

        if guess.isupper() == True:
            guess = guess.swapcase()
            print "** It's better if you type in lowercase, but I'll convert it for you =)."

        for n in secret_word:
            if guess in n:
                pos = [pos for pos, letter in enumerate(secret_word) if letter == guess]
                for i in pos:
                    field[i] = guess

        if guess not in secret_word:
            if guess not in wrong_list:
                wrong_list.append(guess)
                wrong_counter += 1
            else:
                print "You've already tried the letter %s." % guess
        
        if wrong_counter == 1:
            hangman_middle = "  |          (_)\n"
        elif wrong_counter == 2:
            hangman_middle_2 = "  |          \|\n"
        elif wrong_counter == 3:
            hangman_middle_2 = "  |          \|/\n"
        elif wrong_counter == 4:
            hangman_middle_3 = "  |           |\n"
        elif wrong_counter == 5:
            hangman_middle_4 = "  |          /  \n"
        elif wrong_counter == 6:
            lost()
            wrong_counter = 0
            hangman_middle_4 = "  |          / \ \n"

            print hangman_top, hangman_middle, hangman_middle_2, hangman_middle_3, hangman_middle_4, hangman_end
            print "Missed letters:", ', '.join(wrong_list)
            print ''.join(field)
            print "The word was: ", secret_word

            choice = raw_input("You lost, wanna try again? ")
            if choice == 'yes':
                print "let's go again!"
                hangman()
            elif choice == 'no':
                exit(0)
        else:
            pass

        if "_" not in field:
            print hangman_top, hangman_middle, hangman_middle_2, hangman_middle_3, hangman_middle_4, hangman_end
            print "Missed letters:", ', '.join(wrong_list)
            print "word: ", ''.join(field)
            win()

        print hangman_top, hangman_middle, hangman_middle_2, hangman_middle_3, hangman_middle_4, hangman_end
        print "Missed letters:", ', '.join(wrong_list)
        print ''.join(field)

def win():
    print "You're awesome you won!"
    exit(0)

def lost():
    sleep(1)
    jagger = """
                    _____    ____
                 .#########.#######..
              .#######################.
            .############################.
           .################################.
          .#########,##,#####################.
         .#########-#,'########## ############.
        .######'#-##' # ##'### #. `####:#######.
        #####:'# #'###,##' # # +#. `###:':######
       .####,'###,##  ###  # # #`#. -####`######.
      .####+.' ,'#  ##' #   # # #`#`.`#####::####
      ####'    #  '##'  #   #_'# #.## `#######;##
      #:##'      '       #   # ``..__# `#######:#
      #:##'  .#######s.   #.  .s######.\`#####:##
      #:##   ."______""'    '""_____"". `.#####:#
     .#:##   ><'(##)'> )    ( <'(##)`><   `####;#
     ##:##  , , -==-' '.    .` `-==- . \  ######'
     #|-'| / /      ,  :    : ,       \ ` :####:'
     :#  |: '  '   /  .     .  .  `    `  |`####
     #|  :|   /   '  '       `  \   . ,   :  #:# 
     #L. | | ,  /   `.-._ _.-.'   .  \ \  : ) J##
    ###\ `  /  '                   \  : : |  /##
     ## #|.:: '       _    _        ` | | |'####
     #####|\  |  (.-'.__`-'__.`-.)   :| ' ######
     ######\:      `-...___..-' '     :: /######
     #######\``.                   ,'|  /#######
    .# ######\  \       ___       / /' /#######
    # #'#####|\  \    -     -    /  ,'|### #. #.
    `#  #####| '-.`             ' ,-'  |### #  #
        #' `#|    '._         ,.-'     #`#`#.
             |       .'------' :       |#   #
             |       :         :       |
             |       :         :       |
                     :         :
                     I see you"""
    print jagger
    
hangman()
