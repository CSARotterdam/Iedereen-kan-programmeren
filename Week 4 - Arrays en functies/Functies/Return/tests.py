import unittest

from test_helper import run_common_tests, failed, passed
from regex_helper import *
from UserInputHelper import *

helper = Helper()


class varAanmaken(unittest.TestCase):
    def testAnswer1(self):
        self.assertEqual(helper.answers[0], "sum")

    def testAnswer2(self):
        self.assertRegex(helper.answers[1], helper.re.argsRegex("5","10"))

    def testAnswer3(self):
        self.assertRegex(helper.answers[2], "integer|Integer")

    def testAnswer4(self):
        self.assertEqual(helper.answers[3], "15")

    def testAnswer5(self):
        self.assertRegex(helper.answers[4], helper.re.argsRegex("10", "5"))

    def testAnswer6(self):
        self.assertRegex(helper.answers[5], "integer|Integer")

    def testAnswer7(self):
        self.assertEqual(helper.answers[6], "15")

    def testAnswer8(self):
        self.assertEqual(helper.answers[7], "str")

    def testAnswer9(self):
        self.assertEqual(helper.answers[8], "\"5\"")

    def testAnswer10(self):
        self.assertRegex(helper.answers[9], "string|String")

    def testAnswer11(self):
        self.assertEqual(helper.answers[10], "sum")

    def testAnswer12(self):
        self.assertRegex(helper.answers[11], helper.re.argsRegex("\"5\"", "\"Hello, World!\""))

    def testAnswer13(self):
        self.assertRegex(helper.answers[12], "string|String")

    def testAnswer14(self):
        self.assertEqual(helper.answers[13], "\"5Hello, World\"")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(testCaseClass=varAanmaken)
    res = unittest.TextTestRunner().run(suite)
    if res.wasSuccessful():
        passed("Congratulations")
    else:
        for el in res.failures:
            failed(f"There is an error in " + str(el[0])[4:12])




