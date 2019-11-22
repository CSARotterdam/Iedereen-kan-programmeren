import re

class regex_helper:
    VAR_STRUCTURE = "^[_|a-zA-Z]\w*\s*=\s*(\".*\"|\'.*\'|\d+|\d+\.\d+|True|False)$"
    FLOAT = "^\d*\.\d*$"
    STRING = "^[\"\'].*[\"\']$"
    INTEGER = "^(?<!\d\.)(-)*\d+(?!\.\d)$"
    BOOLEAN = "(True|False)$"
    COMMENT = "#.*$"
    opArrNoEscape = ["-", "/", "//", "%",
                     "=", "-=", "/=", "//=", "&=", ">>=", "<<=",
                     "==", "!=", ">", "<", ">=", "<=",
                     "and", "or",
                     "is", "is not",
                     "in", "not in",
                     "&", "~", "<<", ">>", ]
    opArrMustBeEscaped = ["+", "*", "+=", "*=", "|=", "^=", "|", "^", ]
    opArrMustBeEscapedTwice = ["**", "**=", ]
    opArrArity1 = ["not", ]
    ifLine1 = "if()"

    opArr = opArrNoEscape + opArrMustBeEscaped + opArrMustBeEscapedTwice + opArrArity1

    # Create a regex matching any applicable operands being applied to any given operator
    def createOperatorPattern(self, operator, *operands):
        if operator in self.opArrMustBeEscaped:
            return f"^{operands[0]}\s*\{operator}\s*{operands[1]}$"
        elif operator in self.opArrMustBeEscapedTwice:
            return f"^{operands[0]}\s*\{operator[0]}\{operator[1:]}\s*{operands[1]}$"
        elif operator in self.opArrNoEscape:
            return f"^{operands[0]}\s*{operator}\s*{operands[1]}$"
        elif operator in self.opArrArity1:
            return f"^{operator}\s*{operands[0]}$"
        else:
            return "^$"

    # Create a regex matching a given expression
    # Param: operands - Indexable collection containing all operands in left to right order
    # Param: operators - Indexable collection containing all operators in left to right order
    def createExpressionPattern(self, operands, operators):
        regexOut = "^"

        # sanitizing String operands
        escOperands = []
        for operand in operands:
            escOperands.append(operand.translate(str.maketrans({"\"": r"\""})))

        print(escOperands)
        count = 0
        loopOps = escOperands[0:-1]

        # Looping through Operators and operands 0 through N-1
        # Because of the structure of expressions, we can encounter up to two operators between each operand.
        for operand in loopOps:
            if operators[count] in self.opArrArity1 and count < len(operators) - 1:
                regexOut += f"{operators[count]}\s*"
                count = count + 1 if count < len(operators) - 1 else count

            regexOut += operand + "\s*"

            if count < len(operators):
                if operators[count] in self.opArrMustBeEscaped:
                    regexOut += f"\{operators[count]}\s*"
                elif operators[count] in self.opArrMustBeEscapedTwice:
                    regexOut += f"\{operators[count][0]}\{operators[count][1:]}\s*"
                else:
                    regexOut += f"{operators[count]}\s*"
                count = count + 1 if count < len(operators) - 1 else count

        # Adding final operand and optionally operator
        if operators[-1] in self.opArrArity1:
            regexOut += f"{operators[-1]}\s*{escOperands[-1]}"
        else:
            regexOut += f"{escOperands[-1]}$"

        return regexOut

    # Takes in an expression as it would be typed in regular python, and returns a regex matching that expression.
    def expressionToRegex(self, stringIn):
        operands = []
        operators = []

        PATTERN = re.compile(r'''((?:[^ "']|"[^"]*"|'[^']*')+)''')
        for word in PATTERN.split(stringIn)[1::2]:
            if word in self.opArr:
                operators.append(word)
            else:
                operands.append(word)

        return self.createExpressionPattern(operands, operators)

    def ifRegex(self,conditionStr):
        ifRegex = "if *(\( *"
        ifRegex2 = " *\)| *"
        ifRegex3 = " *):"
        condRegex = self.expressionToRegex(conditionStr)[1:-1]
        return ifRegex + condRegex + ifRegex2 + condRegex + ifRegex3

    def whileRegex(self,conditionStr):
        whileRegex = "while *(\( *"
        whileRegex2 = " *\)| *"
        whileRegex3 = " *):"
        condRegex = self.expressionToRegex(conditionStr)[1:-1]
        return whileRegex + condRegex + whileRegex2 + condRegex + whileRegex3

    def forRegex(self,iteratorStr,collectionStr):
        return f"^for\s*(({iteratorStr})|(\({iteratorStr}\)))\s*in\s*(({collectionStr})|(\({collectionStr}\))):\s*$"

    def argsRegex(self, *args):
        out = "^" + args[0] + "\s*"
        for string in args[1:]:
            out += ",\s*" + string + "\s*"
        out += "$"
        return out

    def splitSpace(self, stringIn):
        PATTERN = re.compile(r'''(-|/|//|%|==|=|-=|/=|//=|&=|>>=|<<=|!=|>|<|>=|<=|&|~|<<|>>|\+|\*|\+=|\*=|\|=|\^=|\||\^|\*\*|\*\*=)''')
        arrout = []
        for el in PATTERN.split(stringIn):
            arrout.append(el.strip())
        return arrout

    def CheckAbstractAbstraction(self, input):
        self.baseExecute(input, )

    def setupRegex(self):
        pass

    def baseExecute(self, input, structure):
        pattern = re.compile(structure)
        matches = pattern.findall(input)
        return matches

    def execute(self, input, structure):
        return len(self.baseExecute(input, structure)) > 0

    def varStructureCheck(self, input):
        return self.execute(input, self.VAR_STRUCTURE)

    def customVarMatch(self, input, varName, varData):
        return self.execute(input, varName + "\s*=\s*" + varData)

    def typeCheck(self, input, type):
        structure = ""
        if type == "string":
            structure = self.STRING
        elif type == "integer":
            structure = self.INTEGER
        elif type == "float":
            structure = self.FLOAT
        elif type == "boolean":
            structure = self.BOOLEAN
        else:
            pass
        return self.execute(input, structure)
