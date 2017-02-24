import unittest
from childrenLessThan5 import getChildrenList

class TestChildrenLessThan5(unittest.TestCase):
    def test1(self):
        res = getChildrenList("@F1@")
        self.assertEqual(res, True)
    def test2(self):
        res2 = getChildrenList("@F2@")
        self.assertEqual(res2, True)
    def test3(self):
        res3 = getChildrenList("@F3@")
        self.assertEqual(res3, True)
    def test4(self):
        res4 = getChildrenList("@F4@")
        self.assertEqual(res4, True)
    def test5(self):
        res5 = getChildrenList("@F5@")
        self.assertTrue(res5)
        #self.assertEqual(res5,"TRUE")

if __name__ == '__main__':
    unittest.main()