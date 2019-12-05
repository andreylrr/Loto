
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
        self.i_number = number
        self.s_state = state

    @property
    def number(self):
        """
            Проперти для получения номера, ассоциированного с данным бочонком
        :return: номер бочонка
        """
        return self.i_number

    @number.setter
    def number(self, value):
        """
            Проперти для изменеия номера бочонка
        :param value: новое значение номера бочонка
        """
        self.i_number = value

    @property
    def state(self):
        """
            Проперти для получения состояния бочонка
        :return: состояние бочонка
        """
        return self.s_state

    @state.setter
    def state(self, value):
        """
            Проперти для изменения состояния бочонка

        :param value: новое значение состояния бочонка
        """
        self.s_state = value
