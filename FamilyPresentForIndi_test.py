import unittest
from FamilyPresentForIndi import check_family_present_for_individual

class TestUniqueIds(unittest.TestCase):
    """
    Our basic test class
    """

    def test_check_family_present_for_individual(self):
        
        res = check_family_present_for_individual("@I41@")
        self.assertEqual(res, 1)


if __name__ == '__main__':
    unittest.main()