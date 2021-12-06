# python-oop

class Dog():
    
    def __init__(self,breed):
        self.breed = breed

my_dog = Dog('boxer')

print(type(my_dog))
#<class '__main__.Dog'>

print(my_dog.breed)
#==> boxer