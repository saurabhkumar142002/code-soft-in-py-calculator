num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nSelect operation:")
print("3. Addition (+)")
print("4. Subtraction (-)")
print("5. Multiplication (*)")
print("6. Division (/)")

choice = input("Enter choice (3/4/5/6): ")

if choice == '3' or choice == '+':
    result = num1 + num2
    print(f"\nResult: {num1} + {num2} = {result}")

elif choice == '4' or choice == '-':
    result = num1 - num2
    print(f"\nResult: {num1} - {num2} = {result}")

elif choice == '5' or choice == '*':
    result = num1 * num2
    print(f"\nResult: {num1} * {num2} = {result}")

elif choice == '6' or choice == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"\nResult: {num1} / {num2} = {result}")
    else:
        print("\nError! Division by zero is not allowed.")
else:
    print("\nInvalid input! Please select a valid operation.")
