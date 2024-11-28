# Simple Calculator Program for Beginners

# Step 1: Ask the user to input the first number
num1 = input("Enter the first number: ")

# Step 2: Ask the user to input the second number
num2 = input("Enter the second number: ")

# Step 3: Ask the user to input the operation
operation = input("Enter the operation (+, -, *, /): ")

# Step 4: Convert the input numbers from strings to integers
num1 = int(num1)
num2 = int(num2)

# Step 5: Perform the chosen operation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    result = "Invalid operation."

# Step 6: Display the result
print("The result is:", result)
