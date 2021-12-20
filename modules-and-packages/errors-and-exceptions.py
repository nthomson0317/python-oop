#errors and exception handling

#try: this is the block of code to be attempted (may lead to an error)

#except: this block of code will execute in case there is an error in try block

#finally: a block of code that is executed regardless of error

def add(n1,n2):
    print(n1 + n2)

add(10,20)
#==> 30

number1 = 10

number2 = input("Please provide a number")

add(number1,number2)
#==> TypeError: unsupported operand type(s) for +: 'int' and 'str'

try:
    #WANT TO ATTEMPT THIS CODE
    #MAY HAVE AN ERROR
    result = 10 + 10
except: 
    print("Hey it looks like you aren't adding correctly.")

result 
#==> 20

try:
    #WANT TO ATTEMPT THIS CODE
    #MAY HAVE AN ERROR
    result = 10 + '10'
except: 
    print("Hey it looks like you aren't adding correctly.")
    #==> Hey it looks like you aren't adding correctly.

