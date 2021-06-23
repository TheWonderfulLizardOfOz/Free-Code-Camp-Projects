import re
class ArithmeticArranger():
    def __init__(self, problems, outSolution = False):
        self.problems = problems
        self.validProblems = True
        self.errors = {"incorrectOperator": False, "incorrectOperand": False,
                       "operandTooBig": False}
        self.num1 = []
        self.num2 = []
        self.operators = []
        self.totalProblems = len(problems)
        self.counter = 0
        self.errorCounter = 0
        self.topLine = ""
        self.bottomLine = ""
        self.dashLine = ""
        self.solutionLine = ""
        self.outSolution = outSolution

    def returnResults(self):
        self.topLine = ""
        self.bottomLine = ""
        self.dashLine = ""
        self.solutionLine = ""
        self.errorCounter = 0
        self.individualProblems()
        if self.errorCounter == 0:
            self.arithmeticArranger()
            finalResult = self.output()
            return finalResult
        else:
            errorMessage = self.errorMessageCreator()
            return errorMessage

    def errorMessageCreator(self):
        message = ""
        if self.totalProblems > 5:
            return "Error: Too many problems."
        if self.errors["incorrectOperator"] == True:
            message += "Error: Operator must be '+' or '-'.\n"
        if self.errors["incorrectOperand"] == True:
            message += "Error: Numbers must only contain digits.\n"
        if self.errors["operandTooBig"] == True:
            message += "Error: Numbers cannot be more than four digits."
        message = message.strip("\n")
        return message
        
    def validator(self, splitProblem, num1, num2, operator):
        if operator not in ("+", "-"):
            self.errors["incorrectOperator"] = True
            self.errorCounter += 1
        if num1 != splitProblem[0]:
            self.errors["incorrectOperand"] = True
            self.errorCounter += 1
        if num2 != splitProblem[2]:
            self.errors["incorrectOperand"] = True
            self.errorCounter += 1
        if len(str(num1)) > 4:
            self.errors["operandTooBig"] = True
            self.errorCounter += 1
        if len(str(num2)) > 4:
            self.errors["operandTooBig"] = True
            self.errorCounter += 1
        if self.totalProblems > 5:
            self.errorCounter += 1
            
    def individualProblems(self):
        for problem in self.problems:
            nums = self.numberFinder(problem)
            self.num1.append(nums[0])
            self.num2.append(nums[1])
            operator = self.operatorFinder(problem)
            self.operators.append(operator)
            splitProblem = problem.split()
            self.validator(splitProblem, nums[0], nums[1], operator)
            
    def operatorFinder(self, problem):
        operator = re.findall("[+-]", problem)
        if len(operator) == 0:
            operator = "[&]"
        return str(operator)[2].strip()

    def numberFinder(self, problem):
        nums = re.findall("[0-9]+", problem)
        return nums

    def findBiggestLength(self, num1, num2):
        lnum1 = len(str(num1))
        lnum2 = len(str(num2))
        if lnum1 > lnum2:
            return lnum1
        else:
            return lnum2

    def arrangeTop(self, num1, totalLength, biggestLength):
        if len(str(num1)) == biggestLength:
            self.topLine += " " + " " + str(num1)
        else:
            totalToAdd = totalLength - len(str(num1))
            self.topLine += " "*totalToAdd + str(num1)
        if self.counter != self.totalProblems:
            self.topLine += " "*4

    def arrangeBottom(self, num2, totalLength, biggestLength, operator):
        self.bottomLine += str(operator) + " "
        if len(str(num2)) != biggestLength:
            totalToAdd = totalLength - len(str(num2)) - 2
            self.bottomLine += " "*totalToAdd
        self.bottomLine += str(num2)
        if self.counter != self.totalProblems:
            self.bottomLine += " "*4

    def arrangeSolutionLine(self, solution, totalLength, biggestLength):
        if self.outSolution == False:
            return None
        if len(str(solution)) == biggestLength:
            self.solutionLine += " " + " " + str(solution)
            if self.counter != self.totalProblems:
                self.solutionLine += " "*4
        else:
            totalToAdd = totalLength - len(str(solution))
            self.solutionLine += " "*totalToAdd
            self.solutionLine += str(solution)
            if self.counter != self.totalProblems:
                self.solutionLine += " "*4
        
    def solve(self, num1, num2, operator):
        solution = eval(str(num1) + str(operator) + str(num2))
        return solution

    def createDashLine(self, totalLength):
        self.dashLine += "-"*totalLength
        if self.counter != self.totalProblems:
            self.dashLine +=" "*4
        
    def arithmeticArranger(self):
        self.counter = 0
        for i in range(self.totalProblems):
            self.counter += 1
            if self.outSolution == True:
                solution = self.solve(self.num1[i], self.num2[i], self.operators[i])
            else:
                solution = None
            biggestLength = self.findBiggestLength(self.num1[i], self.num2[i])
            totalLength = biggestLength + 2
            self.arrangeTop(self.num1[i], totalLength, biggestLength)
            self.arrangeBottom(self.num2[i], totalLength, biggestLength, self.operators[i])
            self.arrangeSolutionLine(solution, totalLength, biggestLength)
            self.createDashLine(totalLength)
    
    def output(self):
        finalResult = self.topLine + "\n" + self.bottomLine + "\n" + self.dashLine
        if self.outSolution == True:
            finalResult += "\n" + self.solutionLine
        return finalResult
