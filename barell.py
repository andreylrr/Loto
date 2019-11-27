

class Barell ():

    def __init__(self, number, state):
        self.i_number = number
        self.s_state = state

    @property
    def number(self):
        return self.i_number

    @number.setter
    def number(self, value):
        self.i_number = value

    @property
    def state(self):
        return self.s_state

    @state.setter
    def state(self, value):
        self.s_state = value
