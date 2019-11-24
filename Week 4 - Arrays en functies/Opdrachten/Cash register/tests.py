import unittest
import runpy
import sys
from test_helper import failed, passed
from UserInputHelper import *

helper = Helper()


class varAanmaken(unittest.TestCase):
    products, amounts = [], []
    @classmethod
    def setUpClass(cls) -> None:
        global products, amounts
        products = [['test1', 1], ['test2', -2], ['test3', 4]]
        amounts = [20, 500, 3]

    def testAnswer1(self):
        self.assertEqual(helper.answers[0], "products[0][0]")

    def testAnswer2(self):
        self.assertEqual(helper.answers[1], "products[1][0]")

    def testAnswer3(self):
        self.assertEqual(helper.answers[2], "products[2][0]")

    def testTotalShouldBeCalculatedCorrectly(self):
        sys.stdout = open('testoutput.txt', 'w')
        print(runpy.run_module('task', init_globals={'products': products, 'amounts':amounts}))
        sys.stdout = sys.__stdout__
        self.assertEqual(open('testoutput.txt','r').readlines()[0][17:21], '-968')



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(testCaseClass=varAanmaken)
    res = unittest.TextTestRunner().run(suite)
    if res.wasSuccessful():
        passed("Congratulations")
    else:
        for el in res.failures:
            failed(f"The following condition is not met: " + str(el[0])[4:-23])




