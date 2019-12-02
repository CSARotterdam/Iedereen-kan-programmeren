import unittest

from test_helper import run_common_tests, failed, passed
from regex_helper import *
from UserInputHelper import *

helper = Helper()


class varAanmaken(unittest.TestCase):
    def testAnswer1(self):
        self.assertRegex(helper.answers[0], helper.re.argsRegex("index", "array1"))

    def testAnswer2(self):
        self.assertRegex(helper.answers[1], helper.re.expressionToRegex("index < len\(array1\)"))

    def testAnswer3(self):
        self.assertEqual(helper.answers[2], "3")

    def testAnswer4(self):
        self.assertEqual(helper.answers[3], "index")

    def testAnswer5(self):
        self.assertRegex(helper.answers[4], helper.re.expressionToRegex("index >= 0"))

    def testAnswer6(self):
       self.assertEqual(helper.answers[5], "3")

    def testAnswer7(self):
        self.assertRegex(helper.answers[6], helper.re.argsRegex("array1","array2"))

    def testAnswer8(self):
        self.assertRegex(helper.answers[7], helper.re.expressionToRegex("len\(array1\) == len\(array2\)"))

    def testAnswer9(self):
        self.assertEqual(helper.answers[8], "1")

    def testAnswer10(self):
        self.assertRegex(helper.answers[9], helper.re.argsRegex("index","array2"))

    def testAnswer11(self):
        self.assertRegex(helper.answers[10], helper.re.expressionToRegex("index < len\(array2\)"))

    def testAnswer12(self):
        self.assertEqual(helper.answers[11], "3")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(testCaseClass=varAanmaken)
    res = unittest.TextTestRunner().run(suite)
    if res.wasSuccessful():
        passed("Congratulations")
    else:
        for el in res.failures:
            failed(f"There is an error in " + str(el[0])[4:12])




