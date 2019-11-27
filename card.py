import random
import barell as b


class Card():

    def __init__(self):
        self.clean()

    def clean(self):
        self.l_lines = []
        for i in range(3):
            self.l_lines.append(self.clean_line())

    def clean_line(self):
        return {i: b.Barell(0,"Empty") for i in range(1,9)}

    def is_number_in(self, number):
        pass

    def card_out(self):
        l_out = []
        for d_line in self.l_lines:
            l_out.append(self.line_out(d_line))
        return l_out

    def line_out(self, card_dict):
        s_out = ""
        for barell in card_dict:
            if barell.state == "Empty":
                s_out += "   "
            elif barell.state == "Ready":
                s_out += str(barell.number)
            elif barell.state == "Played":
                s_out += "---"
        return s_out

    def set_card(self):
        map(self.set_line, self.l_lines)

    def set_line(self, card_dict):
        l_number = random.sample(range(1,100), 5)
        l_number.sort()
        i_position = 0
        while True:
            i_r_position = random.randint(1,9)
            if card_dict[i_r_position].state == "Empty":
                card_dict[i_r_position].number = l_number[i_position]
                card_dict[i_r_position].state = "Ready"
                i_position += 1
            if i_position > 5:
                break
        return card_dict
