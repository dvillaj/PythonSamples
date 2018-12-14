import itertools as it

def better_grouper(inputs, n):
    iters = [iter(inputs)] * n
    return zip(*iters)

for g in better_grouper([1, 2, 3, 4, 5, 6], 3):
    print(g)

bills = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]

makes_100 = []
for n in range(1, len(bills) + 1):
    for combination in it.combinations(bills, n):
        if sum(combination) == 100:
            makes_100.append(combination)



print(list(it.combinations([1,2,3,4], 2)))
print(list(it.combinations_with_replacement([1,2,3,4], 2)))
print(list(it.permutations([1,2,3,4])))

def evens():
    """Generate even integers, starting with 0."""
    n = 0
    while True:
        yield n
        n += 2



evens = evens()

print(type(evens))

for n in range(1,5):
    print(next(evens))

for n in range(1,5):
    print(next(evens))

print(list(next(evens) for _ in range(5)))
print(list(next(evens) for _ in range(5)))

count = it.count(start=0.5, step=0.75)

print(list(next(count) for _ in range(5)))

iterator = iter([1,2,3,4,10])
print(next(iterator))
print(next(iterator))