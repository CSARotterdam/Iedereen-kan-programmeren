import unittest

from test_helper import run_common_tests, failed, passed
from regex_helper import *
from UserInputHelper import *

helper = Helper()


class varAanmaken(unittest.TestCase):
    def testAnswer1(self):
        self.assertEqual(helper.answers[0], "equA")

    def testAnswer2(self):
        self.assertRegex(helper.answers[1], "boolean|Boolean")

    def testAnswer3(self):
        self.assertEqual(helper.answers[2], "equB")

    def testAnswer4(self):
        self.assertEqual(helper.answers[3], "True")

    def testAnswer5(self):
        self.assertEqual(helper.answers[4], "uneqA")

    def testAnswer6(self):
        self.assertEqual(helper.answers[5], "True")

    def testAnswer7(self):
        self.assertEqual(helper.answers[6], "varD")

    def testAnswer8(self):
        self.assertRegex(helper.answers[7], "boolean|Boolean")

    def testAnswer9(self):
        self.assertEqual(helper.answers[8], "largerA")

    def testAnswer10(self):
        self.assertEqual(helper.answers[9], "False")

    def testAnswer11(self):
        self.assertEqual(helper.answers[10], "largerB")

    def testAnswer12(self):
        self.assertEqual(helper.answers[11], "varA")

    def testAnswer13(self):
        self.assertEqual(helper.answers[12], "True")

    def testAnswer14(self):
        self.assertEqual(helper.answers[13], "True")

    def testAnswer15(self):
        self.assertEqual(helper.answers[14], "True")

    def testAnswer16(self):
        self.assertEqual(helper.answers[15], "False")

    def testAnswer17(self):
        self.assertEqual(helper.answers[16], "smallerequA")

    def testAnswer18(self):
        self.assertEqual(helper.answers[17], "True")

    def testAnswer19(self):
        self.assertEqual(helper.answers[18], "False")



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(testCaseClass=varAanmaken)
    res = unittest.TextTestRunner().run(suite)
    if res.wasSuccessful():
        passed("Congratulations")
    else:
        for el in res.failures:
            failed(f"There is an error in " + str(el[0])[4:12])


