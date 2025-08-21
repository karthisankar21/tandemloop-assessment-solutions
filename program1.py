# program1.py
# A simple calculator that keeps inputs and only re-prompts what was wrong.

class Calculator:
    def __init__(self, a: float, b: float, operation: str):
        self.a = a
        self.b = b
        self.operation = operation.lower()

    def calculate(self):
        if self.operation == 'add':
            return self.a + self.b
        elif self.operation == 'sub':
            return self.a - self.b
        elif self.operation == 'mul':
            return self.a * self.b
        elif self.operation == 'div':
            # We already ensure b != 0 before calling calculate()
            return self.a / self.b
        else:
            return "❌ Error: Invalid operation."


VALID_OPS = {'add', 'sub', 'mul', 'div'}

def prompt_float(msg: str) -> float:
    while True:
        s = input(msg)
        try:
            return float(s)
        except ValueError:
            print(f"❌ Error: '{s}' is not a number. Please enter a numeric value.")

def prompt_operation(msg: str = "Enter operation (add, sub, mul, div): ") -> str:
    while True:
        op = input(msg).strip().lower()
        if op in VALID_OPS:
            return op
        print(f"❌ Error: '{op}' is not a valid operation. Please choose from add, sub, mul, div.")

def main():
    print("Starting the calculator program...")
    while True:
        a = prompt_float("\nEnter first number: ")
        b = prompt_float("Enter second number: ")

        # Ask operation repeatedly until valid (does NOT re-ask numbers)
        operation = prompt_operation()

        # If division chosen, ensure b is not zero (re-ask ONLY the second number)
        if operation == 'div':
            while b == 0.0:
                print("Error: Division by zero is not allowed for 'div'.")
                b = prompt_float("Enter a NON-ZERO second number: ")

        # Calculate and show result
        calc = Calculator(a, b, operation)
        result = calc.calculate()
        print(f"✅ The result is: {result}")

        while True:
            again = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
            if again == 'yes' or again == 'y':
                break  # start a new calculation
            elif again == 'no' or again == 'n':
                print("👋 Exiting calculator. Goodbye!")
                return  # exit main loop
            else:
                print("⚠️ Please type 'yes' or 'no'.")


if __name__ == "__main__":
    main()
