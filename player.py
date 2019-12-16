import card as cd
"""

    Класс Player представляет игрока в лото включая все карточки, принадлежащие игроку

"""

class Player():
    def __init__(self, name: str):
        """
            Метод инициализации класса
        :param name: имя игрока
        """
        self._l_card = []
        self._s_name = name
        self._s_state = "Play"
        self._s_type = "Human"

    @property
    def state(self):
        """
            Проперти представляющее состояние игрока. Может иметь два значения:
            "Play" игрок находится в игре
            "Lost" игрок проиграл
            "Win" игрок выиграл
        :return: состояние игрока
        """
        return self._s_state

    @state.setter
    def state(self, value: str):
        """
            Проперти для изменения состояния игрока
        :param value: новое значение состояния
        """
        if value == "Play" or value == "Lost" or value == "Win":
            self._s_state = value
        else:
            raise ValueError("Неподдерживаемое состояние игрока.")

    @property
    def name(self):
        """
            Проперти для получения имени игрока
        :return: имя игрока
        """
        return self._s_name

    @name.setter
    def name(self, value: str):
        """
            Проперти для изменеия имени игрока
        :param value: новое значение имени игрока
        """
        self._s_name = value

    @property
    def type(self):
        """
            Проперти представляющее состояние игрока. Может иметь два значения:
            "Computer" компьютер
            "Human" человек
        :return: тип игрока
        """
        return self._s_type

    @type.setter
    def type(self, value):
        """
            Проперти для изменения типа игрока
        :param value: новое значение типа
        """
        if value == "Computer" or value == "Human":
            self._s_type = value
        else:
            raise ValueError("Неподдерживаемый тип игрока.")

    def add_card(self, card: cd.Card):
        """
            Метод для добавления новой карточки игроку
        :param card: новая карточка
        """
        self._l_card.append(card)

    def clean_card(self):
        """
            Метод очистки игрока. Удаляет все ранее прикрепленные игроку карточки
        """
        self._l_card = []

    def check_number(self, number: int):
        """
            Метод, который проверяет наличие номера бочонка указанного
            во входном параметре во всех карточках игрока
        :param number: номер бочонка
        :return: True если бочонок с таким номером существует в карточках игрока
                 False если бочлнка с таким номером не существует в карточках игрока
        """
        b_result = False
        for card in self._l_card:
            if card.is_number_in(number):
                b_result = True
        return b_result

    def get_cards_out(self):
        """
            Метод, который представляет собержимое карточек в качестве строки
        :return: лист из трех элементов, представляющих три строки в карточке
        """
        return [card.card_out() for card in self._l_card]

    def all_played(self):
        """
            Метод, который проверяет наличие незакрытых бочонков. Если у игрока нет незакрытых бочонков,
            то state игрока меняется на "Win"
        """
        if False not in [False for card in self._l_card if not card.is_all_played()]:
            self.state = "Win"

    def __str__(self):
        return f'{self.name} {self.state} {self.type} {len(self._l_card)}'

    def __ne__(self, other):
        if str(self) != str(other):
            return True
        else:
            return False

    def __len__(self):
        return len(self._l_card)
