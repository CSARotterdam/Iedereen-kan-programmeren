import unittest

from test_helper import run_common_tests, failed, passed
from regex_helper import *
from UserInputHelper import *

helper = Helper()


class varAanmaken(unittest.TestCase):
    def testAnswer1(self):
        self.assertEqual(helper.answers[0], "while")

    def testAnswer2(self):
        self.assertEqual(helper.answers[1], "condition")

    def testAnswer3(self):
        self.assertEqual(helper.answers[2], "condition")

    def testAnswer4(self):
        self.assertEqual(helper.answers[3], "5")

    def testAnswer5(self):
        self.assertRegex(helper.answers[4], helper.re.argsRegex('if', 'else'))

    def testAnswer6(self):
        self.assertRegex(helper.answers[5], "Ja|ja")

    def testAnswer7(self):
        self.assertEqual(helper.answers[6], "counter")

    def testAnswer8(self):
        self.assertRegex(helper.answers[7], helper.re.expressionToRegex("counter <= 4"))

    def testAnswer9(self):
        self.assertEqual(helper.answers[8], "5")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(testCaseClass=varAanmaken)
    res = unittest.TextTestRunner().run(suite)
    if res.wasSuccessful():
        passed("Congratulations")
    else:
        for el in res.failures:
            failed(f"There is an error in " + str(el[0])[4:12])




