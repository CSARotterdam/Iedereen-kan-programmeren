import unittest
import runpy
import sys
from test_helper import failed, passed
from UserInputHelper import *

helper = Helper()


class varAanmaken(unittest.TestCase):
    def testLessThan18ShouldGive10(self):
        sys.stdout = open('testoutput.txt', 'w')
        print(runpy.run_module('task', init_globals={'Age': 17}))
        sys.stdout = sys.__stdout__
        self.assertEqual(open('testoutput.txt','r').readline(), 'Reduction = 10%\n')

    def test18ShouldGive0(self):
        sys.stdout = open('testoutput.txt', 'w')
        print(runpy.run_module('task', init_globals={'Age': 18}))
        sys.stdout = sys.__stdout__
        self.assertEqual(open('testoutput.txt','r').readline(), 'Reduction = 0%\n')

    def testBetween18And65ShouldGive0(self):
        sys.stdout = open('testoutput.txt', 'w')
        print(runpy.run_module('task', init_globals={'Age': 19}))
        sys.stdout = sys.__stdout__
        self.assertEqual(open('testoutput.txt','r').readline(), 'Reduction = 0%\n')

    def test65ShouldGive0(self):
        sys.stdout = open('testoutput.txt', 'w')
        print(runpy.run_module('task', init_globals={'Age': 65}))
        sys.stdout = sys.__stdout__
        self.assertEqual(open('testoutput.txt','r').readline(), 'Reduction = 0%\n')

    def testOver65ShouldGive25(self):
        sys.stdout = open('testoutput.txt', 'w')
        print(runpy.run_module('task', init_globals={'Age': 66}))
        sys.stdout = sys.__stdout__
        self.assertEqual(open('testoutput.txt','r').readline(), 'Reduction = 25%\n')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(testCaseClass=varAanmaken)
    res = unittest.TextTestRunner().run(suite)
    if res.wasSuccessful():
        passed("Congratulations")
    else:
        for el in res.failures:
            failed(f"The following condition is not met: " + str(el[0])[4:-23])




