# User input for Addition Multiplication and Substraction
def take_input(operation):
    user_input = []
    # Addition or Multiplication 
    if operation in [1,2]:
        n = int(input("How many numbers do you want to enter: "))
        for _ in range(n):
            number = float(input("Enter the number: "))
            user_input.append(number)
    # Substraction
    else:
        for _ in range(2):
            number = float(input("Enter the number: "))
            user_input.append(number)
    return user_input

# User input for Division 
def take_division_input():
    user_input = []
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    user_input.append(numerator)
    user_input.append(denominator)
    return user_input


# Perform the Calculations 
def calculation(operation, numbers):
    if operation == 1:
        return addition(numbers)
    elif operation == 2:
        return multiplication(numbers)
    elif operation == 3:
        return substraction(numbers)
    elif operation == 4:
        return division(numbers)


# Addition
def addition(numbers):
    number_1, number_2 = numbers
    return sum(numbers)

# Mutiplication
def multiplication(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product

# Substraction
def substraction(numbers):
    number_1, number_2 = numbers
    return number_1 - number_2

# Division
def division(numbers):
    number_1, number_2 = numbers
    if number_2 == 0:
        return "Error: Divion by zero is not possible."
    return number_1 / number_2

# View Result
def view_result(result):
    print(f"Result: {result}")


# Execute Calculator 
def execute_calculator():
    execute_again = "yes"

    while execute_again.lower() == "yes":
        print("\nSelect the operations:")
        print("1. Addition")
        print("2. Multiplication")
        print("3. Substraction")
        print("4. Division")

        while True:
            try:
                operation = int(input("Select operation (1/2/3/4)"))
                if operation in [1,2,3,4]:
                    break
                else:
                    print("Invalid selection. Please enter a valid operation(1/2/3/4)")
            except ValueError:
                print("Invalid input. Please enter a number.")

        if operation == 4:
            numbers = take_division_input()
        else:
            numbers = take_input(operation)

        result = calculation(operation,numbers)
        view_result(result)

        execute_again = input("\nDo you want to perform another calculation? (Yes/No): ")
    
    print("\nThank You for using the calculator.")

# Execute the calculator
execute_calculator()
