import player as pl
import card as cd
import random as rd

"""
    Класс Game реализует игру Лото для некоторого количества участников, у каждого из которых может быть
    некоторое количество карт.
"""

class Game():
    def __init__(self):
        """
             Метод инициализации класса. Создает пустой список игроков.
        """
        self._l_players = []
        # Устанавливаем максимальное количество бочонков
        self._i_number_barells_left = 99

    def add_player(self, name):
        """
            Метод, который добавляет игрока к игре с именем указанным в качестве входного параметра
        :param name: имя игрока
        """
        c_player = pl.Player(name)
        c_player.clean_card()
        for i in range(self._i_card_number):
            c_card = cd.Card()
            c_card.set_card()
            c_player.add_card(c_card)
        self._l_players.append(c_player)


    def start_game(self, play_number, card_number, names ):
        """
             Метод, который начинает игру. Для указанного количества игроков, карт у каждого игрока и их имена
        :param play_number: количество игроков, должен быть учтен игрок "компьютер"
        :param card_number: количество карт у каждого игрока
        :param names: список имен игроков
        """
        self._i_play_number = play_number
        self._i_card_number = card_number
        self._l_players_names = names
        self._l_players = []

        # Проверка количества игроков. Не должно быть отрицательного числа
        if self._i_play_number <= 0:
            raise ValueError("Количество игроков не может быть отрицательным числом.")

        # Проверка количества карт у игрока. Не должно быть отрицательного числа.
        if self._i_card_number <= 0:
            raise ValueError("Количество карт у игроков не может быть отрицательным числом.")

        # Проверка количества карт у игрока. Не должно быть больше 5 карт у игрока.
        if self._i_card_number > 5:
            raise ValueError("Количество карт у игроков не может быть больше 5.")

        # К игре добавляется указанное число игроков минус один с их именами
        for i in range(self._i_play_number - 1):
            self.add_player(self._l_players_names[i - 1])

        # Добавляется обязательный игрок "компьютер"
        self.add_player("компьютер")

        # Создаем генератор уникальных случайных чисел от 1 до 99
        co_random = self.random_number(99)
        while True:
            # Получаем уникальное случайное число
            self._i_random_number = next(co_random)
            print("\n")
            print(f'Новый бочонок: {self._i_random_number} (осталось {self._i_number_barells_left}) ')

            # Для каждого игрока выводим случайное число и спрашиваем его о проверке этого числа
            # В случае ошибки игрока выводим сообщение и помечаем игрока как проигравшего
            for x in self._l_players:
                if x.state == "Play":
                    print(f'Бочонок: {self._i_random_number} ')
                    self.print_player(x)
                    b_is_number_in = x.check_number(self._i_random_number)
                    if x.name != "компьютер":
                        s_yes = input("Зачеркнуть цифру? (y/n)")
                        if s_yes == "y" and not b_is_number_in or s_yes == "n" and b_is_number_in:
                            print ( f'Игрок {x.name} проиграл.')
                            x.state = "Lost"
                # Проверяем все ли номера на карте игрока закрыты
                # Если да, то помечаем игрока как победителя
                x.all_played()

            # Проверяем есть ли победитель среди игроков
            # Если есть, то выводим сообщение и завершаем игру
            if self.check_win():
                print("Игра завершена!!!!")
                for player in self._l_players:
                    if player.state == "Win":
                        print(f'Победил {player.name}')
                break

            # Проверяем кол-во игроков в состоянии "Play". Если есть только один игрок в этом состоянии, то он
            # является победителем. Выводим сообщение и завершаем игру
            if len(self.check_in_play()) == 1:
                print("Игра завершена!!!!")
                for player in self._l_players:
                    if player.state == "Play":
                        print(f'Победил {player.name}')
                break

            # Если победителей на данной итерации нет, уменьшаем кол-во оставшихся бочонков и продолжаем игру
            if self._i_number_barells_left < 0:
                break
            else:
                self._i_number_barells_left -= 1

    def check_win(self):
        """
            Проверяем наличие победителей среди игроков. Если они есть, то возвращаем их список
        :return: список победителей
        """
        return [x for x in self._l_players if x.state == "Win"]

    def check_in_play(self):
        """
            Метод формирует список игроков, которые еще играют
        :return: список игроков
        """
        return [x for x in self._l_players if x.state == "Play"]

    def print_player(self, player):
        """
            Метод выводит на печать содержимое карточек игрока
        :param player: игрок
        """
        # Вывод заголовка
        l_cards_out = player.get_cards_out()
        s_name = f'Карточки игрока {player.name}'
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

        # Вывод строк карточки
        for card in l_cards_out:
            print(card[0]+"\n"+card[1]+"\n"+card[2])
            print(i_len_card*"-")

    def random_number(self, max_number):
        """
            Генератор уникальных случайных чисел в диапазоне от 1 до max_number
        :param max_number: максимальное значение диапазона случайных чисел
        :return: уникальное случайное число
        """
        l_numbers = []
        i_iterator = max_number
        while i_iterator > 0:
            while True:
                i_random_number = rd.randint(1,max_number)
                if i_random_number not in l_numbers:
                    l_numbers.append(i_random_number)
                    break
            yield i_random_number
            i_iterator -= 1


