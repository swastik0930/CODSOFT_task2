def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero."
    
while True:
    
    # Display operation choices
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # Prompt user for operation choice
    choice = input("Enter the operation number (1, 2, 3, or 4): ")

    # Prompt user for input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform calculation based on user choice
    if choice == '1':
        result = add(num1, num2)
        operation = '+'
    elif choice == '2':
        result = subtract(num1, num2)
        operation = '-'
    elif choice == '3':
        result = multiply(num1, num2)
        operation = '*'
    elif choice == '4':
        result = divide(num1, num2)
        operation = '/'
    else:
        print("Invalid operation choice.")
        result = None

    # Display the result
    if result is not None:
        print(f"{num1} {operation} {num2} = {result}")

    # Ask the user if they want to Continue 
    next_calculation = input("Lets do another calculation? (yes/no): ")
    if next_calculation == "no":
        break