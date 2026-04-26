def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Enter the valid number")

def get_operator():
    valid_operators = ['+', '-', '*', '/']
    while True:
        op = input("Enter operation (+, -, *, /): ").strip()
        if op in valid_operators:
            return op
        else:
            print(f" Invalid operator. Please use one of: {', '.join(valid_operators)}")

def add(a, b):
    """Addition operation"""
    return a + b

def subtract(a, b):
    """Subtraction operation"""
    return a - b

def multiply(a, b):
    """Multiplication operation"""
    return a * b

def divide(a, b):
    """
    Division operation with zero-check
    Returns error message if dividing by zero
    """
    if b == 0:
        return "Error: Division by zero is not allowed"
    return a / b

def calculator():
    num1 = get_number("Enter first number\n")
    operator = get_operator()
    num2 = get_number("Enter the second number\n")

     # Processing Phase
    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        result = divide(num1, num2)
    
        # Output Phase
    display_result(num1, operator, num2, result)


# ============= OUTPUT/DISPLAY UNIT =============

def display_result(num1, operator, num2, result):
    """
    Display the calculation result in a formatted way
    """
    print("\n" + "=" * 40)
    if isinstance(result, str) and result.startswith("Error"):
        print(f"{result}")
    else:
        print(f" {num1} {operator} {num2} = {result}")
    print("=" * 40 + "\n")
    
def main():
    """
    Main entry point - allows continuous calculations
    """
    while True:
        print(calculator())
        
        # Ask if user wants to continue
        continue_calc = input("Do another calculation? (yes/no): ").strip().lower()
        if continue_calc not in ['yes', 'y']:
            print("\nThank you for using the calculator!")
            break


if __name__ == "__main__":
    main()

