import unittest

from test_helper import run_common_tests, failed, passed
from regex_helper import *
from UserInputHelper import *

helper = Helper()


class varAanmaken(unittest.TestCase):
    def testAnswer1(self):
        self.assertEqual(helper.answers[0], "len")

    def testAnswer2(self):
        self.assertRegex(helper.answers[1], helper.re.listRegex("1", "2", "3"))

    def testAnswer3(self):
        self.assertRegex(helper.answers[2], "list|List|array|Array")

    def testAnswer4(self):
        self.assertEqual(helper.answers[3], "3")

    def testAnswer5(self):
        self.assertRegex(helper.answers[4], helper.re.listRegex("\"ab\"", "\"bcd\"", "\"efgh\""))

    def testAnswer6(self):
        self.assertRegex(helper.answers[5], "list|List|array|Array")

    def testAnswer7(self):
        self.assertEqual(helper.answers[6], "3")

    def testAnswer8(self):
        self.assertRegex(helper.answers[7], "integer|Integer")

    def testAnswer9(self):
        self.assertEqual(helper.answers[8], "\"ab\"")

    def testAnswer10(self):
        self.assertRegex(helper.answers[9], "string|String")

    def testAnswer11(self):
        self.assertEqual(helper.answers[10], "2")

    def testAnswer12(self):
        self.assertEqual(helper.answers[11], "\"efgh\"")

    def testAnswer13(self):
        self.assertRegex(helper.answers[12], "string|String")

    def testAnswer14(self):
        self.assertEqual(helper.answers[13], "4")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(testCaseClass=varAanmaken)
    res = unittest.TextTestRunner().run(suite)
    if res.wasSuccessful():
        passed("Congratulations")
    else:
        for el in res.failures:
            failed(f"There is an error in " + str(el[0])[4:12])




