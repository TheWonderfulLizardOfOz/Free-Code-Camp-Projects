import re
class Arithmetic_arranger():
    def __init__(self, problems):
        self.problems = problems
        self.num1 = []
        self.num2 = []
        self.operands = []
        self.totla_problems = len(problems)
        self.individual_problems()
        self.arithmetic_arranger()

    def individual_problems(self):
        for problem in self.problems:
            nums = self.number_finder(problem)
            self.num1.append(nums[0])
            self.num2.append(nums[1])
            self.operands.append(self.operand_finder(problem))
            print(self.num1)
            print(self.num2)
            print(self.operands)
            
    def operand_finder(self, problem):
        operand = re.findall("[+-]", problem)
        return operand

    def number_finder(self, problem):
        nums = re.findall("[0-9]+", problem)
        return nums
    
    def arithmetic_arranger(self, problems):
        return arranged_problems
