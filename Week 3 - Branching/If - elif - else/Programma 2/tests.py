import unittest

from test_helper import run_common_tests, failed, passed
from regex_helper import *
from UserInputHelper import *

helper = Helper()


class varAanmaken(unittest.TestCase):
    def testAnswer1(self):
        self.assertRegex(helper.answers[0], helper.re.argsRegex("if", "elif", "else"))

    def testAnswer2(self):
        self.assertRegex(helper.answers[1], "Ja|ja")

    def testAnswer3(self):
         self.assertEqual(helper.answers[2], helper.re.argsRegex("x"))

    def testAnswer4(self):
        self.assertRegex(helper.answers[3], helper.re.expressionToRegex("x > 1"))

    def testAnswer5(self):
        self.assertEqual(helper.answers[4], "False")

    def testAnswer6(self):
        self.assertRegex(helper.answers[5], helper.re.argsRegex("2"))

    def testAnswer7(self):
         self.assertEqual(helper.answers[6], "Ja|ja")

    def testAnswer8(self):
       self.assertEqual(helper.answers[7], helper.re.argsRegex("z","y"))

    def testAnswer9(self):
        self.assertRegex(helper.answers[8], helper.re.expressionToRegex("z <= y"))

    def testAnswer10(self):
        self.assertRegex(helper.answers[9], helper.re.argsRegex("True"))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(testCaseClass=varAanmaken)
    res = unittest.TextTestRunner().run(suite)
    if res.wasSuccessful():
        passed("Congratulations")
    else:
        for el in res.failures:
            failed(f"There is an error in " + str(el[0])[4:12])




