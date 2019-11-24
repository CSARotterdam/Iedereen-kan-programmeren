import unittest

from test_helper import run_common_tests, failed, passed
from regex_helper import *
from UserInputHelper import *

helper = Helper()


class varAanmaken(unittest.TestCase):
    def testAnswer1(self):
        self.assertEqual(helper.answers[0], "20")

    def testAnswer2(self):
        self.assertEqual(helper.answers[1], "0")

    def testAnswer3(self):
        self.assertEqual(helper.answers[2], "19")

    def testAnswer4(self):
        self.assertEqual(helper.answers[3], "y")

    def testAnswer5(self):
        self.assertRegex(helper.answers[4], helper.re.rangeRegex("10", helper.re.expressionToRegex("40 // 4 + 3")[1:-1]))

    def testAnswer6(self):
        self.assertEqual(helper.answers[5], "3")

    def testAnswer7(self):
        self.assertEqual(helper.answers[6], "12")

    def testAnswer8(self):
        self.assertRegex(helper.answers[7], helper.re.rangeRegex("0"))

    def testAnswer9(self):
        self.assertEqual(helper.answers[8], "0")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(testCaseClass=varAanmaken)
    res = unittest.TextTestRunner().run(suite)
    if res.wasSuccessful():
        passed("Congratulations")
    else:
        for el in res.failures:
            failed(f"There is an error in " + str(el[0])[4:12])




