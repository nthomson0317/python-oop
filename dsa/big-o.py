def print_items(n):
    for i in range(n):
        print(i)

print_items(10)

#O(n) --> it ran n times

##Drop Constants
    ## n+n
        ##still #O(n)

def print_items(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)

print_items(10)


##O(n^2)
    ## n*n

def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
print_items(10)

    ## n*n*n
        ##still O(n^2)
def print_items(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i,j,k)
print_items(10)



        ## Drop non dominants
            ## O(n^2 + n)
                ##O(n^2)
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

    for k in range(n):
        print(k)
print_items(10)

##O(1)
    ##constant time: as n increases, number of operations remains constant

def add_items(n):
    return n + n

##O(log n)
    ## most efficient

## O(a+b)
def print_items(a,b):
    for i in range(a):
        print(i)
    for j in range(b):
        print(j)

##Lists

##adding to the end is O(1)
##adding to the beginning is O(n) because you have to reindex every list item after starting index

##search a list by value is O(n)
##search a list by index is O(1) --> you can go directly there in memory