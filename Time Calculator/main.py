# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import AddTime
from unittest import main

addTime = AddTime("11:06 PM", "2:02")
print(addTime.newTime())


# Run unit tests automatically
main(module='test_module', exit=False)
