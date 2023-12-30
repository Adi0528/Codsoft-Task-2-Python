def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operation"

num1 = float(input("Enter First number: "))
num2 = float(input("Enter Second number: "))
operation = input("Which function do you want to perform ? (+, -, *, /): ")

result = calculate(num1, num2, operation)
print(f"The Result For your required Input is: {result}")