import random


class Card:
    CARD_VALUE = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    CARD_SUIT = ['♥', '♦', '♣', '♠']

    # card suit can be either String or Symbol
    # String example: CARD_SUIT = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def is_equal(self, card):
        if self.value == card.value and self.suit == card.suit:
            return True
        return False

    def __repr__(self):
        return self.value + " " + self.suit


class CardDeck:
    def __init__(self):
        self.card_deck = []
        self.shuffle()

    def deal(self):
        deck_size = len(self.card_deck)

        if deck_size == 0:
            return "The card deck is empty"

        return self.card_deck.pop(deck_size - 1)

    def shuffle(self):
        self.card_deck = []
        for suit in Card.CARD_SUIT:
            for value in Card.CARD_VALUE:
                new_card = Card(value, suit)
                self.card_deck.append(new_card)
        random.shuffle(self.card_deck)
        return self.card_deck


card_deck = CardDeck()
print("Initial card deck:")
print(card_deck.card_deck)
print("number of cards in Card Deck:", len(card_deck.card_deck))
print("")

print("Deal:", card_deck.deal())
print("number of cards in Card Deck:", len(card_deck.card_deck))
print("")

for i in range(0, 52):
    print("Deal:", card_deck.deal())

print("number of cards in Card Deck:", len(card_deck.card_deck))
