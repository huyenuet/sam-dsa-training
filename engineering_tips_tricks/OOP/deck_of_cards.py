import random


class Card:
    card_value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    card_suit = ['♥', '♦', '♣', '♠']
    # card suit can be either String or Symbol
    # String example: card_suit = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

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

    def deal(self, deal_card: Card):
        for card_index, card in enumerate(self.card_deck):
            if card.is_equal(deal_card):
                to_remove_index = card_index
                self.card_deck.pop(to_remove_index)
                break
        else:
            return "The card \"{}\" isn't existed in the Card Deck\n".format(str(deal_card))

        return self.card_deck

    def shuffle(self):
        for suit in Card.card_suit:
            for value in Card.card_value:
                new_card = Card(value, suit)
                self.card_deck.append(new_card)
        random.shuffle(self.card_deck)
        return self.card_deck


card_deck = CardDeck()
print("Initial card deck:")
print(card_deck.card_deck)
print("")

card = Card('8', '♥')
print("Deal " + str(card))
print(card_deck.deal(card))
print("")

card = Card('8', '♥')
print("Deal " + str(card))
print(card_deck.deal(card))

card = Card('1', '♣')
print("Deal " + str(card))
print(card_deck.deal(card))
