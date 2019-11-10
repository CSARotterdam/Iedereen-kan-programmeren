from test_helper import PlaceHolder
from regex_helper import *

class Helper:
    def __init__(self):
        self.re = regex_helper()
        self.answers = PlaceHolder.get_answer_placeholders()

    def CheckBaseType(self, index, type):
        answer = self.GetInput(index)
        outcome = False
        if(type=="boolean"):
            outcome = self.re.execute(answer, self.re.BOOLEAN)
        elif(type=="float"):
            outcome = self.re.execute(answer, self.re.FLOAT)
        elif(type=="string"):
            outcome = self.re.execute(answer, self.re.STRING)
        elif(type=="integer"):
            outcome = self.re.execute(answer, self.re.INTEGER)
        return outcome

    def CheckInput(self, index, regexString):
        return self.re.execute(self.GetInput(index), regexString)

    def GetInput(self, index):
        return self.answers[index]
