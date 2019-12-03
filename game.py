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
        self.l_players.append(c_player)


    def start_game(self, play_number, card_number, names ):
        self.i_play_number = play_number
        self.i_card_number = card_number
        self.l_players_names = names

        if self.i_play_number <= 0:
            raise ValueError("Количество игроков не может быть отрицательным числом.")

        if self.i_card_number <= 0:
            raise ValueError("Количество карт у игроков не может быть отрицательным числом.")

        if self.i_card_number > 5:
            raise ValueError("Количество карт у игроков не может быть больше 5.")

        for i in range(self.i_play_number-1):
            self.add_player(self.l_players_names[i-1])

        self.add_player("компьютер")

        self.i_number_barells_left = 99
        while True:
            self.i_random_number = rd.randint(1,100)
            print("\n")
            print(f'Новый бочонок: {self.i_random_number} (осталось {self.i_number_barells_left}) ')

            for x in self.l_players:
                self.print_player(x)
                s_yes = input("Зачеркнуть цифру? (y/n)")
                b_is_number_in = x.check_number(self.i_random_number)
                if x.s_player_name != "компьютер":
                    if s_yes == "y" and not b_is_number_in or s_yes == "n" and b_is_number_in:
                        print ( f'Игрок {x.s_player_name} проиграл.')
                        self.l_players.remove(x)
            if self.i_number_barells_left <= 0:
                break
            else:
                self.i_number_barells_left -= 1

            if self.check_win():
                print("Игра завершена!!!!")
                for player_name in self.check_win():
                    print(f'Победил {player_name}')

    def check_win(self):
        l_winers = []
        for x in self.l_players:
            if x.all_played():
                l_winers.append(x.s_player_name)
        return l_winers

    def print_player(self, player):
        l_cards_out = player.get_cards_out()
        s_name = f'Карточки игрока {player.s_player_name}'
        if l_cards_out:
            i_len_card = len(l_cards_out[0][0])
            if len(s_name) > i_len_card:
                print(s_name)
                print(i_len_card * "-")
            else:
                i_asterisk = int((i_len_card - len(s_name))/2 - 1)
                print(i_asterisk*"-" + " " + s_name + " " + i_asterisk*"-")
                print(i_len_card * "-")
        else:
            raise ValueError("Список карточек пуст.")

        for card in l_cards_out:
            print (card[0]+"\n"+card[1]+"\n"+card[2])
            print (i_len_card*"-")


if __name__ == "__main__":
    c_g = Game()
    c_g.start_game(3,2,["Andrey","Pavel"])

# TODO Повторяются случайные цифры надо написать метод по генерирования уникальных случайных чисел
# TODO Выводится случайное число 100
# TODO Для игрока компьютер не надо сравнивать и спрашивать Зачеркнуть. Просто вывести результат
# TODO Оформить код комментариями
# TODO Выводить номер бочонка для каждого игрока, за исключением компьютер
# TODO Вставить пробелы между числами в карточке
