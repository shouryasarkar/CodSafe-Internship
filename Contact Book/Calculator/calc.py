def take_input(operation):
    user_input = []
    if operation in [1, 2]:  # Addition or Multiplication
        n = int(input("How many numbers do you want to enter: "))
        for _ in range(n):
            number = float(input("Enter the number: "))
            user_input.append(number)
    else:  # Subtraction or Division
        for _ in range(2):
            number = float(input("Enter the number: "))
            user_input.append(number)
    return user_input

def addition(numbers):
    return sum(numbers)

def multiplication(numbers):
    product = 1
    for i in numbers:
        product *= i
    return product

def subtraction(numbers):
    number_1, number_2 = numbers
    return number_1 - number_2

def division(numbers):
    number_1, number_2 = numbers
    if number_2 == 0:
        return "Error: Division by zero is not allowed."
    return number_1 / number_2

print("Select the operations:")
print("1) Addition")
print("2) Multiplication")
print("3) Subtraction")
print("4) Division")

# Program starts to execute from here
select = int(input("Select operation (1/2/3/4): "))

if select in [1, 2, 3, 4]:
    numbers = take_input(select)
    if select == 1:
        print("Result:", addition(numbers))
    elif select == 2:
        print("Result:", multiplication(numbers))
    elif select == 3:
        print("Result:", subtraction(numbers))
    elif select == 4:
        print("Result:", division(numbers))
else:
    print("Invalid selection. Please select a valid operation (1/2/3/4).")
