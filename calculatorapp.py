"""
Authors: Mitchell Hornsby & Collin Sherman
Project 1
File: calculatorapp.py
"""

from breezypythongui import EasyFrame
from tkinter.font import Font
from calculator import Calculator

class CalculatorApp(EasyFrame):
    """Creates and displays the window, labels, and contains the math functions of the calculator."""


    def __init__(self):
        """Sets up the window, label, and buttons."""

        #Creates the window.
        EasyFrame.__init__(self, "Calculator", resizable = False)

        #Creates the data model Calculator.
        self.calculator = Calculator()

        #Keeps track of when the user enters an input.
        self.operatorEntered = False

        #Creates the colored panels.
        for column in range(5):
            numberBarPanel = self.addPanel(row = 0, column = column, background = "black")

        for row in range(1, 6):
            symbolPanel = self.addPanel(row = row, column = 4, background = 'orange')

        for column in range (4):
            topPanel = self.addPanel(row = 1, column = column, background = "snow3")

        for row in range (2, 6):
            for column in range (0, 3):
                numberPanel = self.addPanel(row = row, column = column, background = "snow2")

        #Creates fonts.
        barFont = Font(family = "San Francisco", size = 20)
        
        #Creates the number bar at the top of the calculator.
        self.digits = self.addLabel("0", row= 0, column= 0, columnspan= 5, sticky= "E", background = 'black', foreground = 'white', font = barFont)

        #Creates button for clear.
        self.clearButton= self.addButton(text= "AC", row= 1, column= 0, command= self.clearCommand)
        self.clearButton['background'] = 'snow3'
        
        #Creates button for +/-.
        negativeButton= self.addButton(text= "+/-", row= 1, column= 1, command= self.negativeCommand)
        negativeButton['background'] = 'snow3'
        
        #Creates button for %
        percentButton= self.addButton(text= "%", row= 1, column= 2, command= self.percentCommand)
        percentButton['background'] = 'snow3'

        #Creates side row of operator symbols.
        sideSymbols= ["/", "X", "-", "+", "="]
        row= 1
        for symbol in sideSymbols:
            symbolButton = self.addButton(text= symbol, row= row, column= 4)
            symbolButton["command"] = self.operatorCommand(symbol)
            symbolButton['foreground'] = 'white'
            symbolButton['background'] = 'orange'
            row += 1
            
        #Goes through and creates a grid with numbers 1-9.
        digit= 7
        for row in range(2, 5):
            for column in range(3):
                numberButton = self.addButton(str(digit), row, column)
                numberButton["command"] = self.numberCommand(str(digit))
                numberButton['background'] = 'snow2'
                if digit == 9:
                    digit = 3
                elif digit == 6:
                    digit = 0
                digit += 1

        #Creates 0 button.
        zeroButton = self.addButton(text= "0              ", row= 5, column = 0, columnspan = 2, command = self.numberCommand("0"))
        zeroButton['background'] = 'snow2'

        #Creates . button.
        self.decimalButton = self.addButton(text= ".", row = 5, column = 2, command = self.decimalCommand, state = 'normal')
        self.decimalButton['background'] = 'snow2'
        

    def clearCommand(self):
        """Clears the number bar."""

        #Sets the number in the number bar to 0.
        self.digits["text"] = "0"
        if self.clearButton["text"] == "AC":
            self.calculator.clear()
            self.operatorEntered = False
        else:
            self.clearButton["text"] = "AC"

        #Reactivates the decimal button.
        self.decimalButton['state'] = 'active'
        
        
    def negativeCommand(self):
        """Makes number in number bar negative."""

        #Checks to see if the number bar only contains 0; if true, returns nothing.
        if self.digits["text"] == '0':
            return

        #Checks to see if a negative exists in the number bar; if true, removes it.
        if '-' in self.digits['text']:
            self.digits['text'] = self.digits['text'][1:]

        #Adds a negative to a non-negative, non-zero integer.
        else:
            self.digits["text"] = "-" + self.digits["text"]
        

    def percentCommand(self):
        """Divides number in number bar by 100."""
        if self.digits["text"] == '0':
            return
        else:
            number = float(self.digits["text"])
            number /= 100
            self.digits["text"] = str(number)
            return self.digits["text"]
        
        
        
    def operatorCommand(self, buttonText):
        """Perform operation for specific operator button pressed."""
        def applyOperator():
            number = self.digits["text"]
            if number == 'Error':
                return
            if "." in number:
                number = float(number)
            else:
                number = int(number)
            self.calculator.applyOperator(buttonText, number)
            self.digits["text"] = str(self.calculator)
            self.operatorEntered = True
        return applyOperator
            

        
    def numberCommand(self, buttonText):
        """Define and return the event handler for a button."""
        def addDigit():
            """Allows calculator to display number of button pushed."""

            #Checks to see if the number bar is a 0; if so, returns an empty string.
            if self.digits["text"] == "0" or self.operatorEntered == True or self.digits["text"] == 'Error':
                self.digits["text"] = ""
                self.operatorEntered = False
            #Adds the text from the digit button pressed onto the end of the number bar.    
            self.digits["text"] += buttonText

            #Sets the text on the clear button to AC if the number bar only contains 0.
            if self.digits["text"] == "0" and self.operatorEntered == False:
                self.clearButton["text"]= "AC"

            #Sets the text on the clear button to C if the number bar contains anything other than 0.
            if self.digits["text"] == "0" and self.operatorEntered == True:
                self.clearButton["text"]= " C "
            else:
                self.clearButton["text"]= " C "

        return addDigit
        

    def decimalCommand(self):
        """Adds decimal to number line when button is pressed."""

        #Adds a decimal to the end of the text.
        self.digits["text"] += "."

        #Changes the text on the clear button from AC to C.
        self.clearButton["text"]= " C "

        #Disables the decimal button.
        self.decimalButton['state'] = 'disabled'
        

def main():
    """The starting point for launching the program."""
    CalculatorApp().mainloop()


#Instantiates and pops up the window.
if __name__ == "__main__":
    main()
