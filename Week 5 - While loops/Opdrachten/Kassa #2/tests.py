import unittest

from test_helper import run_common_tests, failed, passed
from regex_helper import *
from UserInputHelper import *

helper = Helper()


class varAanmaken(unittest.TestCase):
    def testAnswer1(self):
        self.assertRegex(helper.answers[0],
                         helper.re.expressionToRegex("index < len\(products\)") +
                         "|" +
                         helper.re.expressionToRegex("index != len\(products\)"))

    def testAnswer2(self):
        self.assertRegex(helper.answers[1],
                         helper.re.expressionToRegex("total = total + products\[index\]\[1\] * amounts\[index\]") +
                         "|" +
                         helper.re.expressionToRegex("total += products\[index\]\[1\] * amounts\[index\]"))

    def testAnswer3(self):
        self.assertRegex(helper.answers[2], helper.re.expressionToRegex("index = index + 1") +
                         "|" +
                         helper.re.expressionToRegex("index += 1"))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(testCaseClass=varAanmaken)
    res = unittest.TextTestRunner().run(suite)
    if res.wasSuccessful():
        passed("Congratulations")
    else:
        for el in res.failures:
            failed(f"There is an error in " + str(el[0])[4:12])
