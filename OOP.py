# python-oop

class Dog():
    
    def __init__(self,breed,name,spots):

        #Attributes
        #We take in the argument
        #Assign it using self.attribute_name
        self.breed = breed
        self.name = name

        # Expect boolean
        self.spots = spots

my_dog = Dog(breed='boxer',name='Basil',spots=False)

print(type(my_dog))
#<class '__main__.Dog'>

print(my_dog.breed)
#==> boxer

print(my_dog.name)
#==> Basil

print(my_dog.spots)
#==> False