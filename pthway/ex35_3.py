from sys import exit

def cthulhu_room():
    print "You're in a dark room with cool ppl lol."
    print "Do you eat your own head or do you go back to try again?"

    choice = raw_input("> ")

    if "head" in choice:
        dead("Dam funk")
    elif "back" in choice:
        print "Alright, you get another chance, or two ;)"
    else: 
        cthulhu_room()

def bear_room():
    print "You're in a fucking bear room"
    print "It stands in front of a door, protecting it furiously while masturbating to honey, what do you do?"
    bear_moved = False

    while True:
        choice = raw_input("> ")

        if choice == "take honey":
            dead("Got damn man, you don't steal honey from a bear.")
        elif choice == "taunt bear" and not bear_moved:
            print "wow, you got the bear away from the door."
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("Don't taunt him twice man.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else: 
            bear_room()

def gold_room():
    print "You enter a room with shit ton of gold."
    print "How much do you take?"
    print "Tip: You can always go back if you've missed something, just type back."

    choice = raw_input("> ")

    # Use this type of back int conversion if you want to be able to handle both strings and integers simultaneously. 
    if "back" in choice:
        print "You're back in the bear room."
        bear_room()
    elif "0" in choice or "1" in choice:
        how_much = int(choice)
    else: 
        print "Try again!"

    if how_much < 50:
        win("yay")
    elif how_much >= 50:
        dead("greedy bastord")
    else: 
        print "Try again!"
    

def dead(why):
    print why, "dam you dead"
    exit(0)

def win(why):
    print why, "got damn you win son."
    exit(0)

while True:
    print "You're in a room, there's two doors, right or left, which one do you take?"

    choice = raw_input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else: 
        print "Try again!"


