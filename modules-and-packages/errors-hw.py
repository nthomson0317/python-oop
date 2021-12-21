#Errors and Exceptions Homework
#Problem 1
#Handle the exception thrown by the code below by using try and except blocks.
try:
    for i in ['a','b','c']:
        print(i**2)
except:
    print('Whoops! You can only multiply numbers')

##Problem 2
#Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'

x = 5
y = 0

try:
    z = x/y
except:
    print("Whoops! You can't divide by zero!")
finally:
    print("ALl done")