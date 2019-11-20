import unittest

from test_helper import run_common_tests, failed, passed
from regex_helper import *
from UserInputHelper import *

helper = Helper()


class varAanmaken(unittest.TestCase):
    def testAnswer1(self):
        self.assertEqual(helper.answers[0], "40")

    def testAnswer2(self):
        self.assertEqual(helper.answers[1], "2.5")

    def testAnswer3(self):
        self.assertRegex(helper.answers[2], "Float|float")

    def testAnswer4(self):
        self.assertRegex(helper.answers[3], helper.re.expressionToRegex("x * 5 + y / 2"))

    def testAnswer5(self):
        self.assertRegex(helper.answers[4], helper.re.expressionToRegex("expressionB >= expressionA"))

    def testAnswer6(self):
        self.assertRegex(helper.answers[5], helper.re.expressionToRegex("expressionC or expressionA > 40"))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(testCaseClass=varAanmaken)
    res = unittest.TextTestRunner().run(suite)
    if res.wasSuccessful():
        passed("Congratulations")
    else:
        for el in res.failures:
            failed(f"There is an error in " + str(el[0])[4:12])




