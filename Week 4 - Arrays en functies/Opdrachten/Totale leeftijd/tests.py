import unittest
import runpy
import sys
from test_helper import failed, passed
from UserInputHelper import *

helper = Helper()


class varAanmaken(unittest.TestCase):
    persons = []
    @classmethod
    def setUpClass(cls) -> None:
        global persons
        persons = [['test1', 0], ['test2', 500], ['test3', -50], ['test4', 20]]

    def testPerson1NameShouldBeRetrievedCorrectly(self):
        sys.stdout = open('testoutput.txt', 'w')
        print(runpy.run_module('task', init_globals={'persons': persons}))
        sys.stdout = sys.__stdout__
        self.assertEqual(open('testoutput.txt','r').readlines()[0][10:15], 'test1')

    def testPerson2NameShouldBeRetrievedCorrectly(self):
        sys.stdout = open('testoutput.txt', 'w')
        print(runpy.run_module('task', init_globals={'persons': persons}))
        sys.stdout = sys.__stdout__
        self.assertEqual(open('testoutput.txt','r').readlines()[1][10:15], 'test2')

    def testPerson2AgeShouldBeRetrievedCorrectly(self):
        sys.stdout = open('testoutput.txt', 'w')
        print(runpy.run_module('task', init_globals={'persons': persons}))
        sys.stdout = sys.__stdout__
        self.assertEqual(open('testoutput.txt','r').readlines()[1][26:29], '500')

    def testPerson3AgeShouldBeRetrievedCorrectly(self):
        sys.stdout = open('testoutput.txt', 'w')
        print(runpy.run_module('task', init_globals={'persons': persons}))
        sys.stdout = sys.__stdout__
        self.assertEqual(open('testoutput.txt','r').readlines()[2][26:29], '-50')

    def testPerson4NameShouldBeRetrievedCorrectly(self):
        sys.stdout = open('testoutput.txt', 'w')
        print(runpy.run_module('task', init_globals={'persons': persons}))
        sys.stdout = sys.__stdout__
        self.assertEqual(open('testoutput.txt','r').readlines()[3][10:15], 'test4')

    def testPerson4AgeShouldBeRetrievedCorrectly(self):
        sys.stdout = open('testoutput.txt', 'w')
        print(runpy.run_module('task', init_globals={'persons': persons}))
        sys.stdout = sys.__stdout__
        self.assertEqual(open('testoutput.txt','r').readlines()[3][26:28], '20')

    def testTotalAgeShouldBeRetrievedCorrectly(self):
        sys.stdout = open('testoutput.txt', 'w')
        print(runpy.run_module('task', init_globals={'persons': persons}))
        sys.stdout = sys.__stdout__
        self.assertEqual(open('testoutput.txt','r').readlines()[4][36:39], '470')



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(testCaseClass=varAanmaken)
    res = unittest.TextTestRunner().run(suite)
    if res.wasSuccessful():
        passed("Congratulations")
    else:
        for el in res.failures:
            failed(f"The following condition is not met: " + str(el[0])[4:-23])




