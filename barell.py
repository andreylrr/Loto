
"""

    Класс Barell представляет бочонок с номером

"""

class Barell ():

    def __init__(self, number, state):
        """
            Метод инициализации класса Barell
        :param number: - номер ассоциированный с данными бочонком
        :param state: - состояние бочонка. Возможны тра варианта:
                        "Ready" бочонок создан и готов к игре
                        "Played" бочонок, номер которого уже был вытащен из мешка
                        "Empty" бочонок создан, но не имеет никакого присоединненого номера

        """
        self.number = number
        self.state = state

    @property
    def number(self):
        """
            Проперти для получения номера, ассоциированного с данным бочонком
        :return: номер бочонка
        """
        return self._i_number

    @number.setter
    def number(self, value: int):
        """
            Проперти для изменеия номера бочонка
        :param value: новое значение номера бочонка
        """
        if value < 0 or value > 99:
            raise ValueError("Неверное значение номера бочонка.")
        else:
            self._i_number = value

    @property
    def state(self):
        """
            Проперти для получения состояния бочонка
        :return: состояние бочонка
        """
        return self._s_state

    @state.setter
    def state(self, value):
        """
            Проперти для изменения состояния бочонка

        :param value: новое значение состояния бочонка
        """
        if value == "Played" or value == "Ready" or value == "Empty":
            self._s_state = value
        else:
            raise ValueError("Неподдерживаемое состояние бочонка.")

    def __str__(self):
        if self.state == "Ready":
            return f'Бочонок номер {self.number} создан и готов к игре.'
        elif self.state == "Played":
            return f'Бочнок номер {self.number} уже был вытащен из мешка.'
        elif self.state == "Empty":
            return f'Бочонок создан, но не имеет никакого номера.'
        return f'Ни номер ни состояние бочонка неопределены.'

    
