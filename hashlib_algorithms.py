import hashlib


print('Guaranteed:\n{}\n'.format(
    ', '.join(sorted(hashlib.algorithms_guaranteed))))
print('Available:\n{}'.format(
    ', '.join(sorted(hashlib.algorithms_available))))


lorem = '''Lorem ipsum dolor sit amet, consectetur adipisicing
elit, sed do eiusmod tempor incididunt ut labore et dolore magna
aliqua. Ut enim ad minim veniam, quis nostrud exercitation
ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis
aute irure dolor in reprehenderit in voluptate velit esse cillum
dolore eu fugiat nulla pariatur. Excepteur sint occaecat
cupidatat non proident, sunt in culpa qui officia deserunt
mollit anim id est laborum.'''

h = hashlib.md5()
h.update(lorem.encode('utf-8'))

print("hexdigest: ",h.hexdigest())

h = hashlib.new('sha3_512')
h.update(lorem.encode('utf-8'))
print('sha3_512:', h.hexdigest())

import hmac

h = hmac.new(b'secret-shared-key-goes-here')
h.update(lorem.encode('utf-8'))
print('hmac:', h.hexdigest())

h = hmac.new(b'secret-shared-key-goes-here', lorem.encode('utf-8'),
    hashlib.sha256)
print('hmac [sha256]:', h.hexdigest())


