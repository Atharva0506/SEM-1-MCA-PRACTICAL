# 4.	Create a  module  ‘arithmetic’ which has  classes . (substraction , division , addition and multiplication)

#  arithmetic.py create seprate file
class Arithmetic:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b if self.b != 0 else "Division by zero is not allowed."

#  main.py import above code in main file
# from arithmetic import Arithmetic 

# Create an instance
calc = Arithmetic(10, 5)

# Perform operations
print("Addition: ", calc.add())        # Output: 15
print("Subtraction: ", calc.subtract())  # Output: 5
print("Multiplication: ", calc.multiply())  # Output: 50
print("Division: ", calc.divide())    # Output: 2.0
