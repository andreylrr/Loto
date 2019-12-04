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
        return {i: b.Barell(0,"Empty") for i in range(1,10)}

    def is_number_in(self, number):
        b_result = False
        for x in self.l_lines:
            for barell in x.values():
                if barell.number == number:
                    barell.state = "Played"
                    b_result = True
        return b_result

    def is_all_played(self):
        b_result = True
        for x in self.l_lines:
            for barell in x.values():
                if barell.state == "Ready":
                    b_result = False
        return b_result

    def card_out(self):
        l_out = []
        for d_line in self.l_lines:
            l_out.append(self.line_out(d_line))
        return l_out

    def line_out(self, card_dict):
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
        self.l_lines = list(map(self.set_line, self.l_lines))

    def set_line(self, card_dict):
        l_number = random.sample(range(1,100), 5)
        l_number.sort()
        l_position = random.sample(range(1,10), 5)
        l_position.sort()
        if len(set(l_number)) == 5 and len(set(l_position)) == 5 :
            for i,i_position in enumerate(l_position):
                card_dict[i_position].number = l_number[i]
                card_dict[i_position].state = "Ready"
        return card_dict


