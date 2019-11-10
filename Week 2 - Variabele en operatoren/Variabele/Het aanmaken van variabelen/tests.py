from UserInputHelper import *
from test_helper import run_common_tests, failed, passed
import unittest

helper = Helper()


class varAanmaken(unittest.TestCase):
    def testAnswer1(self):
        self.assertEqual(helper.answers[0], "x")

    def testAnswer2(self):
        self.assertEqual(helper.answers[1], "235")

    def testAnswer3(self):
        self.assertRegex(helper.answers[2], "integer|Integer|int")

    def testAnswer4(self):
        self.assertEqual(helper.answers[3], "stappenteller")

    def testAnswer5(self):
        self.assertEqual(helper.answers[4], "0")

    def testAnswer6(self):
        self.assertEqual(helper.answers[5], "45")

    def testAnswer7(self):
        self.assertRegex(helper.answers[6], "integer|Integer|int")

    def testAnswer8(self):
        self.assertEqual(helper.answers[7], "aantalHoeken")

    def testAnswer9(self):
        self.assertEqual(helper.answers[8], "4")

    def testAnswer10(self):
        self.assertRegex(helper.answers[9], "integer|Integer|int")

    def testAnswer11(self):
        self.assertRegex(helper.answers[10], helper.re.expressionToRegex("varA = -342"))

    def testAnswer12(self):
        self.assertRegex(helper.answers[11], helper.re.expressionToRegex("varB = 244"))

    def testAnswer13(self):
        self.assertRegex(helper.answers[12], helper.re.expressionToRegex("varC = 8942"))




# def test_answer_placeholders():
#     helper = Helper()
#     for answerNumber in range(len(helper.answers)):
#         outcome = False
#         backupText = ""
#         if(answerNumber == 0):
#             outcome = helper.CheckInput(answerNumber, "x")
#         elif(answerNumber == 1):
#             outcome = helper.CheckInput(answerNumber, "235")
#         elif(answerNumber == 2):
#             outcome = helper.CheckInput(answerNumber, "integer|Integer")
#         elif(answerNumber == 3):
#             outcome = helper.CheckInput(answerNumber, "stappenteller")
#         elif(answerNumber == 4):
#             outcome = helper.CheckInput(answerNumber, "0")
#         elif(answerNumber == 5):
#             outcome = helper.CheckInput(answerNumber, "45")
#         elif(answerNumber == 6):
#             outcome = helper.CheckInput(answerNumber, "integer|Integer")
#         elif(answerNumber == 7):
#             outcome = helper.CheckInput(answerNumber, "aantalHoeken")
#         elif(answerNumber == 8):
#             outcome = helper.CheckInput(answerNumber, "4")
#         elif(answerNumber == 9):
#             outcome = helper.CheckInput(answerNumber, "integer|Integer")
#         elif(answerNumber == 10):
#             outcome = helper.CheckInput(answerNumber, helper.re.expressionToRegex("varA = -342"))
#         elif(answerNumber == 11):
#             outcome = helper.CheckInput(answerNumber, helper.re.expressionToRegex("varB = 244"))
#         elif(answerNumber == 12):
#             outcome = helper.CheckInput(answerNumber, helper.re.expressionToRegex("varC = 8942"))
#         CheckOutcome(outcome, answerNumber, backupText)
#
# def CheckOutcome(outcome, answerNumber, backupText):
#     if(outcome):
#         passed("Answer #" + str(answerNumber) + " is correct!")
#     else:
#         failed("There is an error in answer #"+ str(answerNumber)+" " + backupText)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(testCaseClass=varAanmaken)
    res = unittest.TextTestRunner().run(suite)
    if res.wasSuccessful():
        passed("Congratulations")
    else:
        for el in res.failures:
            failed(f"There is an error in " + str(el[0])[4:12])
    # test_answer_placeholders()
