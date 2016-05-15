from sys import exit


class Scene(object):

    def enter(self):
        pass


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()


class Finished(Scene):

    def enter(self):
        print "You won! Good job!"
        return 'finished'


class Death(Scene):

    def enter(self):
        print "You dead nigga"
        exit()


class CentralCorridor(Scene):

    def enter(self):
        print "hello I'm a retard"
        choice = raw_input("Choose a number, 1 or 2")

        if choice == '1':
            return 'death'
        else:
            return 'anus_chamber'


class AnusChamber(Scene):

    def enter(self):
        print "You're in the poop chamber."
        return 'finished'


class Map(object):

    scenes = {
                'central_corridor': CentralCorridor(),
                'anus_chamber': AnusChamber(),
                'death': Death(),
                'finished': Finished()
            }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

# Create a new time object with the Map class.
a_map = Map('central_corridor')

# Create a game object by instantiating the Engine class
# with an object, which has to be an instance of the class Map.
game = Engine(a_map)

# Invoke the play method on the game subject
game.play()
