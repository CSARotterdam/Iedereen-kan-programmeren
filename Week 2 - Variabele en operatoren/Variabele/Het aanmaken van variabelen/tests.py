from test_helper import run_common_tests, failed, passed, get_answer_placeholders
from regex_helper import *
from UserInputHelper import *

def test_answer_placeholders():
    helper = Helper()
    for answerNumber in range(len(helper.answers)):
        outcome = False
        backupText = ""
        if(answerNumber == 0):
            outcome = helper.CheckInput(answerNumber, "x")
        elif(answerNumber == 1):
            outcome = helper.CheckInput(answerNumber, "235")
        elif(answerNumber == 2):
            outcome = helper.CheckInput(answerNumber, "integer|Integer")
        elif(answerNumber == 3):
            outcome = helper.CheckInput(answerNumber, "stappenteller")
        elif(answerNumber == 4):
            outcome = helper.CheckInput(answerNumber, "0")
        elif(answerNumber == 5):
            outcome = helper.CheckInput(answerNumber, "45")
        elif(answerNumber == 6):
            outcome = helper.CheckInput(answerNumber, "integer|Integer")
        elif(answerNumber == 7):
            outcome = helper.CheckInput(answerNumber, "aantalHoeken")
        elif(answerNumber == 8):
            outcome = helper.CheckInput(answerNumber, "4")
        elif(answerNumber == 9):
            outcome = helper.CheckInput(answerNumber, "integer|Integer")
        elif(answerNumber == 10):
            outcome = helper.CheckInput(answerNumber, helper.helper.expressionToRegex("varA = -342"))
        elif(answerNumber == 11):
            outcome = helper.CheckInput(answerNumber, helper.helper.expressionToRegex("varB = 244"))
        elif(answerNumber == 12):
            outcome = helper.CheckInput(answerNumber, helper.helper.expressionToRegex("varC = 8942"))
        CheckOutcome(outcome, answerNumber, backupText)

def CheckOutcome(outcome, answerNumber, backupText):
    if(outcome):
        passed("Answer #" + str(answerNumber) + " is correct!")
    else:
        failed("There is an error in answer #"+ str(answerNumber)+" " + backupText)

if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()


