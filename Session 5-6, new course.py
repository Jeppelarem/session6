import random

class Card:
    SUITS = ["♣", "♦", "♥", "♠"]
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, rank, suit):
        if rank not in self.RANKS:
            raise Exception(f"Invalid rank, must be one of {self.RANKS}")
        if suit not in self.SUITS:
            raise Exception(f"Invalid suit, must be one of {self.SUITS}")
        self._rank = rank
        self._suit = suit

    @property
    def suit(self):
        return self._suit

    @property
    def rank(self):
        return self._rank

    def __str__(self):
        return f"{self.rank}{self.suit}"

    def __repr__(self):
        return self.__str__()


class Deck:
    def __init__(self):
        self._cards = [Card(rank, suit) for rank in Card.RANKS for suit in Card.SUITS]

    @property
    def cards(self):
        return self._cards

    def __str__(self):
        return str(self.cards)

    def shuffle(self):
        random.shuffle(self._cards)

class Hand:
    def __init__(self, deck):
        self._cards = [deck.cards[i] for i in range(5)]

    def __str__(self):
        return str(self._cards)

    @property
    def is_flush(self):
        suit = self._cards[0].suit
        for card in self._cards[1:]:
            if card.suit != suit:
                return False
        return True

tries = 10
i = 0
while tries > 0:
    i += 1
    d = Deck()
    d.shuffle()
    hand = Hand(d)
    if hand.is_flush:
        tries -= 1

probability = (10 / i) * 100
print(f"The odds of getting a flush are {probability}%")
