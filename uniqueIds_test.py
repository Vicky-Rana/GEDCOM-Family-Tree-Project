import unittest
from uniqueIds import check_distinct_individual

class TestUniqueIds(unittest.TestCase):
    """
    Our basic test class
    """

    def test_check_distinct_individual(self):
        
        res = check_distinct_individual("@I41@")
        self.assertEqual(res, "true")


if __name__ == '__main__':
    unittest.main()