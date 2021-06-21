import re
class ArithmeticArranger():
    def __init__(self, problems, outSolution = False):
        self.problems = problems
        self.validProblems = True
        self.errors = {}
        self.num1 = []
        self.num2 = []
        self.operands = []
        self.totalProblems = len(problems)
        self.topLine = ""
        self.bottomLine = ""
        self.dashLine = ""
        self.solutionLine = ""
        self.outSolution = outSolution
        self.individualProblems()
        self.validator()

    def returnResults(self):
        if self.validProblems == True:
            self.arithmeticArranger()
            finalResult = self.output()
            return finalResult
        else:
            return None
        
    def validator(self):
        for operand in self.operands:
            if operand not in ("+", "-"):
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
            self.operands.append(self.operandFinder(problem))
            
    def operandFinder(self, problem):
        operand = re.findall("[+-]", problem)
        if len(operand) == 0:
            operand = "[&]"
        return str(operand)[2]

    def numberFinder(self, problem):
        nums = re.findall("[0-9]+", problem)
        return nums

    def findBiggestLength(self, solution, num1, num2):
        if solution == None:
            if len(num1) > len(num2):
                return len(num1)
            else:
                return len(num2)
        else:
            if len(solution) > len(num1) and len(solution) > len(num2):
                return len(solution)
            elif len(num1) > len(num2):
                return len(num1)
            else:
                return len(num2)

    def arrangeTop(self, num1, totalLength, biggestLength):
        if len(num1) == biggestLength:
            self.topLine += " " + " " + str(num1) + " "*4
        else:
            totalToAdd = totalLength - len(num1)
            self.topLine += " "*totalToAdd
            self.topLine += str(num1) + " "*4

    def arrangeBottom(self, num2, totalLength, biggestLength, operand):
        self.bottomLine += str(operand) + " "
        if len(num2) != biggestLength:
            totalToAdd = totalLength - len(num2) - 2
            self.bottomLine += " "*totalToAdd
        self.bottomLine += str(num2) + " "*4

    def arrangeSolutionLine(self, solution, totalLength, biggestLength):
        if self.outSolution == False:
            return None
        if len(solution) == biggestLength:
            self.solutionLine += " " + " " + str(solution) + " "*4
        else:
            totalToAdd = totalLength - len(solution)
            self.solutionLine += " "*totalToAdd
            self.solutionLine += str(solution) + " "*4
        
    def solve(self, num1, num2, operand):
        solution = eval(str(num1) + str(operand) + str(num2))
        return solution

    def createDashLine(self, totalLength):
        self.dashLine += "-"*totalLength + " "*4
        
    def arithmeticArranger(self):
        for i in range(self.totalProblems - 1):
            if self.outSolution == True:
                solution = self.solve(self.num1[i], self.num2[i], self.operands[i])
            else:
                solution = None
            biggestLength = self.findBiggestLength(str(solution), self.num1[i], self.num1[i])
            totalLength = biggestLength + 2
            self.arrangeTop(self.num1[i], totalLength, biggestLength)
            self.arrangeBottom(self.num2[i], totalLength, biggestLength, self.operands[i])
            self.arrangeSolutionLine(str(solution), totalLength, biggestLength)
            self.createDashLine(totalLength)
    
    def output(self):
        finalResult = self.topLine + "\n" + self.bottomLine + "\n" + self.dashLine
        if self.outSolution == True:
            finalResult += "\n" + self.solutionLine
        #print(finalResult)
        return finalResult
