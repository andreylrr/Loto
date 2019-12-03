
class Player():
    def __init__(self, name):
        self.l_card = []
        self.s_player_name = name

    def add_card(self, card):
        self.l_card.append(card)

    def clean_card(self):
        self.l_card = []

    def check_number(self, number):
        b_result = False
        for x in self.l_card:
            if x.is_number_in(number):
                b_result = True
        return b_result

    def get_cards_out(self):
        return [x.card_out() for x in self.l_card]

    def all_played(self):
        b_result = True
        for x in self.l_card:
            if not x.is_all_played():
                b_result = False
        return b_result
