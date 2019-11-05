from test_helper import get_answer_placeholders
from regex_helper import *

class Helper:
    def __init__(self):
        self.helper = regex_helper()
        self.answers = get_answer_placeholders()

    def CheckBaseType(self, index, type):
        answer = self.GetInput(index)
        outcome = False
        if(type=="boolean"):
            outcome = self.helper.execute(answer, self.helper.BOOLEAN)
        elif(type=="float"):
            outcome = self.helper.execute(answer, self.helper.FLOAT)
        elif(type=="string"):
            outcome = self.helper.execute(answer, self.helper.STRING)
        elif(type=="integer"):
            outcome = self.helper.execute(answer, self.helper.INTEGER)
        return outcome

    def CheckInput(self, index, regexString):
        return self.helper.execute(self.GetInput(index), regexString)

    def GetInput(self, index):
        return self.answers[index]
