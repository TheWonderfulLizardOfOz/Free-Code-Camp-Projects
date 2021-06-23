import re
class ArithmeticArranger():
    def __init__(self, problems, outSolution = False):
        self.problems = problems
        self.validProblems = True
        self.errors = {"manyProblems": False, "incorrectOperator": False,
                       "incorrectOperand": False, "operandTooBig": False}
        self.num1 = []
        self.num2 = []
        self.operators = []
        self.totalProblems = len(problems)
        self.counter = 0
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
        self.individualProblems()
        self.validator()
        if self.validProblems == True:
            self.arithmeticArranger()
            finalResult = self.output()
            print(finalResult)
            return finalResult
        else:
            return None
        
    def validator(self):
        for operator in self.operators:
            if operator not in ("+", "-"):
                self.validProblems = False
        for num in self.num1:
            if num.isdigit() == False:
                self.validProblems = False
        for num in self.num2:
            if num.isdigit() == False:
                self.validProblems = False
        
    def individualProblems(self):
        for problem in self.problems:
            nums = self.numberFinder(problem)
            self.num1.append(nums[0])
            self.num2.append(nums[1])
            self.operators.append(self.operatorFinder(problem))
            
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
        #print(finalResult)
        return finalResult
