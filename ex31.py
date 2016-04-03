print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear eating a cheese cake. What do you do?"
    print "1. Take the cake"
    print "2. Scream at the bear"

    bear = raw_input("> ")

    if bear == "1":
        print "The bear silently smirks at you, feeling deprived of sugar decides to walks away."
        print "A new adventure awaits you, how are you going to proceed?"
        print "1. Eat a snickers bar and end the game."
        print "2. Rate your professor @ rateyourprofessor.com to let him know that he should practice teaching."
        print "3. Leave the dark room and proceed into the vastness of space."

        future = raw_input("What will you do mighty warrior? ")

        if future == "1":
            print "\"mmmmmmm, yum yum\""
        elif future == "2":
            print "Somehow your professor finds out it was you who rated him and are now giving you D- all year \'round."
        elif future == "3":
            print "Much like the movie gravity you float into space where the only sounds you can hear is the *muffling* of your space suit, on top of that you realise that you only have 30 more seconds to live. Tops 1 minute."
        else: 
            print "What the hell are you doing? Pick something for god's sake! Oh well, game over."


    elif bear == "2":
        print "The bear eats your face off. Good job!"
    else: 
        print "well doing %s is probably better." % bear

elif door == "2":
    print "You stare into the endless abyss of Cthulhu's retina."
    print "1. Blueberries"
    print "2. Yellow jacket clothespins"
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2": 
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"

else:
    print "You stumble around and fall on a knife and die. Good job!"


