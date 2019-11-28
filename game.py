import player as pl
import card as cd

class Game():
    def __init__(self, play_number, card_number):
        self.l_players = []
        self.i_play_number = play_number
        self.i_card_number = card_number

    def add_player(self, name):
        if len(self.l_players) >= self.i_play_number:
            return -1

        c_player = pl.Player(name)
        c_player.


