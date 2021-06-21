import re
class Arithmetic_arranger():
    def __init__(self, problems):
        self.problems = problems
        self.num1 = []
        self.num2 = []
        self.operands = []
        self.totalProblems = len(problems)
        self.topLine = " "
        self.bottomLine = ""
        self.individualProblems()
        self.arithmeticArranger()

    def individualProblems(self):
        for problem in self.problems:
            nums = self.numberFinder(problem)
            self.num1.append(nums[0])
            self.num2.append(nums[1])
            self.operands.append(self.operandFinder(problem))
            print(self.num1)
            print(self.num2)
            print(self.operands)
            
    def operandFinder(self, problem):
        operand = re.findall("[+-]", problem)
        return operand

    def numberFinder(self, problem):
        nums = re.findall("[0-9]+", problem)
        return nums

    def findBiggestLength(self, num1, num2):
        if len(num1) > len(num2):
            return len(num1)
        else:
            return len(num2)

    def arrangeTop(self, num1, totalLength, biggestLength):
        if len(num1) == biggestLength:
            self.topLine += " " + " " + str(num1) + " "
        else:
            totalToAdd = totalLength - len(num1)
            self.topLine += " "*totalToAdd
            self.topLine += str(num1) + " "

    def arrangeBottom(self, num2, totalLength, biggestLength):
        self.bottomLine += "+ "
        if len(num2) != biggestLength:
            totalToAdd = totalLength - len(num2) - 2
            self.bottomLine += " "*totalToAdd
        self.bottomLine += str(num2) + " "
            
    def arithmeticArranger(self):
        for i in range(self.totalProblems):
            biggestLength = self.findBiggestLength(self.num1[i], self.num1[i])
            totalLength = biggestLength + 2
            self.arrangeTop(self.num1[i], totalLength, biggestLength)
            self.arrangeBottom(self.num2[i], totalLength, biggestLength)
        print(self.topLine)
        print(self.bottomLine)
