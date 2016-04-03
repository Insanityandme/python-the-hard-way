from sys import exit

while True:
    print "You walk into a forest of dicks."
    print "There's a path to the right."
    print "There's a path to the left."
    print "Where do you go?"

    choice = raw_input("> ")
    
    def beach():
        print "you approach a beach and an old rotten boat containing something shiny."
        print "what do you do?"

    if "right" in choice:
        beach()
    elif "left" in choice:
        print "bla"


def gold_room():
    print "You enter a room with lots and lots of gold"
    print "What do you do?"

    choice = raw_input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Sorry mate, that is not a number, you dead.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else: 
        dead("You greedy bastard")

def bear_room():
    print "There is a bear there."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "What do you do?"
    bear_moved = False

    while True:
        choice = raw_input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You may enter."
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed of and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        elif choice == "open door" and not bear_moved:
            dead("Don't try to open a door while a bear protects it, try again.")
        else:
            print "I got no idea what that means, try again."

def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    choice = raw_input("> ")
    
    # If you type flee head, or head flee, flee will be first because of the nature of da loop.
    if "head" in choice:
        start()
    elif "flee" in choice:
        dead("Well, that was tasty!") 
    else:
        cthulhu_room()

def dead(why):
    print why, "Good Job!"
    exit(0)


def start():
    print "You are in a dark room."
    print "There is a door to the left and right."
    print "Which one do you choose?"

    choice = raw_input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right": 
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve to death.")

start()
