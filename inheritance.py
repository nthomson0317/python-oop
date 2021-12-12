# INHERITANCE
# a way to form new classes using classes that have already been defined

class Animal():

    def __init__(self):
        print("ANIMAL CREATED")
    
    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

myanimal = Animal()
#==> ANIMAL CREATED

myanimal.eat()
#=> I am eating

myanimal.who_am_i
#=> I am an animal

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

my_dog = Dog()
#=>ANIMAL CREATED
#=>Dog Created

my_dog.eat()



# POLYMORPHISM