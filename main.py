#victoria capparelli
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

#misha (created decode function)
def decoder(new_pw):
    new_decoded_pw = ""
    for num in new_pw:
        num = int(num)
        new_pw = num - 3
        if new_pw < 0:
            new_pw = new_pw + 10
        new_decoded_pw += str(new_pw)
    return new_decoded_pw

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
        #misha (created elif for option 2)
        elif user_input == 2:
            orig_pw = str(input("Please enter your password to decode: "))
            decoded_pw = decoder(orig_pw)
            print(decoded_pw)
            print()
            print(f"The decoded password is {decoded_pw}, and the original password is {orig_pw}.")
        elif user_input == 3:
            condition = False
