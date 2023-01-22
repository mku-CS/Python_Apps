import string
import random
import datetime

characters = string.ascii_lowercase

# ==== COLORS DEFINITION ====
REGULAR = "\033[39m"
GREEN = "\033[92m"
ORANGE = "\033[93m"
BOLD = '\33[1m'
NORMAL = '\33[0m'
# ===========================

def input_validation():
    try:
        if int(pass_len) < 8:
            print("Too short, not safe!")
        elif int(pass_len) > 20:
            print("Please specify the length between 8 - 20 characters.")
        else:
            return True
    except Exception:
        print(" >>> Enter number (8-20) <<< ")


def yes_no_validation(user_input):
    if user_input.upper() == "Y" or user_input.upper() == "N":
        return True
    else:
        print(" >>> type y or n! <<<")


def password_type(if_upper, if_special, if_digits):
    global characters
    if if_upper.upper() == "Y":
        characters += string.ascii_uppercase
    if if_special.upper() == "Y":
        characters += "!@#$%^&*"
    if if_digits.upper() == "Y":
        characters += string.digits

def generate_password():
    password = []
    for i in range(0, int(pass_len)):
        password.append(random.choice(characters))
    current_time = str(datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S"))
    passwords_file = open("savedPasswords.txt", "a")
    passwords_file.write("DATETIME: " + current_time + "\n => " + "".join(password) + "\n\n")
    return password


print(f"\n\t{BOLD}{GREEN}Generate your safe password in few simple steps.{NORMAL}\n")

while True:
    pass_len = (input(f"{BOLD}{ORANGE}1.{REGULAR} How many characters? (8-20){NORMAL}\n >> "))
    if input_validation():
        break

while True:
    incl_spec_chars = input(f"{BOLD}{ORANGE}2.{REGULAR} Include special characters? (y/n){NORMAL}\n >> ")
    if yes_no_validation(incl_spec_chars):
        break
while True:
    incl_uppercase = input(f"{BOLD}{ORANGE}3.{REGULAR} Include uppercase characters? (y/n){NORMAL}\n >> ")
    if yes_no_validation(incl_uppercase):
        break
while True:
    incl_digits = input(f"{BOLD}{ORANGE}4.{REGULAR} Include digits? (y/n){NORMAL}\n >> ")
    if yes_no_validation(incl_digits):
        break

password_type(incl_uppercase, incl_spec_chars, incl_digits)
#print(characters)
user_password = generate_password()
user_pass_string = "".join(user_password)

print(f"\n\t\t{BOLD}{GREEN}Your password:\n\n"
      f"\t{ORANGE} ==> {REGULAR}{user_pass_string}{ORANGE} <== \n {NORMAL}")



# TODO:
# 1. ensure at least 2 special characters / digits are included if user chooses to include them
# 2. OR ask user how many special characters / digits user wants in password
# 3. write password to file - DONE
# 4. timestamp in output file - DONE
#
#




