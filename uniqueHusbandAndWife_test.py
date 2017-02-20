import unittest
from uniqueHusbandAndWife import check_unique_husband_wife

class TestUniqueIds(unittest.TestCase):
    """
    Our basic test class
    """

    def test_check_unique_husband_wife(self):
        
        res = check_unique_husband_wife("@F19@")
        self.assertEqual(res, 1)


if __name__ == '__main__':
    unittest.main()