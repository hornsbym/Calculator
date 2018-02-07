"""
Author: Mitchell Hornsby & Collin Sherman
File: calculator.py
Project 2
"""

class Calculator(object):
    """Models a calculator."""

    def __init__(self):
        """Sets up the model."""

        #Keeps track of the total, previous operator and previous operand for the calculator object.
        self.total = None
        self.previousOperator = None
        self.previousOperand = None


    def clear(self):
        """Resets the calculator to its initial state."""
        self.total = None
        self.previousOperand = None
        self.previousOperand = None
        

    def __str__(self):
        """Returns the string representation of the total."""
        return str(self.total)
    

    def applyOperator(self, operator, operand):
        """Applies +, -, X, /, or = and updates the total."""

        #If total is None, sets the operand to the total.
        if self.total == None:
            self.total = operand

        #If user hits the '=' button, passes operand to applyEquals method.
        elif operator == "=":
            self.applyEquals(operand)

        #If the previousOperand isn't None, sets the previousOperand to None.
        elif self.previousOperand != None:
            self.previousOperand = None

        #Runs compute total with the operator and operand.
        else:
            self.computeTotal(operator, operand)

        #Sets the previousOperator value to the last operator entered, excluding '='.
        if operator != '=':
            self.previousOperator = operator
        
            
    def applyEquals(self, operand):
        """Applies the previous operator and updates the total."""
        if self.previousOperator != None:
            if self.previousOperand == None:
                self.previousOperand = operand
            self.computeTotal(self.previousOperator, self.previousOperand)


    def computeTotal(self, operator, operand):
        """Applies +, -, X, or / to the total and the operand and
        updates the total."""

        #Adds operand to the total.
        if operator == "+":
            self.total += operand

        #Subtracts the operand from the total.
        elif operator == "-":
            self.total -= operand

        #Multiplies the operand by the total.
        elif operator == "X":
            self.total *= operand

        #Divides the total by the operand.
        else:
            if operand == 0:
                self.total = 'Error'
            elif self.total % operand == 0:
                self.total //= operand
            else:
                self.total /= operand
        

def main():
    """Entry point for starting the application."""
    c = Calculator()
    print("Startup, expect None:", c)
    c.applyOperator("+", 4)
    print("0 + 4, expect 4:", c)
    c.applyOperator("+", 5)
    print("4 + 5, expect 9:", c)
    c.applyOperator("X", 2)
    print("9 X 2, expect 18:", c)
    c.applyOperator("/", 3)
    print("18 / 3, expect 6.0:", c)
    c.clear()
    print("Cleared, expect None:", c)
    c.applyOperator("+", 4)
    print("0 + 4, expect 4:", c)
    c.applyOperator("-", 5)
    print("4 - 5, expect -1:", c)
    c.applyOperator("=", 5)
    print("= with 5, expect -6:", c)

if __name__ == "__main__":
    main()
