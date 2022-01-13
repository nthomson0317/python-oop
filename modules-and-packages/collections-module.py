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