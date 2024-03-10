from collections import namedtuple
from random import choice

Card = namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(number) for number in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit)
                       for rank in self.ranks
                       for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]


suit_values = {'spades': 3, 'hearts': 2, 'diamonds': 1, 'clubs': 0}


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


french_deck = FrenchDeck()
print(len(french_deck))
print(french_deck[3])
for card in french_deck:
    print(card)
for card in reversed(french_deck):
    print(card)

print(f'Random card: {choice(french_deck)}')
print(f'First four cards: {french_deck[:4]}')
print(f'Every spade: {french_deck[::4]}')

print(Card('7', 'spades') in french_deck)
print(Card('7', 'somethings') in french_deck)

for card in sorted(french_deck, key=spades_high):
    print(card)