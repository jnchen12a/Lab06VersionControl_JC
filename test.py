# Encoding function
def encode(num):
    return_num = ''
    for digit in num:
        return_num = str(int(digit) + 3) + return_num

    return return_num
# Decoding function
def decode(num):
    return_num = ''
    for digit in num:
        return_num = str(int(digit) - 3) + return_num

    return return_num

# Start of main if dunder
if __name__ == '__main__':
    encoded_password = False
    # Start of main while loop
    while True:
        # Printing menu
        print('Menu')
        print('-----------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print()
        choice = input('Please enter an option: ')
        if choice == '1': # Encode a password
            while True:
                try:
                    password = input('Please enter your password to encode: ')
                    encoded_password = encode(password)
                    print('Your password has been encoded and stored!')
                    print()
                    break
                except: # Bozo check, user enters non-number
                    print('Please enter a numerical password')
        elif choice == '2': # Decode a password
            if not encoded_password: # Bozo check, nothing to decode
                print('No password to decode.')
                print()
                continue
            decoded_password = decode(encoded_password)
            print(f'The encoded password is {encoded_password}, and the original password is {decoded_password}.')
            print()
        elif choice == '3': # Quitting out
            quit()
        else: # Bozo check, user doesn't choose a valid choice
            print('Please enter a valid choice.')
            print()
    # End of main while loop
# End of main if dunder