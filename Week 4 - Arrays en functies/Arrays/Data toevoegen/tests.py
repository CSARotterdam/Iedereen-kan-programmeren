import unittest

from test_helper import run_common_tests, failed, passed
from regex_helper import *
from UserInputHelper import *

helper = Helper()


class varAanmaken(unittest.TestCase):
    def testAnswer1(self):
        self.assertRegex(helper.answers[0], helper.re.listRegex("\"first\""))

    def testAnswer2(self):
        self.assertRegex(helper.answers[1], "list|List|array|Array")

    def testAnswer3(self):
        self.assertEqual(helper.answers[2], "emptyArray")

    def testAnswer4(self):
        self.assertRegex(helper.answers[3], helper.re.listRegex("\"first\"", "\"second\""))

    def testAnswer5(self):
        self.assertRegex(helper.answers[4], helper.re.listRegex("1", "2", "3", "1"))

    def testAnswer6(self):
        self.assertRegex(helper.answers[5], helper.re.listRegex("\"1\"", "\"2\"", "\"3\"", "\"4\""))

    def testAnswer7(self):
        self.assertRegex(helper.answers[6], helper.re.listRegex("13", "1", "2", "3", "1"))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(testCaseClass=varAanmaken)
    res = unittest.TextTestRunner().run(suite)
    if res.wasSuccessful():
        passed("Congratulations")
    else:
        for el in res.failures:
            failed(f"There is an error in " + str(el[0])[4:12])




