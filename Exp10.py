AIM: WRITE A PROGRAM TO CREATE A SIMPLE CALCULATOR USING A SWITCH CASE AND FUNCTION FOR EVERY OPERATION.

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero."

# Function to perform calculations based on user input
def perform_calculation(operator, num1, num2):
    calc = Calculator()
    if operator == 1:
        result = calc.add(num1, num2)
    elif operator == 2:
        result = calc.subtract(num1, num2)
    elif operator == 3:
        result = calc.multiply(num1, num2)
    elif operator == 4:
        result = calc.divide(num1, num2)
    else:
        result = "Invalid operator"
    return result

# Main program
print("Simple Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

try:
    operator = int(input("Select operation (1/2/3/4): "))
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = perform_calculation(operator, num1, num2)

    print("Result: {}".format(result))

except ValueError:
    print("Invalid input. Please enter valid numbers.")
except Exception as e:
    print("An error occurred:", str(e))
