import unittest
from uniqueFamIds import check_distinct_Family

class TestUniqueIds(unittest.TestCase):
    """
    Our basic test class
    """

    def test_check_distinct_Family(self):
        
        res = check_distinct_Family("@F19@")
        self.assertEqual(res, "true")


if __name__ == '__main__':
    unittest.main()