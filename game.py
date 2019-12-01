import player as pl
import card as cd
import random as rd

class Game():
    def __init__(self):
        self.l_players = []

    def add_player(self, name):
        c_player = pl.Player(name)
        c_player.clean_card()
        for i in range(self.i_card_number):
            c_card = cd.Card()
            c_card.set_card()
            c_player.add_card(c_card)

    def start_game(self, play_number, card_number, names ):
        self.i_play_number = play_number
        self.i_card_number = card_number
        self.i_players_names = names

        if self.i_play_number <= 0:
            raise ValueError("Количество игроков не может быть отрицательным числом.")

        if self.i_card_number <= 0:
            raise ValueError("Количество карт у игроков не может быть отрицательным числом.")

        if self.i_card_number > 5:
            raise ValueError("Количество карт у игроков не может быть больше 5.")

        for i in range(self.i_play_number):
            self.add_player(self.i_players_names)

        self.add_player("компьютер")

        self.i_number_barells_left = 99
        while True:
            self.i_random_number = rd.randint(1,100)
            print(f'Новый бочонок: {self.i_random_number} (осталось {self.i_number_barells_left}) ')

            for x in self.l_players:
                l_cards_out = x.get_cards_out()
                print("")



