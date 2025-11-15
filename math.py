try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    print(f"Addition: {a + b}")
    print(f"Subtraction: {a - b}")
except ValueError:
    print("Please enter valid numbers.")
