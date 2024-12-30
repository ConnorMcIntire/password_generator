import random
import string

def generate_password(min_length,numbers=True,special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd

while True:
    try: 
        min_length = int(input("Enter the minimum length of password: "))
        break
    except ValueError:
        print("Please enter a valid number")

while True:
    has_number_input = input("Do you want to have numbers (y/n)? ").lower()
    if has_number_input in ["y", "n"]:
        has_number = has_number_input == "y"
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

while True:
    has_special_input = input("Do you want to have symbols (y/n)? ").lower()
    if has_special_input in ["y", "n"]:
        has_special = has_special_input == "y"
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

        
pwd = generate_password(min_length,has_number,has_special)
print("The generated password is: ",pwd)


