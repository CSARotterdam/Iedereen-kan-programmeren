import unittest

from test_helper import run_common_tests, failed, passed
from regex_helper import *
from UserInputHelper import *

helper = Helper()


class varAanmaken(unittest.TestCase):
    def testAnswer1(self):
        self.assertEqual(helper.answers[0], "7")

    def testAnswer2(self):
        self.assertRegex(helper.answers[1], "integer|Integer")

    def testAnswer3(self):
        self.assertEqual(helper.answers[2], "4")

    def testAnswer4(self):
        self.assertRegex(helper.answers[3], "integer|Integer")

    def testAnswer5(self):
        self.assertEqual(helper.answers[4], "\"31\"")

    def testAnswer6(self):
        self.assertRegex(helper.answers[5], "string|String")

    def testAnswer7(self):
        self.assertEqual(helper.answers[6], "\"abc\"")

    def testAnswer8(self):
        self.assertRegex(helper.answers[7], "string|String")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(testCaseClass=varAanmaken)
    res = unittest.TextTestRunner().run(suite)
    if res.wasSuccessful():
        passed("Congratulations")
    else:
        for el in res.failures:
            failed(f"There is an error in " + str(el[0])[4:12])




