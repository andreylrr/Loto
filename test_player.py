import unittest
import player as pl
import card as cd
import random as rd

class PlayerTestCase(unittest.TestCase):
    def setUp(self):
        self.player = pl.Player("Компьютер")
        rd.seed(2)

    def test_state_property_valid(self):
        self.player.state = "Play"
        s_state = self.player.state
        self.assertEqual(s_state, "Play")
        self.player.state = "Lost"
        s_state = self.player.state
        self.assertEqual(s_state, "Lost")
        self.player.state = "Win"
        s_state = self.player.state
        self.assertEqual(s_state, "Win")

    def test_state_property_invalid(self):
        with self.assertRaises(ValueError):
            self.player.state = "New"
        with self.assertRaises(ValueError):
            self.player.state = ""
        with self.assertRaises(ValueError):
            self.player.state = 1
        with self.assertRaises(ValueError):
            self.player.state = ["Play"]

    def test_name_property(self):
        self.player.name = "Игорь"
        s_out = self.player.name
        self.assertEqual(s_out, "Игорь")
        self.player.name = 1
        s_out = self.player.name
        self.assertEqual(s_out, 1)

    def test_type_property_valid(self):
        self.player.type = "Computer"
        s_out = self.player.type
        self.assertEqual(s_out, "Computer")
        self.player.type = "Human"
        s_out = self.player.type
        self.assertEqual(s_out, "Human")

    def test_type_property_invalid(self):
        with self.assertRaises(ValueError):
            self.player.type = "New"
        with self.assertRaises(ValueError):
            self.player.type = 1
        with self.assertRaises(ValueError):
            self.player.type = 2
        with self.assertRaises(ValueError):
            self.player.type = ["Computer"]

    def test_add_card(self):
        self.player.add_card(cd.Card())
        self.assertEqual(1, len(self.player._l_card))
        self.player.add_card(cd.Card())
        self.assertEqual(2, len(self.player._l_card))

    def test_clean_card(self):
        self.player.add_card(cd.Card())
        self.assertEqual(1, len(self.player._l_card))
        self.player.clean_card()
        self.assertEqual(True, len(self.player._l_card) == 0)

    def test_check_number(self):
        o_card1 = cd.Card()
        o_card1.set_card()
        o_card2 = cd.Card()
        o_card2.set_card()
        self.player.add_card(o_card1)
        self.player.add_card(o_card2)

        b_result = self.player.check_number(8)
        self.assertEqual(b_result, True)
        b_result = self.player.check_number(56)
        self.assertEqual(b_result, True)
        b_result = self.player.check_number(60)
        self.assertEqual(b_result, True)
        b_result = self.player.check_number(23)
        self.assertEqual(b_result, True)
        b_result = self.player.check_number(66)
        self.assertEqual(b_result, True)
        b_result = self.player.check_number(76)
        self.assertEqual(b_result, True)
        b_result = self.player.check_number(47)
        self.assertEqual(b_result, True)

        b_result = self.player.check_number(1)
        self.assertEqual(b_result, False)
        b_result = self.player.check_number(99)
        self.assertEqual(b_result, False)
        b_result = self.player.check_number(0)
        self.assertEqual(b_result, False)
        b_result = self.player.check_number(3000)
        self.assertEqual(b_result, False)

    def test_get_cards_out(self):
        o_card1 = cd.Card()
        o_card1.set_card()
        o_card2 = cd.Card()
        o_card2.set_card()
        self.player.add_card(o_card1)
        self.player.add_card(o_card2)

        l_out = self.player.get_cards_out()
        self.assertEqual(l_out[0][0], "      8          11      12  22  47 ")
        self.assertEqual(l_out[0][1], "              5  21  56  75      88 ")
        self.assertEqual(l_out[0][2], "      4       5  35  47  60         ")
        self.assertEqual(l_out[1][0], "      4  23      30  31  72         ")
        self.assertEqual(l_out[1][1], "         24      47  66  72  87     ")
        self.assertEqual(l_out[1][2], "     21          46  47  58  76     ")

    def test_all_played(self):
        o_card1 = cd.Card()
        o_card1.set_card()
        o_card2 = cd.Card()
        o_card2.set_card()
        self.player.add_card(o_card1)
        self.player.add_card(o_card2)

        self.player.check_number(8)
        self.player.check_number(11)
        self.player.check_number(12)
        self.player.check_number(22)
        self.player.check_number(47)
        self.player.check_number(5)
        self.player.check_number(21)
        self.player.check_number(56)
        self.player.check_number(75)
        self.player.check_number(88)
        self.player.check_number(4)
        self.player.check_number(35)
        self.player.check_number(60)
        self.player.check_number(23)
        self.player.check_number(30)
        self.player.check_number(31)
        self.player.check_number(72)
        self.player.check_number(24)
        self.player.check_number(66)
        self.player.check_number(87)
        self.player.check_number(46)
        self.player.check_number(58)

        self.player.all_played()
        self.assertNotEqual("Win", self.player.state)

        self.player.check_number(76)
        self.player.all_played()
        self.assertEqual("Win", self.player.state)

if __name__ == '__main__':
    unittest.main()
