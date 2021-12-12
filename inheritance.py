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
    
    def who_am_i(self):
        print("I am a dog")

    def bark(self):
        print("WOOF!")

my_dog = Dog()
#=>ANIMAL CREATED
#=>Dog Created

my_dog.eat()
#=>I am eating

my_dog.who_am_i()
#=>I am a dog

my_dog.bark()
#==> WOOF!


# POLYMORPHISM

class Cat():
    def __init__(self,name):
        self.name = name 

    def speak(self):
        return self.name + " says meow!"

class Snake():
    def __init__(self,name):
        self.name = name 

    def speak(self):
        return self.name + " says sssssss!"

niko = Cat("niko")

felix = Snake("felix")

print(niko.speak())
#=>niko says meow!


print(felix.speak())
#=>felix says sssssss!

for pet in [niko,felix]:
    print(type(pet))
    print(type(pet.speak()))

#<class '__main__.Cat'>
#<class 'str'>
#<class '__main__.Snake'>
#<class 'str'>

def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)
#niko says meow!

pet_speak(felix)
#felix says sssssss!

class Human():
    def __init__(self,name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")

myhuman = Human('fred')

myhuman.speak()
#==>  raise NotImplementedError("Subclass must implement this abstract method")