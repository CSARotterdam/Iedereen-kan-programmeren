import unittest

from test_helper import run_common_tests, failed, passed
from regex_helper import *
from UserInputHelper import *

helper = Helper()


class varAanmaken(unittest.TestCase):
    def testAnswer1(self):
        self.assertEqual(helper.answers[0], "sumA")

    def testAnswer2(self):
        self.assertEqual(helper.answers[1], "9")

    def testAnswer3(self):
        self.assertRegex(helper.answers[2], "integer|Integer|int")

    def testAnswer4(self):
        self.assertRegex(helper.answers[3], "varA|varC")

    def testAnswer5(self):
        self.assertEqual(helper.answers[4], "sumB")

    def testAnswer6(self):
        self.assertRegex(helper.answers[2], "integer|Integer|int")

    def testAnswer7(self):
        self.assertRegex(helper.answers[6], "varA|varC")

    def testAnswer8(self):
        self.assertEqual(helper.answers[7], "subA")

    def testAnswer9(self):
        self.assertRegex(helper.answers[8], "integer|Integer|int")

    def testAnswer10(self):
        self.assertRegex(helper.answers[9], helper.re.expressionToRegex("sumB - varB"))

    def testAnswer11(self):
        self.assertEqual(helper.answers[10], "subB")

    def testAnswer12(self):
        self.assertRegex(helper.answers[11], "integer|Integer|int")

    def testAnswer13(self):
        self.assertEqual(helper.answers[12], "varB")

    def testAnswer14(self):
        self.assertEqual(helper.answers[13], "multA")

    def testAnswer15(self):
        self.assertEqual(helper.answers[14], "varD")

    def testAnswer16(self):
        self.assertEqual(helper.answers[15], "powA")

    def testAnswer17(self):
        self.assertEqual(helper.answers[16], "6")

    def testAnswer18(self):
        self.assertRegex(helper.answers[17], helper.re.expressionToRegex("varC ** varD") +
                         "|" + helper.re.expressionToRegex("varA ** varD"))



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(testCaseClass=varAanmaken)
    res = unittest.TextTestRunner().run(suite)
    if res.wasSuccessful():
        passed("Congratulations")
    else:
        for el in res.failures:
            failed(f"There is an error in " + str(el[0])[4:12])


