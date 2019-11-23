import unittest
import runpy
import sys
from test_helper import failed, passed
from UserInputHelper import *

helper = Helper()


class varAanmaken(unittest.TestCase):
    def testNumberUnder0ShouldGiveOption1(self):
        sys.stdout = open('testoutput.txt', 'w')
        print(runpy.run_module('task', init_globals={'number': -1, 'randomNumber': 50}))
        sys.stdout = sys.__stdout__
        self.assertEqual(open('testoutput.txt','r').readline(), 'No negative numbers!\n')

    def testNumberUnderRandomShouldGiveOption2(self):
        sys.stdout = open('testoutput.txt', 'w')
        print(runpy.run_module('task', init_globals={'number': 1, 'randomNumber': 50}))
        sys.stdout = sys.__stdout__
        self.assertEqual(open('testoutput.txt','r').readline(), 'The number is below the random number.\n')

    def testNumberEqualToRandomShouldGiveOption3(self):
        sys.stdout = open('testoutput.txt', 'w')
        print(runpy.run_module('task', init_globals={'number': 50, 'randomNumber': 50}))
        sys.stdout = sys.__stdout__
        self.assertEqual(open('testoutput.txt','r').readline(), 'The number is equal to the random number!\n')

    def testNumberAboveRandomShouldGiveOption4(self):
        sys.stdout = open('testoutput.txt', 'w')
        print(runpy.run_module('task', init_globals={'number': 51, 'randomNumber': 50}))
        sys.stdout = sys.__stdout__
        self.assertEqual(open('testoutput.txt','r').readline(), 'The number is above the random number.\n')

    def testNumberAbove100ShouldGiveOption5(self):
        sys.stdout = open('testoutput.txt', 'w')
        print(runpy.run_module('task', init_globals={'number': 101, 'randomNumber': 50}))
        sys.stdout = sys.__stdout__
        self.assertEqual(open('testoutput.txt','r').readline(), 'No numbers higher than 100!\n')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(testCaseClass=varAanmaken)
    res = unittest.TextTestRunner().run(suite)
    if res.wasSuccessful():
        passed("Congratulations")
    else:
        for el in res.failures:
            failed(f"The following condition is not met: " + str(el[0])[4:-23])




