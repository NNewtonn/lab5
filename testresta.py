import unittest
from restar import restar
class TestSumar(unittest.TestCase):
    def test_restar(self):
        self.assertEqual(restar(3, 2), 1)
        self.assertEqual(restar(-1, 1), -2)
        self.assertEqual(restar(-1, -1), 0)
if __name__ == '__main__':
    unittest.main()