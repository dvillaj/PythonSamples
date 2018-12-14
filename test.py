a = [23,1,4]
b = a
c = a[:]

b[1] = -1
c[2] = 2

print(a)
print(b)
print(c)