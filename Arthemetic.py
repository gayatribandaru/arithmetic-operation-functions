import argparse
import unittest
import tkinter as tk

# Define the arithmetic operation functions
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero")
    return num1 / num2

# Define the unit tests for the arithmetic operation functions
class TestOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        with self.assertRaises(ValueError):
            divide(6, 0)

# Define the main application
class CalculatorApp:
    def __init__(self, master):
        # Create the GUI elements
        self.num1_label = tk.Label(master, text="First number:")
        self.num1_label.grid(row=0, column=0)
        self.num1_entry = tk.Entry(master)
        self.num1_entry.grid(row=0, column=1)

        self.num2_label = tk.Label(master, text="Second number:")
        self.num2_label.grid(row=1, column=0)
        self.num2_entry = tk.Entry(master)
        self.num2_entry.grid(row=1, column=1)

        self.operator_label = tk.Label(master, text="Operator:")
        self.operator_label.grid(row=2, column=0)
        self.operator_var = tk.StringVar(value="+")
        self.operator_menu = tk.OptionMenu(master, self.operator_var, "+", "-", "*", "/")
        self.operator_menu.grid(row=2, column=1)

        self.calculate_button = tk.Button(master, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=3, column=0, columnspan=2)

        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=4, column=0, columnspan=2)

    def calculate(self):
        try:
            # Get the input values and selected operator
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            operator = self.operator_var.get()

            # Perform the calculation based on the selected operator
            if operator == "+":
                result = add(num1, num2)
            elif operator == "-":
                result = subtract(num1, num2)
            elif operator == "*":
                result = multiply(num1, num2)
            elif operator == "/":
                result = divide(num1, num2)

            # Display the result
            self.result_label.config(text=f"Result: {result}")
        except ValueError:
            # Display an error message if the input is invalid
            self.result_label.config(text="Invalid input")

# Define the command-line interface
def main():
    parser = argparse.ArgumentParser(description="Perform basic arithmetic operations")
    parser.add_argument("num1", type=float, help="First operand")
    parser.add_argument("num2", type=float, help="Second operand")
    parser.add_argument("operator", choices=["+", "-", "*", "/"], help="Operator (+, -, *, /)")
    args = parser.parse_args()

    # Perform the calculation based on the command-line arguments
    try:
        if args.operator == "+":
            result = add(args.num1, args.num2)
        elif args.operator == "-":
            result = subtract(args.num1, args.num2)
        elif args.operator == "*":
            result = multiply(args.num1, args.num2)
        elif args.operator == "/":
            result = divide(args.num1, args.num2)

        # Display the result
        print(f"Result: {result}")
    except ValueError as e:
        # Display an error message if the input is invalid
        print(e)

if __name__ == "__main__":
    # Run the unit tests
    unittest.main(argv=[""], exit=False)

    # Run the GUI application
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

    # Run the command-line interface
    main()