import itertools


iterator1 = range(1, 4)
iterator2 = range(4, 7)
iterator3 = range(7, 10)

combined_iterator = itertools.chain(iterator1, iterator2, iterator3)

for item in combined_iterator:
    print(item)