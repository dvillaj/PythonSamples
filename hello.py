print("Hello world")

a = [1, 2, 3, 5, 19]

print(list(reversed(a)))

# sorted
# enumerate
# reversed

print(a)
a.reverse()
print(a)

s = slice(2, None, 2)

print(a[s])

print(repr(a))

x = [1, 2, 3]
y = [4, 5, 6]

zipped = zip(x, y)
print(list(zipped))

x2, y2 = zip(*zip(x, y))
print(x2)
print(y2)

print(zip(x, y))
print(*zip(x, y))
print(*zip(*zip(x, y)))
print(list(zip(*zip(x, y))))

def llzip(*iterables):
    sentinel = object
    print("iterables={}".format(iterables))
    iterators = [iter(it) for it in iterables]
    while iterators:
        result = []
        for it in iterators:
            elem = next(it, sentinel)
            if elem is sentinel:
                return
            result.append(elem)
        yield tuple(result)


print("X={}\nY={}".format(x,y))



def fds3(*iterables):
    sentinel = object
    print("iterables={}".format(iterables))

    iterators = [iter(it) for it in iterables]
    print("iterators={}".format(iterators))


    result = []
    for it in iterators:

        print("IT={}".format(it))
        elem = next(it, sentinel)
        result.append(elem)  

    print("RESULT={}".format(result))  


fds3(x, y)