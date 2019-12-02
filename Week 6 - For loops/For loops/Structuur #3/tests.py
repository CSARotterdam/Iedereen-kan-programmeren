import unittest

from test_helper import run_common_tests, failed, passed
from regex_helper import *
from UserInputHelper import *

helper = Helper()


class varAanmaken(unittest.TestCase):
    def testAnswer1(self):
        self.assertEqual(helper.answers[0], "array")

    def testAnswer2(self):
        self.assertEqual(helper.answers[1], "5")

    def testAnswer3(self):
        self.assertEqual(helper.answers[2], "1")

    def testAnswer4(self):
        self.assertEqual(helper.answers[3], "False")

    def testAnswer5(self):
        self.assertRegex(helper.answers[4], helper.re.rangeRegex("len\(array\)"))

    def testAnswer6(self):
        self.assertEqual(helper.answers[5], "5")

    def testAnswer7(self):
        self.assertEqual(helper.answers[6], "0")

    def testAnswer8(self):
        self.assertEqual(helper.answers[7], "4")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(testCaseClass=varAanmaken)
    res = unittest.TextTestRunner().run(suite)
    if res.wasSuccessful():
        passed("Congratulations")
    else:
        for el in res.failures:
            failed(f"There is an error in " + str(el[0])[4:12])




