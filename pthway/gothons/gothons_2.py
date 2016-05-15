from sys import exit
from random import randint

print "### Gothons from Planet Percal #25 ###"
print "You're here to help us save this motherfucking spaceship," \
        + "there's no time to think."

print "While you're at it you need to escape through an escape pod," \
       + "welcome to buttfuck city sir."
print "Thanks, I'll see to it asap, let's fight" \
      + "these motherfucking gothons who raped my mother while I was a baby."
print "Are you sure?"
choice = raw_input("> ")
if "yes" or "y" in choice:
    print "You've entered the central corridor"
    print "There's a Gothon standing in front of you."
    print ""
    print "Gothon: Hey you fucking spick! You're supposed to be dead."
    print "You: Heh, not in this world, lemme show you what I got."
    print "Gothon: Oh yeah? You've got a good joke?"
    print "You: What? Aren't I supposed to kill you?"
    print "Gothon: No man, it's supposed to be a joke."
    print "You: Oh, okay."
    print " "

    # Make this a function later on instead
    # that captures the input and spits something out
    while True:
        print "1. What did the Lawyer say to the other Lawyer? We are both Lawyers."
        print "2. Did you hear about the guy who invented the knock knock joke? He won the no-bell prize!"
        print "3. What's the difference between ignorance and Apathy? I don't know and I don't care."
        choice = raw_input("> ")
        if choice in ['1', '2', '3']:
            break
    if choice == '1':
        print "Gothon: Wow, really? That is the lamest joke I've ever heard."
        exit()
    elif choice == '2':
        # return laser weapon armory
        print "Gothon: Too good, hah, continue to the next room you rascal."
        print "You've entered the Laser Weapon Armory (I know the name is terrible, we had cutdowns in the naming department.)"
        print "In here lay a big neutron bomb and you really want this to blow up the whole got damn ship."
        print "There is one big problem though, it has a keypad, and you have to guess the number in order to unlock it."
        print "What's your guess?"
        print "1  2  3"
        print "4  5  6"
        print "7  8  9"
        while True: 
            choice = raw_input("> ")
            if choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                break
        if choice == '1' or '2' or '3':
            # return the bridge
            print "Kaching! You've got da bomb."
            print "You enter The Bridge."
            print "You encounter a couple of terribly looking Gothons"
            print "You have to place the bomb quietly in order to not get detected by the Gothons."
            choice = raw_input("> ")
            if choice == "slowly place the bomb":
                # return escape pod
                print "You got it placed properly and the motherfuckers blow up and you can finally continue to the last room."
                print "You enter the escape pod room, you have 5 choices, which one do you take?"
                good_pod = randint(1, 5)
                guess = raw_input("[pod #]> ")

                if int(guess) != good_pod:
                    print "wow, you suck you're dead."
                    exit() # return 'death'
                else:
                    print "You fucking won man!"
                    exit() # return 'finished'


        else:
            print "Sorry mate, you're totally dead."
            exit()
        
    elif choice == '3':
        print "Gothon: This is too complex for me to understand, not the way to go."
        exit()

elif "no" or "n" in choice:
    print "Seriously? You just started what the fuck man."
    exit()
