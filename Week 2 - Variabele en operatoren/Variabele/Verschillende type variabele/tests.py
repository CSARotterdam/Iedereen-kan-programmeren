from UserInputHelper import *
from test_helper import run_common_tests, failed, passed
import unittest

helper = Helper()


class varAanmaken(unittest.TestCase):
    def testAnswer1(self):
        self.assertEqual(helper.answers[0], "varA")

    def testAnswer2(self):
        self.assertEqual(helper.answers[1], "\"string\"")

    def testAnswer3(self):
        self.assertEqual(helper.answers[2], "\"stringString\"")

    def testAnswer4(self):
        self.assertRegex(helper.answers[3], "string|string")

    def testAnswer5(self):
        self.assertEqual(helper.answers[4], "varC")

    def testAnswer6(self):
        self.assertEqual(helper.answers[5], "0")

    def testAnswer7(self):
        self.assertRegex(helper.answers[6], "integer|Integer|int")

    def testAnswer8(self):
        self.assertEqual(helper.answers[7], "varD")

    def testAnswer9(self):
        self.assertEqual(helper.answers[8], "1")

    def testAnswer10(self):
        self.assertRegex(helper.answers[9], "integer|Integer|int")

    def testAnswer11(self):
        self.assertRegex(helper.answers[10], helper.re.expressionToRegex("varE = 145.1"))

    def testAnswer12(self):
        self.assertEqual(helper.answers[11], "23.5345")

    def testAnswer13(self):
        self.assertRegex(helper.answers[12], "float|Float")

    def testAnswer14(self):
        self.assertRegex(helper.answers[13], helper.re.expressionToRegex("varG = True"))

    def testAnswer15(self):
        self.assertEqual(helper.answers[14], "varH")

    def testAnswer16(self):
        self.assertEqual(helper.answers[15], "False")

    def testAnswer17(self):
        self.assertRegex(helper.answers[16], "boolean|Boolean")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(testCaseClass=varAanmaken)
    res = unittest.TextTestRunner().run(suite)
    if res.wasSuccessful():
        passed("Congratulations")
    else:
        for el in res.failures:
            failed(f"There is an error in {el[0]}")


