# This entrypoint file to be used in development. Start by reading README.md
from arithmetic_arranger import ArithmeticArranger
from unittest import main

arithmeticArranger = ArithmeticArranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
arithmeticArranger.returnResults()


# Run unit tests automatically
main(module='test_module', exit=False)
