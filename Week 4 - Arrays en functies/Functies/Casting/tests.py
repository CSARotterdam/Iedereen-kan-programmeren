import unittest

from test_helper import run_common_tests, failed, passed
from regex_helper import *
from UserInputHelper import *

helper = Helper()


class varAanmaken(unittest.TestCase):
    def testAnswer1(self):
        self.assertEqual(helper.answers[0], "int")

    def testAnswer2(self):
        self.assertEqual(helper.answers[1], "\"123\"")

    def testAnswer3(self):
        self.assertEqual(helper.answers[2], "string")

    def testAnswer4(self):
        self.assertEqual(helper.answers[3], "123")

    def testAnswer5(self):
        self.assertRegex(helper.answers[4], "integer|Integer")

    def testAnswer6(self):
        self.assertEqual(helper.answers[5], "str")

    def testAnswer7(self):
        self.assertEqual(helper.answers[6], "123")

    def testAnswer8(self):
        self.assertEqual(helper.answers[7], "integer")

    def testAnswer9(self):
        self.assertEqual(helper.answers[8], "\"123\"")

    def testAnswer10(self):
        self.assertRegex(helper.answers[9], "string|String")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(testCaseClass=varAanmaken)
    res = unittest.TextTestRunner().run(suite)
    if res.wasSuccessful():
        passed("Congratulations")
    else:
        for el in res.failures:
            failed(f"There is an error in " + str(el[0])[4:12])




