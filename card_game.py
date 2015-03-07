class Deck(object):

    SUITS = ["C", "D", "H", "S"]
    RANKS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self):
        self.cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = suit+rank
                self.cards.append(card)

deck = Deck()
