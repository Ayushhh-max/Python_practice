def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Cannot divide by zero."
    return x / y

def calculator():
    print("Select an operation:\n1. Add (+)\n2. Subtract (-)\n3. Multiply (*)\n4. Divide (/)")

    while True:
        choice = input("\nEnter choice (1/2/3/4) or 'q' to quit: ").strip().lower()
        if choice == 'q':
            print("Goodbye!")
            break
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            operations = {'1': ('+', add), '2': ('-', subtract), '3': ('*', multiply), '4': ('/', divide)}
            symbol, func = operations[choice]
            result = func(num1, num2)
            print(f"{num1} {symbol} {num2} = {result}")
        else:
            print("Invalid choice. Please select 1, 2, 3, 4, or 'q'.")

if __name__ == "__main__":
    calculator()