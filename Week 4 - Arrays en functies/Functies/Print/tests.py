import unittest

from test_helper import run_common_tests, failed, passed
from regex_helper import *
from UserInputHelper import *

helper = Helper()


class varAanmaken(unittest.TestCase):
    def testAnswer1(self):
        self.assertEqual(helper.answers[0], "print")

    def testAnswer2(self):
        self.assertEqual(helper.answers[1], "5")

    def testAnswer3(self):
        self.assertRegex(helper.answers[2], "integer|Integer")

    def testAnswer4(self):
        self.assertEqual(helper.answers[3], "\"5\"")

    def testAnswer5(self):
        self.assertRegex(helper.answers[4], "string|String")

    def testAnswer6(self):
        self.assertEqual(helper.answers[5], "True")

    def testAnswer7(self):
        self.assertRegex(helper.answers[6], "boolean|Boolean")

    def testAnswer8(self):
        self.assertRegex(helper.answers[7],
                         helper.re.listRegex("5", "\"5\"", "True") + "|" +
                         helper.re.listRegex("x", "y", "z"))

    def testAnswer9(self):
        self.assertRegex(helper.answers[8], "list|List")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(testCaseClass=varAanmaken)
    res = unittest.TextTestRunner().run(suite)
    if res.wasSuccessful():
        passed("Congratulations")
    else:
        for el in res.failures:
            failed(f"There is an error in " + str(el[0])[4:12])
