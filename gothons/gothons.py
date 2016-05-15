# CHEAT SHEET
# Class:
#   Tell Python to make a new type of thing
# Object:
#   Two meanings: the most basic type of thing,
#   and any instance of some thing.
# Instance:
#   What you get when you tell Python to create a class.
# Def:
#  How you define a function inside a class.
# Self:
#   Inside the functions in a class, self is a variable for the
#   instance/object being accessed
# Inheritance:
#   The concept that one class inherits traits from another class,
#   much like you and your parents.
# Composition:
#   The concept that a class can be composed of other classes as parts,
#   much like how a car has wheels.
# Attribute:
#   A property classes have that are from composition and are usually
#   variables.
# is-a:
#   A phrase to say that something inherits from another, as in
#   a "salmon" is-a "fish."
# has-a:
#   A phrase to say that something is composed of other things or has a trait
#   , as in a "salmon" has-a "mouth."
#
# in python __init__ is your constructor, iether say the constructor or
# the init function
#
# You call functions, methods in a class
# If a variable is outside of a method in a class, it's called an
# class attribute.
# ex: class A(object): foo = 5
# A variable inside a method in a class, is an instance attribute
#
# ex: class A(object): __init__(self): self.foo = []
# (instance-attribute-set-at-instantiation)
# variables do exist inside of classes, they are not then referenced
# by the self
#
# You never create instances in a function. Only in classes.
#
# Use self to access methods, attributes and properties of a class
# Ex:
# class Anus(object):
#     foo = {'foo':'bar'}
#     def get_foo(self, foo_name):
#         val = self.foo.get(foo_name)
#         return val
#     def get_bar(self):
#         return self.get_foo('foo')
#
# Engine can access the opening_scene() method because
# it has the variable a_map inside of Engine(a_map) and therefor have access
# to the map classess attributes and methods.
#
# Creating a new object is called instantiation
# and the object is an instance of the class.
#
# You can assign values to an instance using dot notation:
# anus.x = 3.0
# anus.y = 4.0
#
# This syntax is similar to the syntax for selecting a variable from a module
# math.pi or string.whitespace. In this case though,
# we are assigning values to named elements of an object.
# These elements are called attributes.
#
# box = Rectangle()
# box.width = 100.0
# box.height = 200.0
# box.corner = Point()
# box.corner.x = 0.0
# box.corner.y = 0.0
#
# The expression box.corner.x means "Go to the object box refers to and
# select the attribute named corner; then go to that object and select
# the attribute named x."
# An object that is an attribute of another object is embedded.
#
# Functions can return instances
#
# def find_center(rect):
#     p = Point()
#     p.x = rect.corner.x + rect.width/2.0
#     p.y = rect.corner.y + rect.height/2.0
#     return p
#
# center = find_center(box)
# print_point(center)
#
# Object are mutable!
# def grow_rectangle(rect, dwidth, dheight):
#     rect.width += dwidth
#     rect.height += dheight
#
# Ex: grow_rectangle(box, 100, 50)
#
# x = Bank()
# x.create_atm() same as Bank.create_atm(x)
# now self refers to x

# From the module sys import the exit function
from sys import exit
# From the module random import the randint function
from random import randint


# Make a class named Scene that is-a object
class Scene(object):
    # class Scene has-a function named enter that takes self parameter
    def enter(self):
        print "This scene is not yet configured Subclass it and implement enter()."
        exit(1)


# Make a class named Engine that is-a object
class Engine(object):
    # class Engine has-a __init__ function that takes self
    # and scene_map parameters
    def __init__(self, scene_map):
        # refer self to scene_map
        self.scene_map = scene_map
    
    # create a method play that takes the parameter self
    def play(self):
        # create a variable named current_scene 
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene):

    quips = [
            "You died. You kinda suck at this.",
            "Your mom would be proud...if she were smarter.",
            "Such a luser.",
            "I have a small puppy that's better at this."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]

class CentralCorridor(Scene):

    def enter(self):
        print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
        print "your entire crew.  You are the last surviving member and your last"
        print "mission is to get the neutron destruct bomb from the Weapons Armory,"
        print "put it in the bridge, and blow the ship up after getting into an "
        print "escape pod."
        print "\n"
        print "You're running down the central corridor to the Weapons Armory when"
        print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
        print "flowing around his hate filled body.  He's blocking the door to the"
        print "Armory and about to pull a weapon to blast you."

        action = raw_input("> ")

        if action == "shoot!":
            print "Quick on the draw you yank out your blaster and fire it at the Gothon."
            print "His clown costume is flowing and moving around his body, which throws"
            print "off your aim.  Your laser hits his costume but misses him entirely.  This"
            print "completely ruins his brand new costume his mother bought him, which"
            print "makes him fly into an insane rage and blast you repeatedly in the face until"
            print "you are dead.  Then he eats you."
            return 'death'
        
        elif action == "dodge!":
            print "Like a world class boxer you dodge, weave, slip and slide right"
            print "as the Gothon's blaster cranks a laser past your head."
            print "In the middle of your artful dodge your foot slips and you"
            print "bang your head on the metal wall and pass out."
            print "You wake up shortly after only to die as the Gothon stomps on"
            print "your head and eats you."
            return 'death'

        elif action == "tell a joke":
            print "Lucky for you they made you learn Gothon insults in the academy."
            print "You tell the one Gothon joke you know:"
            print "Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr."
            print "The Gothon stops, tries not to laugh, then busts out laughing and can't move."
            print "While he's laughing you run up and shoot him square in the head"
            print "putting him down, then jump through the Weapon Armory door."
            return 'laser_weapon_armory'

        else:
            print "DOES NOT COMPUTE!"
            return 'central_corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
        print "You do a dive roll into the Weapon Armory, crouch and scan the room"
        print "for more Gothons that might be hiding.  It's dead quiet, too quiet."
        print "You stand up and run to the far side of the room and find the"
        print "neutron bomb in its container.  There's a keypad lock on the box"
        print "and you need the code to get the bomb out.  If you get the code"
        print "wrong 10 times then the lock closes forever and you can't"
        print "get the bomb.  The code is 3 digits."
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 9:
            print "BZZZZEDDD!"
            guesses += 1
            guess = raw_input("[keypad]> ")

        if guess == code:
            print "The container clicks open and the seal breaks, letting gas out."
            print "You grab the neutron bomb and run as fast as you can to the"
            print "bridge where you must place it in the right spot."
            return 'the_bridge'
        else:
            print "The lock buzzes one last time and then you hear a sickening"
            print "melting sound as the mechanism is fused together."
            print "You decide to sit there, and finally the Gothons blow up the"
            print "ship from their ship and you die."
            return 'death'

class TheBridge(Scene):

    def enter(self):
        print "You burst onto the Bridge with the netron destruct bomb"
        print "under your arm and surprise 5 Gothons who are trying to"
        print "take control of the ship.  Each of them has an even uglier"
        print "clown costume than the last.  They haven't pulled their"
        print "weapons out yet, as they see the active bomb under your"
        print "arm and don't want to set it off."

        action = raw_input("> ")

        if action == "throw the bomb":
            print "In a panic you throw the bomb at the group of Gothons"
            print "and make a leap for the door.  Right as you drop it a"
            print "Gothon shoots you right in the back killing you."
            print "As you die you see another Gothon frantically try to disarm"
            print "the bomb. You die knowing they will probably blow up when"
            print "it goes off."
            return 'death'

        elif action == "slowly place the bomb":
            print "You point your blaster at the bomb under your arm"
            print "and the Gothons put their hands up and start to sweat."
            print "You inch backward to the door, open it, and then carefully"
            print "place the bomb on the floor, pointing your blaster at it."
            print "You then jump back through the door, punch the close button"
            print "and blast the lock so the Gothons can't get out."
            print "Now that the bomb is placed you run to the escape pod to"
            print "get off this tin can."
            return 'escape_pod'
        else:
            print "DOES NOT COMPUTE!"
            return "the_bridge"

class EscapePod(Scene):

    def enter(self):
        print "You rush through the ship desperately trying to make it to"
        print "the escape pod before the whole ship explodes.  It seems like"
        print "hardly any Gothons are on the ship, so your run is clear of"
        print "interference.  You get to the chamber with the escape pods, and"
        print "now need to pick one to take.  Some of them could be damaged"
        print "but you don't have time to look.  There's 5 pods, which one"
        print "do you take?"

        good_pod = randint(1,5)
        guess = raw_input("[pod #]> ")


        if int(guess) != good_pod:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod escapes out into the void of space, then"
            print "implodes as the hull ruptures, crushing your body"
            print "into jam jelly."
            return 'death'
        else:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod easily slides out into space heading to"
            print "the planet below.  As it flies to the planet, you look"
            print "back and see your ship implode then explode like a"
            print "bright star, taking out the Gothon ship at the same"
            print "time.  You won!"
            return 'finished'

class Finished(Scene):
    
    def enter(self):
        print "You won! Good job."
        return 'finished'
    

class Map(object):

    scenes = {
            'central_corridor': CentralCorridor(),
            'laser_weapon_armory': LaserWeaponArmory(),
            'the_bridge': TheBridge(),
            'escape_pod': EscapePod(),
            'death': Death(),
            'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

# a_map = Map('central_corridor')
# a_game = Engine(a_map)
# a_game.play()
# Engine(Map('central_corridor')).play()
