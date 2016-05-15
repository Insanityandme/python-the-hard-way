# __INIT__.py EXAMPLE AND EXPLANATIONS

# In addition to labeling a directory as a python package and defining
# __all__, __init__.py allows you to define any variable at the package level.

# EXAMPLE: folder in django called apps has 3 files
# __init__.py
# config.py
# registry.py
# This is how the __init__.py file looks like:
from .config import AppConfig
from .registry import apps

# __all__ is a list containing the names of modules that you want to be imported with
# import * 
__all__ = ['AppConfig', 'apps']

# Words that interest me for further research
# __init__, self, hasattr, getattr, rpartition, @classmethod

# An introduction to classes and inheritance in Python
class Pet(object):

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    def __str__(self):
        return "%s is a %s" % (self.name, self.species)

class Dog(Pet):

    def __init__(self, name, hates_dogs):
        Pet.__init__(self, name, "Dog")
        self.chases_cats = chases_cats

    def chasesCats(self):
        return chases_cats

class Cat(Pet):

    def __init__(self, name, hates_dogs):
        Pet.__init__(self, name, "Cat")
        self.hates_dogs = hates_dogs

    def hatesDogs(self):
        return hates_dogs
