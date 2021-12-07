# python-oop

class Dog():
    
    # CLASS OBJECT ATTRIBUTE
    # SAME FOR ANY INSTANCE OF A CLASS
    species = 'mammal'

    def __init__(self,breed,name,spots):
        #Attributes
        #We take in the argument
        #Assign it using self.attribute_name
        self.breed = breed
        self.name = name

        # Expect boolean
        self.spots = spots

    # METHODS (a method is a function inside a class)
    def bark(self,number):
        print('WOOF! My name is {} and the number is {}'.format(self.name,number))

my_dog = Dog(breed='boxer',name='Basil',spots=False)

print(type(my_dog))
#<class '__main__.Dog'>

print('breed: ')
print(my_dog.breed)
#==> boxer

print('name: ')
print(my_dog.name)
#==> Basil

print('spots? ')
print(my_dog.spots)
#==> False

print('species: ')
print(my_dog.species)

my_dog.bark(4)


class Circle():

    #CLASS OBJECT ATTRIBUTE
    pi = 3.14

    def __init__(self,radius=1):

        self.radius = radius
    
    # METHOD
    def get_circumference(self):
        return self.radius * self.pi * 2

my_circle = Circle(30)

print('pi')
print(my_circle.pi)
print('radius')
print(my_circle.radius)
print('circumference')
print(my_circle.get_circumference())