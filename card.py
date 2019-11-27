import random
import barell as b


class Card():

    def __init__(self):
        self.clean()


    def clean(self):
        self.l_lines = []
        d_1 = dict()
        d_2 = dict()
        d_3 = dict()

        for i in range(1, 15):
            d_1[i] = b.Barell(0, "Empty")
            d_2[i] = b.Barell(0, "Empty")
            d_3[i] = b.Barell(0, "Empty")

        self.l_lines.append(d_1)
        self.l_lines.append(d_2)
        self.l_lines.append(d_3)


    def is_number_in(self, number):
        pass

    def card_out(self):
        pass

    def set_card(self):
        for x in self.l_lines:
            i_
            while True:
                i_r_position = random.randint(1, 9)
                i_r_number = random.random(1, 99)
                if x[i_r_position].value.state == "Empty":
                    x[i_r_position].value.number = i_r_number
                    x[i_r_position].value.state = "Ready"




        pass
