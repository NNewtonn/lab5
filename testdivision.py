import unittest
from dividir import dividir
class TestSumar(unittest.TestCase):
    def test_restar(self):
        self.assertEqual(dividir(4, 2), 2)
        self.assertEqual(dividir(-1, 1), -1)
        self.assertEqual(dividir(-1, -1), 1)
        with self.assertRaises(ValueError):
            dividir(5, 0)
if __name__ == '__main__':
    unittest.main()