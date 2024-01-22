import unittest
from multiplicar import multiplicar
class TestSumar(unittest.TestCase):
    def test_restar(self):
        self.assertEqual(multiplicar(3, 2), 6)
        self.assertEqual(multiplicar(-1, 1), -1)
        self.assertEqual(multiplicar(-1, -1), 1)
if __name__ == '__main__':
    unittest.main()