from PyQt6.QtWidgets import (
    QApplication, QWidget, QGridLayout, QPushButton, QLineEdit, QLabel
)
from operations import * 
from calculator import *
import sys 

class CalculatorWindow(QWidget):
  def __init__(self):
    super().__init__()
    self.init_ui()
    
  def operation_clicked(self):
    # Get the button text (operation symbol)
    button_text = self.sender().text()
    # Get current display text (user input)
    current_text = self.display.text()

    # ... (error handling checks as discussed previously)

    # Update display with the operation symbol
    self.display.setText(current_text + button_text)

    # Store the operation symbol for later use
    self.current_operation = button_text

  def equal_clicked(self):
    # Get the operands and operation from display 
    # and stored variables
    display_text = self.display.text()
    current_operation = self.current_operation

    # ... (optional error handling)

    # Extract operands based on the current operation
    if current_operation == "+":
        split_text = display_text.split("+")
        operand1 = float(split_text[0])
        operand2 = float(split_text[1])
    elif current_operation == "-":
        split_text = display_text.split("-")
        operand1 = float(split_text[0])
        operand2 = float(split_text[1])
    elif current_operation == "*":
        split_text = display_text.split("*")
        operand1 = float(split_text[0])
        operand2 = float(split_text[1])  
    elif current_operation == "/":
        split_text = display_text.split("/")
        operand1 = float(split_text[0])
        operand2 = float(split_text[1])      
    else:
        # Handle invalid operation symbol
        zero_num_operation()
        return

    # Call the perform_operation function
    result = perform_operation(operand1, operand2, current_operation)

    # Update the display with the result
    self.display.setText(str(result))    
  
    
  def init_ui(self):
    self.setWindowTitle("Calculator App")
    self.setGeometry(300, 300, 400, 500)  

    # Create layout for widgets
    grid_layout = QGridLayout()
    self.setLayout(grid_layout)

    # Display field for user input and results
    self.display = QLineEdit()
    self.display.setReadOnly(True)  
    # Make display read-only
    grid_layout.addWidget(self.display, 0, 0, 1, 4)  
    # Span across 4 columns

    # Function buttons (add a button for each operation)
    button_add = QPushButton("+")
    button_add.clicked.connect(self.operation_clicked)  
    # Connect to operation_clicked
    grid_layout.addWidget(button_add, 1, 0, 1, 1)
    
    # Subtraction button to perform calculation
    button_minus = QPushButton("-")
    button_minus.clicked.connect(self.operation_clicked)
    grid_layout.addWidget(button_minus, 1, 1, 1, 1)
    
    # Multiplication button to perform calculation
    button_multiply = QPushButton("*")
    button_multiply.clicked.connect(self.operation_clicked)
    grid_layout.addWidget(button_multiply, 1, 2, 1, 1)
    
    # Division button to perform calculation
    button_divide = QPushButton("/")
    button_divide.clicked.connect(self.operation_clicked)
    grid_layout.addWidget(button_divide, 1, 3, 1, 1)

    
    

    # ... Add similar buttons for other operations (subtract, multiply, divide, etc.)

    # Numeric buttons (0-9)
    # for i in range(7, 2, -1):  
    #   # Loop to create buttons for 7 to 1
    #   for j in range(0, 3):
    #     button_text = str((i - 2) * 3 + j) 
    #     # Calculate button text (1 to 9)
    #     button = QPushButton(button_text)
    #     button.clicked.connect(self.number_clicked)
    #     grid_layout.addWidget(button, i, j, 1, 1)
        
    button_positions = {
      1: (4, 2),  # Row 2, Column 2
      2: (4, 1),  # Row 2, Column 1
      3: (4, 0),  # Row 2, Column 0
      4: (3, 2),  # Row 1, Column 2
      5: (3, 1),  # Row 1, Column 1
      6: (3, 0),  # Row 1, Column 0
      7: (2, 2),  # Row 0, Column 2 (adjust based on operator placement)
      8: (2, 1),  # Row 0, Column 1 (adjust based on operator placement)
      9: (2, 0),  # Row 0, Column 0 (adjust based on operator placement)
  }

    for value, (row, col) in button_positions.items():
      button_text = str(value)
      button = QPushButton(button_text)
      button.clicked.connect(self.number_clicked)
      grid_layout.addWidget(button, row, col, 1, 1)
      
   
    # Button for decimal point
    button_decimal = QPushButton(".")
    button_decimal.clicked.connect(self.decimal_clicked)
    grid_layout.addWidget(button_decimal, 5, 0, 1, 1)
    #coord: row, column/position, sizes.

    # button_minus = QPushButton("-")
    # button_minus.clicked.connect(self.minus_clicked)
    # grid_layout.addWidget(button_minus, 4, 2, 1, 2)
    
    
    # Equal button to perform calculation
    button_equal = QPushButton("=")
    button_equal.clicked.connect(self.equal_clicked)
    grid_layout.addWidget(button_equal, 5, 2, 1, 1)
    
    # zero button
    button_zero = QPushButton("0")
    button_zero.clicked.connect(self.number_clicked)
    grid_layout.addWidget(button_zero, 5, 1, 1, 1)

    # Clear button to clear the display
    button_clear = QPushButton("C")
    button_clear.clicked.connect(self.clear_clicked)
    grid_layout.addWidget(button_clear, 5, 3, 1, 1)

    self.show()  # Show the window
    window = QWidget()
    
    window.show()

  # Function to handle button clicks (generic example)
  def button_clicked(self):
    # Get the button text (operation symbol)
    button_text = self.sender().text()

    # Update display with the operation symbol
    self.display.setText(self.display.text() + button_text)

    # Store the operation symbol for later use
    self.current_operation = button_text  # Assuming you have a variable to store the operation


    # Update display based on operation (logic depends on your implementation)
    # ... (e.g., store operand or perform calculation)

  # Implement similar functions for other button click events (add_clicked, etc.)
  # These functions should call appropriate operations functions from calculator_operations.py

  def number_clicked(self):
    button_text = self.sender().text()

    # Update the display with the pressed number
    self.display.setText(self.display.text() + button_text)
    
  def decimal_clicked(self):
    # Check if decimal point already exists in the display
    if "." not in self.display.text():
      # Add decimal point to the display
      self.display.setText(self.display.text() + ".")
  
  

      

  def clear_clicked(self):
    # Clear the display
    self.display.setText("")



    


if __name__ == "__main__":
  app = QApplication([])
  
  window = CalculatorWindow()
  sys.exit(app.exec())
