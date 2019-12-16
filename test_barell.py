import unittest
import barell as b


class BarellTestCase(unittest.TestCase):
    def setUp(self):
        self.barell = b.Barell(1,"Ready")

    def test_state_property_valid(self):
        """
            Тест на правильные значения состояния бочонка
        """
        self.assertEqual(self.barell.state, "Ready")
        self.barell.state = "Played"
        self.assertEqual(self.barell.state, "Played")
        self.barell.state = "Empty"
        self.assertEqual(self.barell.state, "Empty")

    def test_state_property_invalid(self):
        """
            Тест на значения состояния бочонка, которые
            должны вызвать exception
        """
        with self.assertRaises(ValueError):
            self.barell.state = "New"
        with self.assertRaises(ValueError):
            self.barell.state = ""
        with self.assertRaises(ValueError):
            self.barell.state = 0
        with self.assertRaises(ValueError):
            self.barell.state = ["Played", "New"]

    def test_number_property_valid(self):
        """
            Тест на правильные значения номера бочонка
        """
        self.assertEqual(self.barell.number, 1)
        self.barell.number = 99
        self.assertEqual(self.barell.number, 99)
        self.barell.number = 50
        self.assertEqual(self.barell.number, 50)
        self.barell.number = 0
        self.assertEqual(self.barell.number, 0)

    def test_number_property_invalid(self):
        """
            Тест на значения номера бочонка, которые должны вызвать exception
        """
        with self.assertRaises(ValueError):
            self.barell.number = -2
        with self.assertRaises(ValueError):
            self.barell.number = 100
        with self.assertRaises(ValueError):
            self.barell.number = 100000000000000000
        with self.assertRaises(ValueError):
            self.barell.number = -100000000000000000
        with self.assertRaises(TypeError):
            self.barell.number = "11"
        with self.assertRaises(TypeError):
            self.barell.number = [0,1,100]


if __name__ == '__main__':
    unittest.main()
