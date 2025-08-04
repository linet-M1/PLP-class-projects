num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
# Display operation menu
print("\nAvailable operations:")
print("+ : Addition")           
print("- : Subtraction")
print("* : Multiplication")                     
print("/ : Division")   
# Get user's operation choice
operation = input("Enter your chosen operation (+, -, *, /): ") 
# Perform calculation based on operation
if operation == "+":            
    result = num1 + num2
    print(f"\nResult: {num1} + {num2} = {result}")  
elif operation == "-":
    result = num1 - num2
    print(f"\nResult: {num1} - {num2} = {result}")  
elif operation == "*":
    result = num1 * num2
    print(f"\nResult: {num1} * {num2} = {result}")      
elif operation == "/":
    if num2 == 0:
        print("\nError: Cannot divide by zero!")
    else:
        result = num1 / num2
        print(f"\nResult: {num1} / {num2} = {result}")  
else:
    print("\nError: Invalid operation selected. Please choose +, -, *, or /.")  
# End of calculator.py