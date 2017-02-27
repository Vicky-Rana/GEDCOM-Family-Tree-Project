import unittest

from UniqueUserNameAndBirthDate import unique_name_bdate,valid_date

class Test1_UniqueUserNameAndBirthDate(unittest.TestCase):
    """
    Our basic test class
    """
    def test_unique_name_bdate(self):        
        res = unique_name_bdate()
        self.assertEqual(res, True)
		
class Test2_UniqueUserNameAndBirthDate(unittest.TestCase):

    def test_unique_name_bdate(self):
        res = unique_name_bdate()
        self.assertNotEqual(res, False)
		

		
class Test3_UniqueUserNameAndBirthDate(unittest.TestCase):		

    def test_unique_name_bdate(self):
        res= unique_name_bdate()
        self.assertTrue(res, True)	
	
class Test4_UniqueUserNameAndBirthDate(unittest.TestCase):

    def test_valid_date(self):
        res = valid_date()
        self.assertIs(res, True)
	
class Test5_UniqueUserNameAndBirthDate(unittest.TestCase):

    def test_valid_date(self):
        res = valid_date()
        self.assertIsNotNone(res)

if __name__ == '__main__':
    unittest.main()