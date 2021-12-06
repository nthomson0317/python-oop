# python-oop

class Dog():
    
    def __init__(self,breed,name,spots):

        #Attributes
        #We take in the argument
        #Assign it using self.attribute_name
        self.breed = breed
        self.name = name
        self.spots = spots

my_dog = Dog('boxer')

print(type(my_dog))
#<class '__main__.Dog'>

print(my_dog.breed)
#==> boxer