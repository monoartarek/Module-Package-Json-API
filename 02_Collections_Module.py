import collections

# print(collections.__doc__)

# print(dir(collections))

fruits = ['apple', 'banana', 'apple', 'mango']
print(collections.Counter(fruits))
print(collections.Counter(fruits).most_common(2))

word_dict = collections.defaultdict(list) #value gulo list hishebe thakbe

word_dict['python'].append('programming language')
print(word_dict)