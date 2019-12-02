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
                self.print_player(x)
                s_yes = input("Зачеркнуть цифру? (y/n)")
                b_is_number_in = x.check_number()
                if x.s_player_name != "компьютер":
                    if not ( s_yes == "y" and b_is_number_in ):
                        print ( f'Игрок {x.s_player_name} проиграл.')
                        self.l_players.remove(x)
            if self.i_number_barells_left <= 0:
                break
            else:
                self.i_number_barells_left -= 1

    def print_player(self, player):
        l_cards_out = player.get_cards_out()
        s_name = f'Карточка игрока {player.s_player_name}'
        if l_cards_out:
            i_len_card = len(l_cards_out[0])
            if len(s_name) > i_len_card:
                print(s_name)
            else:
                i_asterisk = int((i_len_card - len(s_name))/2 - 2)
                print("".join(["-" for i in range(i_asterisk)]) + " " + s_name + " " +
                      "".join(["-" for i in range(i_asterisk)]))
        else:
            raise ValueError("Список карточек пуст.")

        for card in l_cards_out:
            print (card[0]+"\n"+card[1]+"\n"+card[2]+"\n")
            print (i_len_card*"-")


if __name__ == "__main__":
    c_g = Game()
    c_g.start_game(3,2,["Andrey","Pavel"])