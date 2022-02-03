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
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
    for k in range(n):
        print(k)
print_items(10)