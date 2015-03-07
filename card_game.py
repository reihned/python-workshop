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
        if self.cards:  # [] == false
            return self.cards.pop(0)

        return None

# deck = Deck()

class Game(object):

    def __init__(self):
        self.deck = Deck()
        self.rounds_played = 0
        self.dealer_wins = 0
        self.player_wins = 0
        self.ties = 0

    def play_round(self):
        dealer_card = self.deck.draw_one_card()
        player_card = self.deck.draw_one_card()

        result = self._resolve_result(dealer_card, player_card)      # notice self is not passed in
        return result

    def _resolve_result(self, dealer_card, player_card):
        result = "tie"                                      # give it a default value first, then change it to the real result
        if int(dealer_card[1:]) > int(player_card[1:]):     # in this logic, clubs is weaker than diamonds
            result = "dealer"
        if int(dealer_card[1:]) < int(player_card[1:]):
            result = "player"
        return result

    def _log_result(self, result):
        self.rounds_played += 1
        if result == "player":
            self.player_wins += 1
        elif result == "dealer":
            self.dealer_wins += 1
        else:
            self.ties += 1

    def _show_result(self):
        print("{} games played, {} won by dealer, {} won by player, {} ties".format(self.rounds_played, self.dealer_wins, self.player_wins self.ties))

    def run(self):
        while True:
            if self.deck.cards:
                # pass
                result = self.play_round()
                self._log_result(result)
            else:
                # pass
                break  # break out of an infinite loop
        self._show_result
