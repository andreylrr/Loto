import unittest
import barell as b

class BarellTestCase(unittest.TestCase):
    def setUp(self):
        self.barell = b.Barell()

    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
