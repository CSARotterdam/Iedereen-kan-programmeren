import unittest

from test_helper import run_common_tests, failed, passed
from regex_helper import *
from UserInputHelper import *

helper = Helper()


class varAanmaken(unittest.TestCase):
    def testAnswer1(self):
        self.assertRegex(helper.answers[0], helper.re.expressionToRegex("x = \"World\""))

    def testAnswer2(self):
        self.assertRegex(helper.answers[1], helper.re.expressionToRegex("y = y + 1"))

    def testAnswer3(self):
        self.assertRegex(helper.answers[2], helper.re.expressionToRegex("z = True"))

    def testAnswer4(self):
        self.assertRegex(helper.answers[3], helper.re.expressionToRegex("x = 0"))

    def testAnswer5(self):
        self.assertRegex(helper.answers[4], helper.re.expressionToRegex("y = 0"))

    def testAnswer6(self):
        self.assertRegex(helper.answers[5], helper.re.expressionToRegex("z = 0"))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(testCaseClass=varAanmaken)
    res = unittest.TextTestRunner().run(suite)
    if res.wasSuccessful():
        passed("Congratulations")
    else:
        for el in res.failures:
            failed(f"There is an error in " + str(el[0])[4:12])


