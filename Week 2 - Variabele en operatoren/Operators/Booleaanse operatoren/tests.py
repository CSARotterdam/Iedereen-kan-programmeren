import unittest

from test_helper import run_common_tests, failed, passed
from regex_helper import *
from UserInputHelper import *

helper = Helper()


class varAanmaken(unittest.TestCase):
    def testAnswer1(self):
        self.assertEqual(helper.answers[0], "andA")

    def testAnswer2(self):
        self.assertEqual(helper.answers[1], "True")

    def testAnswer3(self):
        self.assertEqual(helper.answers[2], "False")

    def testAnswer4(self):
        self.assertRegex(helper.answers[3], "boolean|Boolean")

    def testAnswer5(self):
        self.assertEqual(helper.answers[4], "varB")

    def testAnswer6(self):
        self.assertEqual(helper.answers[5], "andC")

    def testAnswer7(self):
        self.assertEqual(helper.answers[6], "False")

    def testAnswer8(self):
        self.assertEqual(helper.answers[7], "orA")

    def testAnswer9(self):
        self.assertEqual(helper.answers[8], "True")

    def testAnswer10(self):
        self.assertEqual(helper.answers[9], "True")

    def testAnswer11(self):
        self.assertEqual(helper.answers[10], "True")

    def testAnswer12(self):
        self.assertEqual(helper.answers[11], "varB")

    def testAnswer13(self):
        self.assertRegex(helper.answers[12], "boolean|Boolean")

    def testAnswer14(self):
        self.assertEqual(helper.answers[13], "notA")

    def testAnswer15(self):
        self.assertEqual(helper.answers[14], "False")

    def testAnswer16(self):
        self.assertEqual(helper.answers[15], "notB")

    def testAnswer17(self):
        self.assertEqual(helper.answers[16], "True")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(testCaseClass=varAanmaken)
    res = unittest.TextTestRunner().run(suite)
    if res.wasSuccessful():
        passed("Congratulations")
    else:
        for el in res.failures:
            failed(f"There is an error in " + str(el[0])[4:12])




