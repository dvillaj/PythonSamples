import time


t = time.clock()
print(type(t))


t = time.gmtime()
print(type(t))

import datetime

t = datetime.datetime.now()
print(t)
print(type(t))

t = datetime.datetime.today()
print(t)
print(type(t))

t = datetime.datetime.utcnow()
print(t)
print(type(t))

print(time.time())
print(time.ctime())