
## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a object that is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name of some kind
        self.name = name

## Cat is-a object that is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name of some kind
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has a name of some kind
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a object that is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## 
        super(Employee, self).__init__(name)
        ## Employee has-a salary of some kind
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a object that is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a object that is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## Satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## From mary get the pet attribute and set it to satan
mary.pet = satan

## Frank is-a employee
frank = Employee("Frank", 120000)

## Franks pet is rover
frank.pet = rover

## Flipper is-a object
flipper = Fish()

## Crouse is-a object
crouse = Salmon()

## Harry is-a object
harry = Halibut()
