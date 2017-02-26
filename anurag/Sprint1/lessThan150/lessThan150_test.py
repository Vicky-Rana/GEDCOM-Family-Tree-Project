import unittest

from lessThan150 import age_less_150

class Test_age_150(unittest.TestCase):
    """
    Our basic test class
    """
    def test_age_less_150(self):        
        res = age_less_150()
        self.assertEqual(res, True)


if __name__ == '__main__':
    unittest.main()