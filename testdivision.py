import unittest
from dividir import dividir
class TestSumar(unittest.TestCase):
    def test_restar(self):
        self.assertEqual(dividir(4, 2), 2)
        self.assertEqual(dividir(-1, 1), -1)
        self.assertEqual(dividir(-1, -1), 1)
        #x
        with self.assertRaises(ValueError):
            try:
                dividir(5, 0)
            except:
                raise ValueError
            
if __name__ == '__main__':
    unittest.main()