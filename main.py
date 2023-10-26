
def menu():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")


def encoder(pw):
    encoded_pw = ""
    for char in pw:
        current_num = int(char) + 3
        if current_num >= 10:
            current_num = current_num % 10

        encoded_pw += str(current_num)

    return encoded_pw


if __name__ == '__main__':
    condition = True
    encoded_password = ""
    password = ""
    while condition:
        menu()
        user_input = int(input("Please enter an option: "))
        if user_input == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encoder(password)
            print("Your password has been encoded and stored!\n")
        elif user_input == 2:
            print(f"The encoded password is {encoded_password}, and the original password is {password}\n")
        elif user_input == 3:
            condition = False
