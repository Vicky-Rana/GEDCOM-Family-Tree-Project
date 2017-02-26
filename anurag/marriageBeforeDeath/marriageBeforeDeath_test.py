import unittest
from marriageBeforeDeath import getFamilyData

class TestMarriageBeforeDeath(unittest.TestCase):
    
    def test3(self):
        res3 = getFamilyData("@F3@")
        self.assertEqual(res3, True)
    
    def test5(self):
        res5 = getFamilyData("@F5@")
    
        self.assertEqual(res5,True)

if __name__ == '__main__':
    unittest.main()