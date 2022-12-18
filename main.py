def validate_input(number):
    while True:
        try:
            input_number = int(input(number))
        except ValueError:
            print("number is invalid")
            continue
        else:
            return input_number


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


def calculation():
    while True:
        user_choice = user_selection()
        if user_choice == 1:
            print("Addition")
        elif user_choice == 2:
            print("Subtraction")
        elif user_choice == 3:
            print("Multiplication")
        else:
            print("Division")
            break


def number_addition():
    first_number = validate_input("Enter first number")
    print(f"First number {first_number}")

    second_number = validate_input("Enter second number")
    print(f"Second number {second_number}")

    addition = int(first_number + second_number)
    print(f"Addition is {addition}")


def number_subtraction():
    first_number = validate_input("Enter first number")
    print(f"First number {first_number}")

    second_number = validate_input("Enter second number")
    print(f"Second number {second_number}")

    addition = int(first_number - second_number)
    print(f"Addition is {addition}")


selection = user_selection("press 1 for Addition \nPress 2 for Subtraction \nPress 3 for Multiplication \nPress 4 for "
                           "Division\n")

# first_number = validate_input("Enter first number")
# print(f"First number {first_number}")
#
# second_number = validate_input("Enter second number")
# print(f"Second number {second_number}")
