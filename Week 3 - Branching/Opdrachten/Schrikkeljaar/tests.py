import unittest
import runpy
import sys
from test_helper import failed, passed
from UserInputHelper import *

helper = Helper()


class varAanmaken(unittest.TestCase):
    def testYearDivisibleby400ShouldGiveLeapYear(self):
        sys.stdout = open('testoutput.txt', 'w')
        print(runpy.run_module('task', init_globals={'year': 2000}))
        sys.stdout = sys.__stdout__
        self.assertEqual(open('testoutput.txt','r').readline(), '2000 is a leap year!\n')

    def testYearDivisibleBy100ButNot400ShouldGiveCommonYear(self):
        sys.stdout = open('testoutput.txt', 'w')
        print(runpy.run_module('task', init_globals={'year': 1900}))
        sys.stdout = sys.__stdout__
        self.assertEqual(open('testoutput.txt','r').readline(), '1900 is a common year!\n')

    def testYearDivisibleBy4ButNot100ShouldGiveLeapYear(self):
        sys.stdout = open('testoutput.txt', 'w')
        print(runpy.run_module('task', init_globals={'year': 2004}))
        sys.stdout = sys.__stdout__
        self.assertEqual(open('testoutput.txt','r').readline(), '2004 is a leap year!\n')

    def testYearNotDivisibleBy4ShouldGiveCommonYear(self):
        sys.stdout = open('testoutput.txt', 'w')
        print(runpy.run_module('task', init_globals={'year': 2003}))
        sys.stdout = sys.__stdout__
        self.assertEqual(open('testoutput.txt','r').readline(), '2003 is a common year!\n')



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(testCaseClass=varAanmaken)
    res = unittest.TextTestRunner().run(suite)
    if res.wasSuccessful():
        passed("Congratulations")
    else:
        for el in res.failures:
            failed(f"The following condition is not met: " + str(el[0])[4:-23])




