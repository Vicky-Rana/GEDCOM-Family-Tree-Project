import unittest
#from lt150 import age_less_150
from user_story_age_lessthan_150 import age_less_150,if_birthdate_present,if_deathdate_present,age_diffe_non_negative,valid_date

class Test_age_150(unittest.TestCase):
    """
    Our basic test class
    """
    def test_age_less_150(self):        
        res = age_less_150()
        self.assertEqual(res, True)

    def test_birthdate(self):
        res=if_birthdate_present()
        self.assertEqual(res, True)

    def test_valid_date(self):
        res=valid_date()
        self.assertTrue(res, True)

    def test_deathdate(self):
        res=if_deathdate_present()
        self.assertEqual(res, True)

    def test_age_diffe_non_negative(self):
        res=age_diffe_non_negative()
        self.assertEqual(res, True)

if __name__ == '__main__':
    unittest.main()