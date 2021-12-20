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
else:
    print("Add went well!")
    print(result)

result 
#==> 20

try:
    #WANT TO ATTEMPT THIS CODE
    #MAY HAVE AN ERROR
    result = 10 + '10'
except: 
    print("Hey it looks like you aren't adding correctly.")
    #==> Hey it looks like you aren't adding correctly.


    ##########

try:
    f = open('testfile','w')
    f.write("Write a test line")
except TypeError:
    print("There was a type error")
except OSError:
    print('Hey you have an OS error')
finally:
    print("I always run")

def ask_for_int():
    try:
        result = int(input("Please provide number"))
    except:
        print("Whoops! That is not a number")
    finally:
        print("End of try/except/finally")