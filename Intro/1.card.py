# 1.1 일련의 카드로 구성한 카드 한 벌

import collections

# 개별 카드를 나타내는 클래스 구현
# namedtuple을 이용해서 데이터베이스의 레코드처럼 메서드를 가지지 않는 일련의 속성으로 구성된 클래스를 만들 수 있다.
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA') # 카드 숫자
    suits = 'spades diamonds clubs hearts'.split() # 카드 모양

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits 
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


beer_card = Card('7', 'diamonds')
# print(beer_card)

deck = FrenchDeck()
# print(len(deck))
# print(deck._cards)
# print(deck.__len__)
# print(deck.__getitem__(2))


# 무작위
from random import choice
# print(choice(deck))

# 모든 카드 뽑기
# for card in deck: # doctest: +ELLIPSIS
#     print(card)

# 뒤로 뽑기
# for card in reversed(deck):
#     print(card)

# 포함 여부 확인
print(Card('Q', 'hearts') in deck)
print(Card('7', 'beasts') in deck)

# 순서대로 배역
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)