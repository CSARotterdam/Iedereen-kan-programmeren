import unittest

from test_helper import run_common_tests, failed, passed
from regex_helper import *
from UserInputHelper import *

helper = Helper()


class varAanmaken(unittest.TestCase):
    def testAnswer1(self):
        self.assertEqual(helper.answers[0], "emptyArray")

    def testAnswer2(self):
        self.assertRegex(helper.answers[1], "leeg|Leeg")

    def testAnswer3(self):
        self.assertRegex(helper.answers[2], helper.re.argsRegex("1", "2", "3"))

    def testAnswer4(self):
        self.assertRegex(helper.answers[3], "list|List")

    def testAnswer5(self):
        self.assertRegex(helper.answers[4], helper.re.argsRegex("\"1\"", "\"2\"", "\"3\""))

    def testAnswer6(self):
        self.assertRegex(helper.answers[5], "list|List")

    def testAnswer7(self):
        self.assertEqual(helper.answers[6], "arrayOfArrays")

    def testAnswer8(self):
        self.assertRegex(helper.answers[7], helper.re.argsRegex("emptyArray", "integerArray", "stringArray"))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(testCaseClass=varAanmaken)
    res = unittest.TextTestRunner().run(suite)
    if res.wasSuccessful():
        passed("Congratulations")
    else:
        for el in res.failures:
            failed(f"There is an error in " + str(el[0])[4:12])




