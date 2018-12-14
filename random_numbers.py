import random
for i in range(5):
    print('%04.3f' % random.random(), end=' ')
print()

random.seed(1)

for i in range(5):
    print('{:04.3f}'.format(random.uniform(1, 100)), end=' ')
print()

#print("State", random.getstate())

for i in range(10):
    print(random.randint(-100, 100), end=' ')
print()


for i in range(10):
    print(random.randrange(-100, -121, -1), end=' ')
print()

outcomes = {
    'heads': 0,
    'tails': 0,
}

sides = list(outcomes.keys())

for i in range(10000):
    outcomes[random.choice(sides)] += 1

print('Heads:', outcomes['heads'])
print('Tails:', outcomes['tails'])

print(random.choice(sides))
print(random.choice(sides))


FACE_CARDS = ('J', 'Q', 'K', 'A')
SUITS = ('H', 'D', 'C', 'S')

import itertools

def new_deck():
    return [
        # Always use 2 places for the value, so the strings
        # are a consistent width.
        '{:>2}{}'.format(*c)
        for c in itertools.product(
            itertools.chain(range(2, 11), FACE_CARDS),
            SUITS,
        )
    ]

def show_deck(deck):
    p_deck = deck[:]
    while p_deck:
        row = p_deck[:13]
        p_deck = p_deck[13:]
        for j in row:
            print(j, end=' ')
        print()

deck = new_deck()
print('Initial deck:')
show_deck(deck)

# Shuffle the deck to randomize the order.
random.shuffle(deck)
print('\nShuffled deck:')
show_deck(deck)

print()
for w in random.sample(deck, 10):
    print(w, end = '')
print()

r1 = random.normalvariate(10, 100)
print(r1)