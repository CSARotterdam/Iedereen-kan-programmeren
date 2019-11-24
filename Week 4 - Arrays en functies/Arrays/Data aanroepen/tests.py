import unittest

from test_helper import run_common_tests, failed, passed
from regex_helper import *
from UserInputHelper import *

helper = Helper()


class varAanmaken(unittest.TestCase):
    def testAnswer1(self):
        self.assertEqual(helper.answers[0], "a")

    def testAnswer2(self):
        self.assertEqual(helper.answers[1], "3")

    def testAnswer3(self):
        self.assertEqual(helper.answers[2], "2")

    def testAnswer4(self):
        self.assertRegex(helper.answers[3], "integer|Integer")

    def testAnswer5(self):
        self.assertEqual(helper.answers[4], "\"3\"")

    def testAnswer6(self):
        self.assertRegex(helper.answers[5], "string|String")

    def testAnswer7(self):
        self.assertEqual(helper.answers[6], "\"1\"")

    def testAnswer8(self):
        self.assertRegex(helper.answers[7], "String|string")

    def testAnswer9(self):
        self.assertRegex(helper.answers[8], helper.re.listRegex("\"1\"", "\"2\"", "\"3\""))

    def testAnswer10(self):
        self.assertRegex(helper.answers[9], "list|List")

    def testAnswer11(self):
        self.assertEqual(helper.answers[10], "f")

    def testAnswer12(self):
        self.assertEqual(helper.answers[11], "1")

    def testAnswer13(self):
        self.assertEqual(helper.answers[12], "\"3\"")

    def testAnswer14(self):
        self.assertRegex(helper.answers[13], helper.re.listRegex())

    def testAnswer15(self):
        self.assertRegex(helper.answers[14], "list|List")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(testCaseClass=varAanmaken)
    res = unittest.TextTestRunner().run(suite)
    if res.wasSuccessful():
        passed("Congratulations")
    else:
        for el in res.failures:
            failed(f"There is an error in " + str(el[0])[4:12])
