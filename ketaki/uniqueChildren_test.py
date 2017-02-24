import unittest
from uniqueChildren import check_childeren_list

class TestUniqueIds(unittest.TestCase):
    """
    Our basic test class
    """

    def test_check_childeren_list(self):
        
        res = check_childeren_list("@F19@")
        self.assertEqual(res, 1)


if __name__ == '__main__':
    unittest.main()