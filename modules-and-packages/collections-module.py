from collections import Counter

mylist = [1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3]

res = Counter(mylist)

print(res)
#Counter({2: 7, 1: 6, 3: 5})