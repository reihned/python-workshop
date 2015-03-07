import 'random'

class Deck(object):

    SUITS = ["D", "C", "H", "S"]
    RANKS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self):
        self.cards = []
        self._generate_card()
        self.shuffle

    def _generate_cards(self):
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = suit+rank
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_one_card(self):
        return self.cards.pop(0)

deck = Deck()
