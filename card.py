import random
import barell as b

"""
    Класс Card представляет карточку игрока с бочонками. Каждая карточка имеет
    три строки по 9 элементов в каждой строке и по 5 не пустых бочонков.
"""

class Card():

    def __init__(self):
        """
            Метод инициализации класса заполняет карточку игрока
            пустыми бочонками
        """
        self.clean()

    def clean(self):
        """
             Метод очистки карты и ее заполнения пустыми бочонками
        :return:
        """
        self._l_lines = []
        for i in range(3):
            self._l_lines.append(self.clean_line())

    def clean_line(self):
        """
             Метод заполнения строк карточки пустымми бочонками
        :return: строка карточки с пустыми бочонками
        """
        return {i: b.Barell(0,"Empty") for i in range(1,10)}

    def is_number_in(self, number):
        """
             Метод проверки если число, указанное в качестве входного параметра
             присутствует в карточке.
             :return: результат проверки
        """
        b_result = False
        for x in self._l_lines:
            for barell in x.values():
                if barell.number == number and barell.state == "Ready":
                    barell.state = "Played"
                    b_result = True
        return b_result

    def is_all_played(self):
        """
             Метод проверки есть ли в карточке хоть один бочонок, который еще не сыграл
        :return: результат проверки
        """
        b_result = True
        for x in self._l_lines:
            for barell in x.values():
                if barell.state == "Ready":
                    b_result = False
        return b_result

    def card_out(self):
        """
            Метод вывода содержимого карточки игрока
        :return: лист и трех элементов
        """
        l_out = []
        for d_line in self._l_lines:
            l_out.append(self.line_out(d_line))
        return l_out

    def line_out(self, card_dict):
        """
            Метод вывода одной строки из карточки игрока
        :param card_dict: словарь представляющий одну строку в карточке игрока
        :return: строка, которая представляет одну строку в карточе игрока
        """
        s_out = ""
        for barell in card_dict.values():
            if barell.state == "Empty":
                s_out += "    "
            elif barell.state == "Ready":
                s_out += '{:3d}'.format(barell.number) + " "
            elif barell.state == "Played":
                s_out += "---" + " "
        return s_out

    def set_card(self):
        """
            Метод, который задает начальное значение карточки
        """
        self._l_lines = list(map(self.set_line, self._l_lines))

    def set_line(self, card_dict):
        """
            Метод который случайным образом задает значение 5 чисел в строке карточки в отсортированном виде.
        :param card_dict: словарь представляющий одну строку карточки
        :return: словарь представляющий одну строку карточки
        """
        l_number = random.sample(range(1,100), 5)
        l_number.sort()
        l_position = random.sample(range(1,10), 5)
        l_position.sort()
        if len(set(l_number)) == 5 and len(set(l_position)) == 5 :
            for i,i_position in enumerate(l_position):
                card_dict[i_position].number = l_number[i]
                card_dict[i_position].state = "Ready"
        return card_dict


