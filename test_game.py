import unittest
import game as gm
import random as rd
import card as cd
from unittest.mock import patch

l_print_output = []
l_input_in = []

def mock_print(str_to_print):
    l_print_output.append(str_to_print)

def mock_input(x):
    return l_input_in.pop()

class GameTestCase(unittest.TestCase):

    def setUp(self):
        rd.seed(2)
        l_print_output.clear()
        l_input_in.clear()
        l_input_in.append("n")
        l_input_in.append("y")
        self.game = gm.Game()

    def test_add_player(self):

        self.game._i_card_number = 1

        self.assertEqual(True, len(self.game._l_players) == 0)

        self.game.add_player("Comp1", "Computer")
        self.game.add_player("Andrey", "Human")
        self.assertEqual(2, len(self.game._l_players))

        with self.assertRaises(ValueError):
            self.game.add_player("Other", "New")

        self.game.add_player(1, "Computer")

    @patch('builtins.print', side_effect=mock_print)
    @patch('builtins.input', side_effect=mock_input)
    def test_start_game_invalid(self, mock_print, mock_input):

        with self.assertRaises(ValueError):
            self.game.start_game(-2, 1, ["Andrey, Computer"], ["Human", "Computer"])

        with self.assertRaises(ValueError):
            self.game.start_game(2, -1, ["Andrey, Computer"], ["Human", "Computer"])

        with self.assertRaises(ValueError):
            self.game.start_game(2, 10, ["Andrey, Computer"], ["Human", "Computer"])

        self.game.start_game(1, 1, ["Fedor"], ["Human"])
        self.assertEqual(l_print_output[7], "Игрок Fedor проиграл.")


    def test_check_win(self):
        self.game._i_card_number = 1
        self.game.add_player("Comp1", "Computer")
        self.game.add_player("Andrey", "Human")
        self.assertEqual(True, len(self.game.check_win()) == 0)

        self.game._l_players[0].state = "Lost"
        self.assertEqual(True, len(self.game.check_win()) == 0)

        self.game._l_players[1].state = "Lost"
        self.assertEqual(True, len(self.game.check_win()) == 0)

        self.game._l_players[0].state = "Win"
        self.assertEqual(True, len(self.game.check_win()) == 1)

    def test_check_in_play(self):
        self.game._i_card_number = 1
        self.game.add_player("Comp1", "Computer")
        self.game.add_player("Andrey", "Human")
        self.assertEqual(True, len(self.game.check_in_play()) == 2)

        self.game._l_players[0].state = "Lost"
        self.assertEqual(True, len(self.game.check_in_play()) == 1)

        self.game._l_players[1].state = "Win"
        self.assertEqual(True, len(self.game.check_in_play()) == 0)

    @patch('builtins.print', side_effect=mock_print)
    def test_print_player(self, print):
        self.game._i_card_number = 1
        self.game.add_player("Comp1", "Computer")

        with self.assertRaises(ValueError):
            self.game._l_players[0]._l_card = []
            self.game.print_player(self.game._l_players[0])

        o_in = cd.Card()
        o_in.set_card()
        self.game._l_players[0].add_card(o_in)
        self.game.print_player(self.game._l_players[0])

        self.assertEqual(l_print_output[0], "------ Карточки игрока Comp1 ------")
        self.assertEqual(l_print_output[1], "------------------------------------")
        self.assertEqual(str(l_print_output[2]),str(o_in))

    def test_random_number(self):
        random_number = self.game.random_number(99)
        l_out = []
        for i in range(1,100):
            l_out.append(next(random_number))
        s_out = set(l_out)
        self.assertEqual(len(s_out), 99)

        l_out.sort()
        self.assertEqual(l_out[0], 1)
        self.assertEqual(l_out[98], 99)

    def test_str(self):
        self.game._i_card_number = 1
        self.game.add_player("Comp1", "Computer")
        self.game.add_player("Andrey", "Human")
        self.assertEqual(str(self.game), "players: Comp1:Computer Andrey:Human  cards:1")

    def test_ne(self):
        self.game._i_card_number = 1
        self.game.add_player("Comp1", "Computer")
        self.game.add_player("Andrey", "Human")
        self.game1 = gm.Game()
        self.game1._i_card_number = 1
        self.game1.add_player("Comp1", "Computer")
        self.game1.add_player("Andrey", "Human")
        self.assertEqual(False, self.game != self.game1)

        self.game1.add_player("Fedor", "Human")
        self.assertEqual(True, self.game != self.game1)

    def test_len(self):
        self.assertEqual(99, len(self.game))

        self.game._i_number_barells_left = 55
        self.assertEqual(55, len(self.game))



if __name__ == '__main__':
    unittest.main()
