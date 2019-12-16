import unittest
import barell as b
import card as c
import random as rd

class CardTestCase(unittest.TestCase):
    def setUp(self):
        self.card = c.Card()
        rd.seed(2)

    def test_card_clean(self):
        b_result = True
        for dic in self.card._l_lines:
            for i in range(1,10):
                if dic[i].state != "Empty" or dic[i].number != 0:
                    b_result = False
                    break
        self.assertEqual(b_result, True)

    def test_clean_line(self):
        b_result = True
        dic = self.card.clean_line()
        for i in range(1,10):
            if dic[i].state != "Empty" or dic[i].number != 0:
                b_result = False
                break
        self.assertEqual(b_result, True)

    def test_number_in(self):
        self.card.clean()
        self.card._l_lines[0][1].number = 7
        self.card._l_lines[0][1].state = "Ready"
        b_result = self.card.is_number_in(7)
        self.assertEqual(b_result, True)

        b_result = self.card.is_number_in(8)
        self.assertEqual(b_result, False)

        self.card._l_lines[0][1].state = "Played"
        b_result = self.card.is_number_in(7)
        self.assertEqual(b_result, False)

        self.card._l_lines[0][1].state = "Empty"
        b_result = self.card.is_number_in(7)
        self.assertEqual(b_result, False)

        self.card._l_lines[0][1].number = 7
        self.card._l_lines[0][1].state = "Ready"
        self.card.is_number_in(7)
        self.assertEqual(True, self.card._l_lines[0][1].state == "Played")

    def test_all_played(self):
        self.card.clean()
        self.card._l_lines[0][1].number = 7
        self.card._l_lines[0][1].state = "Ready"
        b_result = self.card.is_all_played()
        self.assertEqual(b_result, False)

        self.card.clean()
        b_result = self.card.is_all_played()
        self.assertEqual(b_result, True)

    def test_card_out(self):
        self.card.clean()
        self.card._l_lines[0][1].number = 7
        self.card._l_lines[0][1].state = "Ready"
        l_out = self.card.card_out()
        self.assertEqual(l_out[0], "  7                                 ")
        self.assertEqual(l_out[1], "                                    ")
        self.assertEqual(l_out[2], "                                    ")

        self.card._l_lines[1][8].number = 77
        self.card._l_lines[1][8].state = "Ready"
        self.card._l_lines[2][5].number = 99
        self.card._l_lines[2][5].state = "Ready"
        self.card._l_lines[2][6].number = 98
        self.card._l_lines[2][6].state = "Played"
        l_out = self.card.card_out()
        self.assertEqual(l_out[0], "  7                                 ")
        self.assertEqual(l_out[1], "                             77     ")
        self.assertEqual(l_out[2], "                 99 ---             ")


    def test_line_out(self):
        self.card.clean()
        self.card._l_lines[0][1].number = 7
        self.card._l_lines[0][1].state = "Ready"
        l_out = self.card.line_out(self.card._l_lines[0])
        self.assertEqual(l_out, "  7                                 ")

        self.card._l_lines[2][5].number = 99
        self.card._l_lines[2][5].state = "Ready"
        self.card._l_lines[2][6].number = 98
        self.card._l_lines[2][6].state = "Played"
        l_out = self.card.line_out(self.card._l_lines[2])
        self.assertEqual(l_out, "                 99 ---             ")

    def test_card_set(self):
        self.card.set_card()
        l_out = self.card.card_out()
        self.assertEqual(l_out[0], "      8          11      12  22  47 ")
        self.assertEqual(l_out[1], "              5  21  56  75      88 ")
        self.assertEqual(l_out[2], "      4       5  35  47  60         ")

    def test_set_line(self):
        d_card = self.card.set_line(self.card._l_lines[0])
        d_out = self.card.line_out(d_card)
        self.assertEqual(d_out, "      8          11      12  22  47 ")

    def test_str(self):
        self.card.set_card()
        s_out = "".join([x + "\n" for x in ["      8          11      12  22  47 ",
                                            "              5  21  56  75      88 ",
                                            "      4       5  35  47  60         "
                                            ]])
        self.assertEqual(str(self.card), s_out)

    def test_ne(self):
        self.card.set_card()
        self.card1 = c.Card()
        self.card1.set_card()
        self.assertEqual(True, self.card1 != self.card)


if __name__ == '__main__':
    unittest.main()
