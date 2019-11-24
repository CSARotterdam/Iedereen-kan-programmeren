import unittest

from test_helper import run_common_tests, failed, passed
from regex_helper import *
from UserInputHelper import *

helper = Helper()


class varAanmaken(unittest.TestCase):
    def testAnswer1(self):
        self.assertEqual(helper.answers[0], "element")

    def testAnswer2(self):
        self.assertEqual(helper.answers[1], "array1")

    def testAnswer3(self):
        self.assertEqual(helper.answers[2], "1")

    def testAnswer4(self):
        self.assertEqual(helper.answers[3], "5")

    def testAnswer5(self):
        self.assertEqual(helper.answers[4], "symbol")

    def testAnswer6(self):
        self.assertEqual(helper.answers[5], "string1")

    def testAnswer7(self):
        self.assertEqual(helper.answers[6], "4")

    def testAnswer8(self):
        self.assertEqual(helper.answers[7], "\"a\"")

    def testAnswer9(self):
        self.assertEqual(helper.answers[8], "\"d\"")

    def testAnswer10(self):
        self.assertEqual(helper.answers[9], "\"abc\"")

    def testAnswer11(self):
        self.assertEqual(helper.answers[10], "True")

    def testAnswer12(self):
        self.assertEqual(helper.answers[11], "True")

    def testAnswer13(self):
        self.assertEqual(helper.answers[12], "3")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(testCaseClass=varAanmaken)
    res = unittest.TextTestRunner().run(suite)
    if res.wasSuccessful():
        passed("Congratulations")
    else:
        for el in res.failures:
            failed(f"There is an error in " + str(el[0])[4:12])




