from collections import Counter

mylist = [1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3]

res = Counter(mylist)

print(res)
#Counter({2: 7, 1: 6, 3: 5})

print(Counter('aaabbbssshhhssssj'))
#Counter({'s': 7, 'a': 3, 'b': 3, 'h': 3, 'j': 1})

sentence = "How many times does each word show up in this sentence with a word"

print(Counter(sentence.split()))
#Counter({'word': 2, 'How': 1, 'many': 1, 'times': 1, 'does': 1, 'each': 1, 'show': 1, 'up': 1, 'in': 1, 'this': 1, 'sentence': 1, 'with': 1, 'a': 1})

letters = 'aaabbbcccccddddddd'

c = Counter(letters)
print(c)
#Counter({'d': 7, 'c': 5, 'a': 3, 'b': 3})

print(c.most_common())
#[('d', 7), ('c', 5), ('a', 3), ('b', 3)]
print(c.most_common(2))
#[('d', 7), ('c', 5)]

print(list(c))
#['a', 'b', 'c', 'd']

from collections import defaultdict

d = {'a':10}
print(d['a'])
#10

# print(d['WRONG'])
# File "/Users/nicholas.thomson/Desktop/Development/python/modules-and-packages/collections-module.py", line 38, in <module>
    #print(d['WRONG'])
#KeyError: 'WRONG'

d = defaultdict(lambda: 0)

d['correct'] = 100

print(d['correct'])
#100

d['WRONG KEY!']
#  0

print(d)
#defaultdict(<function <lambda> at 0x10e64d700>, {'correct': 100, 'WRONG KEY!': 0})


mytuple = (10,20,30)

print(mytuple[0])
#10

from collections import namedtuple

Dog = namedtuple('Dog',['age','breed','name'])

print(Dog)
#<class '__main__.Dog'>

sammy = Dog(age=5,breed='Husky',name='Sam')

print(type(sammy))
#<class '__main__.Dog'>
print(sammy)
#Dog(age=5, breed='Husky', name='Sam')

print(sammy.age)
#5
print(sammy.breed)
#Husky
print(sammy[0])
#5