def validate_input(number):
    while True:
        try:
            input_number = int(input(number))
        except ValueError:
            print("number is invalid")
            continue
        else:
            return input_number


def number_addition(first_number, second_number):
    addition = int(first_number + second_number)
    return addition


def number_subtraction(first_number, second_number):
    subtraction = int(first_number - second_number)
    return subtraction


def number_multiplication(first_number, second_number):
    multiplication = int(first_number * second_number)
    return multiplication


def number_division(first_number, second_number):
    division = int(first_number / second_number)
    return division


def check_zero(number):
    while number == 0:
        print("Cannot divide by 0")
        number = number
    return number


def user_selection(user_choice):
    while True:
        try:
            user_choice = int(input(user_choice))
        except ValueError:
            print("Invalid number")
            continue
        else:
            if user_choice == 1 or user_choice == 2 or user_choice == 3 or user_choice == 4:
                return user_choice
            else:
                print("Invalid selection")
                user_choice = user_choice


def calculation(user_choice, first_number, second_number):
    while True:
        if user_choice == 1:
            addition = number_addition(first_number, second_number)
            return addition
        elif user_choice == 2:
            subtraction = number_subtraction(first_number, second_number)
            return subtraction
        elif user_choice == 3:
            multiplication = number_multiplication(first_number, second_number)
            return multiplication
        else:
            zero_check = check_zero(second_number)
            division = number_division(first_number, zero_check)
            return division


def menu_display():
    menu = user_selection("press 1 for Addition \nPress 2 for Subtraction \nPress 3 for Multiplication \nPress 4 for "
                          "Division\n")
    return menu


selection = menu_display()
number1 = validate_input("Enter first number")
number2 = validate_input("Enter second number")

result = calculation(selection, number1, number2)
print(f"Result = {result}\n")

selection = menu_display()
