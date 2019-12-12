import unittest
import game as gm
import random as rd

class GameTestCase(unittest.TestCase):

    def setUp(self):
        rd.seed(2)
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

    def test_start_game_invalid(self):

        with self.assertRaises(ValueError):
            self.game.start_game(-2, 1, ["Andrey, Computer"], ["Human", "Computer"])

        with self.assertRaises(ValueError):
            self.game.start_game(2, -1, ["Andrey, Computer"], ["Human", "Computer"])

        with self.assertRaises(ValueError):
            self.game.start_game(2, 10, ["Andrey, Computer"], ["Human", "Computer"])

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

    def test_print_player(self):
        self.game._i_card_number = 1
        self.game.add_player("Comp1", "Computer")

        with self.assertRaises(ValueError):
            self.game._l_players[0]._l_card = []
            self.game.print_player(self.game._l_players[0])

    def test_random_number(self):
        random_number = self.game.random_number(99)
        l_out = []
        for i in range(1,100):
            l_out.append(next(random_number))
        s_out = set(l_out)

        self.assertEqual(len(s_out), 99)

if __name__ == '__main__':
    unittest.main()
